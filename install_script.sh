#!/usr/bin/bash

set -euo pipefail

if [ ! -d miniconda3 ]; then
    echo "### Downloading and installing miniconda3..."
    set -x
    mkdir -p miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3/miniconda.sh
    bash miniconda3/miniconda.sh -b -u -p miniconda3
    rm miniconda3/miniconda.sh
    set +x
fi

echo "### Conda init..."
. miniconda3/etc/profile.d/conda.sh

echo "### Write env file"
sed "s|<WORKING_DIR>|$PWD|g" env/.env.default.template > env/.env.default

if ! conda info --envs | grep ^blast >/dev/null; then
    echo "### Create conda environment"
    set -x
    conda create -y -n blast python=3.11.10
    set +x
fi

echo "### Conda activate"
conda activate blast

echo "### Install conda packages"
conda install -y -c conda-forge pkgconfig scikit-learn=1.2.2 opencv=4.10.0

echo "### Install requirements.txt"
pip install -r app/requirements.txt
mkdir -p tmp
TMPDIR=tmp pip install -r app/requirements.large.txt
rm -rf tmp

echo "### Init database (will also run tests)"
cd app
TEST_MODE=1 env $(cat ../env/.env.default) bash entrypoints/docker-entrypoint.app.sh

echo "### Download dustmaps"
python -c "from dustmaps.config import config; config.reset(); config['data_dir'] = 'data/dustmaps'; import dustmaps.sfd; dustmaps.sfd.fetch()"

