"""
Bolt ⚡️ is a CLI-tool for making your FastAPI projects faster.
"""

import os
import sys
from typer import Typer
from cli.utils.common import print_info, print_success, print_error
from cli.utils.file import file_creator


app = Typer()


@app.command()
def start_app(app_name: str):
    """
    Create a new FastAPI app.

    Steps:
        - Create new directory with the app name
        - Create new directories: tests and utils
        - Create new files: api.py, models.py and dto.py
    """
    print_info(f"Creating app {app_name}...")

    app_dir = os.path.join(f"{app_name}")

    if not os.path.exists(app_dir):
        os.mkdir(app_dir)
        os.mkdir(os.path.join(app_dir, "tests"))
        os.mkdir(os.path.join(app_dir, "utils"))
        
        # create an empty init file in the app directory
        with open(os.path.join(app_dir, "__init__.py"), "w") as f:
            pass

        file_creator(app_dir, app_name, "api.py")
        file_creator(app_dir, app_name, "models.py")
        file_creator(app_dir, app_name, "dto.py")

        print_success(f"App {app_name} created successfully!")
    else:
        print_error("App already exists...")
        sys.exit()


@app.command()
def delete_app(name: str):
    """
    Delete a FastAPI app after confirmation.
    """    
    app_dir = os.path.join(f"{name}")

    if os.path.exists(app_dir):
        user_confirmation = input("Are you sure you want to delete this app? (y/n): ")
        
        if user_confirmation.lower() == "y":
            print_info(f"Deleting app {name}...")
            os.system(f"rm -rf {app_dir}")
            print_success(f"App {name} deleted successfully!")
    else:
        print_error("App does not exist...")
        sys.exit()


@app.command()
def make_migrations(msg: str):
    """
    Create a new migration using alembic.
    """

    print_info("Creating migration...")

    os.system(f"alembic revision --autogenerate -m '{msg}'")

    print_success("Migration created successfully...")


@app.command()
def migrate():
    """
    Run migrations using alembic.
    """

    print_info("Running migrations...")

    os.system("alembic upgrade head")

    print_success("Migrations ran successfully...")


if __name__ == "__main__":
    app()
