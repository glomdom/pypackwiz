import click
import os
import shutil

from .utils import logger as logger
from .utils.packwiz import Packwiz
from .utils import colors
from .utils import minecraft

@click.group(help="A python wrapper for packwiz.")
def cli():
    pass

@cli.command(help="Initializes a packwiz project.")
@click.argument("directory", type=click.Path(file_okay=False, dir_okay=True, writable=True))
@click.option("--no-git", default=False, is_flag=True, help="Will not create a git repository in the pack directory.")
def init(directory, no_git):
    pwiz = Packwiz(directory)

    logger.status(logger.info, pwiz.create_directory_structure, "creating directory structure..")
    logger.status(logger.info, pwiz.download_packwiz, "downloading packwiz..")
    pwiz.create_git_repository()

    # Gather pack information. (pack_name, author, pack_version, mc_version, modloader, modloader_version)
    pack_name = logger.prompt("pack name", pwiz.pack_name_from_dir())
    pack_author = logger.prompt("pack author")
    pack_version = logger.prompt("pack version", "1.0.0")

    versions = minecraft.get_versions()
    mc_version = logger.prompt("minecraft version", versions[0])
    if mc_version not in versions:
        logger.error("invalid minecraft version")

    modloader = logger.prompt("modloader")

    print(pack_name, pack_author, pack_version, mc_version)

if __name__ == '__main__':
    cli()