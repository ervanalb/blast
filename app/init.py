#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # The database migrations must be executed first to establish the db schema
    execute_from_command_line(["__main__.py", "makemigrations"])
    execute_from_command_line(["__main__.py", "migrate"])

    # Create the Django admin account if it does not exist
    with open("entrypoints/setup_superuser.py") as script:
        script_text = script.read()
    execute_from_command_line(["__main__.py", "shell", f"--command={script_text}"])

    # Collect the assets for the static file server
    execute_from_command_line(["__main__.py", "collectstatic", "--noinput"])

    # Create the periodic tasks if they are not already registered
    with open("entrypoints/setup_initial_periodic_tasks.py") as script:
        script_text = script.read()
    execute_from_command_line(["__main__.py", "shell", f"--command={script_text}"])

    # Load data from Django fixture files
    # TO DO: Properly handle duplicate entry errors for fixtures that have already been installed.
    try:
        print(
            """Loading fixture "/app/host/fixtures/initial/setup_survey_data.yaml"..."""
        )
        execute_from_command_line(
            [
                "__main__.py",
                "loaddata",
                "/app/host/fixtures/initial/setup_survey_data.yaml",
            ]
        )
    except Exception as err:
        print(str(err))

        print(
            """Ignoring loaddata error for "/app/host/fixtures/initial/setup_survey_data.yaml"."""
        )
        pass

    try:
        print(
            """Loading fixture "/app/host/fixtures/initial/setup_filter_data.yaml"..."""
        )
        execute_from_command_line(
            [
                "__main__.py",
                "loaddata",
                "/app/host/fixtures/initial/setup_filter_data.yaml",
            ]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/initial/setup_filter_data.yaml"."""
        )
        pass

    try:
        print(
            """Loading fixture "/app/host/fixtures/initial/setup_catalog_data.yaml"..."""
        )
        execute_from_command_line(
            [
                "__main__.py",
                "loaddata",
                "/app/host/fixtures/initial/setup_catalog_data.yaml",
            ]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/initial/setup_catalog_data.yaml"."""
        )
        pass

    try:
        print("""Loading fixture "/app/host/fixtures/initial/setup_tasks.yaml"...""")
        execute_from_command_line(
            ["__main__.py", "loaddata", "/app/host/fixtures/initial/setup_tasks.yaml"]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/initial/setup_tasks.yaml"."""
        )
        pass

    try:
        print("""Loading fixture "/app/host/fixtures/initial/setup_status.yaml"...""")
        execute_from_command_line(
            ["__main__.py", "loaddata", "/app/host/fixtures/initial/setup_status.yaml"]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/initial/setup_status.yaml"."""
        )
        pass

    try:
        print(
            """Loading fixture "/app/host/fixtures/initial/setup_acknowledgements.yaml"..."""
        )
        execute_from_command_line(
            [
                "__main__.py",
                "loaddata",
                "/app/host/fixtures/initial/setup_acknowledgements.yaml",
            ]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/initial/setup_acknowledgements.yaml"."""
        )
        pass

    try:
        print("""Loading fixture "/app/host/fixtures/example/2010ag.yaml"...""")
        execute_from_command_line(
            ["__main__.py", "loaddata", "/app/host/fixtures/example/2010ag.yaml"]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/example/2010ag.yaml"."""
        )
        pass

    try:
        print("""Loading fixture "/app/host/fixtures/example/2010ai.yaml"...""")
        execute_from_command_line(
            ["__main__.py", "loaddata", "/app/host/fixtures/example/2010ai.yaml"]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/example/2010ai.yaml"."""
        )
        pass

    try:
        print("""Loading fixture "/app/host/fixtures/example/2010H.yaml"...""")
        execute_from_command_line(
            ["__main__.py", "loaddata", "/app/host/fixtures/example/2010H.yaml"]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/example/2010H.yaml"."""
        )
        pass

    try:
        print("""Loading fixture "/app/host/fixtures/test/setup_test_transient.yaml"...""")
        execute_from_command_line(
            ["__main__.py", "loaddata", "/app/host/fixtures/test/setup_test_transient.yaml"]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/test/setup_test_transient.yaml"."""
        )
        pass

    try:
        print("""Loading fixture "/app/host/fixtures/test/setup_test_task_register.yaml"...""")
        execute_from_command_line(
            ["__main__.py", "loaddata", "/app/host/fixtures/test/setup_test_task_register.yaml"]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/test/setup_test_task_register.yaml"."""
        )
        pass

    try:
        print("""Loading fixture "/app/host/fixtures/example/snapshot.yaml"...""")
        execute_from_command_line(
            ["__main__.py", "loaddata", "/app/host/fixtures/example/snapshot.yaml"]
        )
    except Exception as err:
        print(str(err))
        print(
            """Ignoring loaddata error for "/app/host/fixtures/example/snapshot.yaml"."""
        )
        pass


if __name__ == "__main__":
    main()
