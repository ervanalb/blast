#!/bin/bash

set -euo pipefail

# Example usage:
# BLAST_TRANSIENT_NAME=2020aqz BLAST_TRANSIENT_RA=133.119904782 BLAST_TRANSIENT_DEC=-6.71221171596 ./run_single_transient

# I had to hack the on the python file app/host/slurm/run_single_transient.py
# which governs the actual execution, that's probably where to make changes.

. miniconda3/etc/profile.d/conda.sh

conda activate blast

cd app

env $(cat ../env/.env.default) python manage.py runcrons host.slurm.run_single_transient.run_single --force
