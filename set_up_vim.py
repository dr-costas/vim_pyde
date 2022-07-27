# -*- coding: utf-8 -*-

"""This script sets up the
Vim related files, using the
`myvim_files` repo.

Brew is needed to use this script.
"""

__author__ = "Konstantinos Drossos"
__docformat__ = "reStructuredText"

from argparse import ArgumentParser
from fileinput import FileInput
from functools import partial
import logging
from pathlib import Path
from shutil import copy, move
from subprocess import DEVNULL, PIPE, run


DATE_FORMAT = "%d-%b-%y %H:%M:%S"
FORMAT = "[Vim-PyDE | %(asctime)s | %(procesname)s | %(levelname)s]: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt=DATE_FORMAT)


def arrange_files() -> None:
    """Makes the .vimrc file"""
    # Create partial message logging function
    msg_log = partial(
        message_logging,
        process="arrange_files",
        indent="  ",
    )

    # Get the path of the vim_pyde directory
    path_parent = Path(__file__).parent.resolve()

    # Create source and destination files
    file_src = path_parent.joinpath("vimrc")
    file_dst = Path.home().joinpath(".vimrc")

    # Check if the destination file exists
    if file_dst.exists():
        suffix = ""
        file_dst_bak = file_dst

        # While it exists, add .bak as suffix
        while file_dst_bak.exists():
            suffix = f"{suffix}.bak"
            file_dst = file_dst_bak.with_suffix(suffix)

        # Move the existing .vimrc to vimrc.bak.bak..
        move(file_dst, file_dst_bak)

        # Inform about what happened
        msg_log("`.vimrc` exists, moved to: `{file_dst_bak}`")

    # Create the ~/.vimrc file
    copy(file_src, file_dst)

    # Fix the paths in the ~/.vimrc
    fix_vimrc()


def download_plug() -> None:
    """Downloads Plug"""
    msg_log = partial(message_logging, process="download_plug", indent="  ")
    msg_log(
        "Downloading Plug from GitHub: https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"
    )
    run(
        "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
        shell=True,
        stdout=DEVNULL,
        stderr=DEVNULL,
    )
    msg_log("Plug downloaded")


def fix_vimrc() -> None:
    """Fixes the vimrc for sourcing the settings."""

    # Get the path of the vim_pyde directory
    path_parent = Path(__file__).parent.resolve()

    # Get the path of the ~/.vimrc file
    file_vimrc = Path.home().joinpath(".vimrc")

    # Fix in-place the paths in the ~/.vimrc
    with FileInput(file_vimrc, inplace=True) as f:
        for line in f:
            if line.startswith("source"):
                line_parts = line.split(" ")
                path_old = Path(line_parts[1])
                path_new = path_parent.joinpath(
                    path_old.parents[0].name,
                    path_old.name,
                )
                line = f"{line_parts[0]} {path_new}"
            print(line, end="")


def get_argument_parser() -> ArgumentParser:
    """Creates and returns an argument parse.

    :return: Argument parser to use.
    :rtype: argparse.ArgumentParser
    """
    arg_parser = ArgumentParser()

    args = [
        [
            ["--install-fonts"],
            {
                "action": "store_true",
                "help": "Install available NerdFonts from Homebrew",
            },
        ],
        [
            ["--install-vim"],
            {
                "action": "store_true",
                "help": "Install Vim from Homebrew",
            },
        ],
        [
            ["--install-plug"],
            {
                "action": "store_true",
                "help": "Install Vim Plug",
            },
        ],
        [
            ["--install-plugins"],
            {
                "action": "store_true",
                "help": "Install Vim plugins",
            },
        ],
    ]

    for arg in args:
        arg_parser.add_argument(*arg[0], **arg[1])

    return arg_parser


def install_fonts() -> None:
    """Installs the NerdFonts from Homebrew"""
    msg_log = partial(message_logging, process="install_fonts", indent="  ")
    msg_log_inner = partial(message_logging, process="install_fonts", indent="    ")

    msg_log("Getting available NERDFonts from Homebrew")
    # Get all available fonts from Homebrew
    brew_fonts = run(
        'brew search "/font-/"', shell=True, stdout=PIPE
    ).stdout.splitlines()

    # Keep on the Nerd Fonts
    brew_fonts = [
        font.decode("utf-8")
        for font in brew_fonts
        if "nerd-font" in font.decode("utf-8")
    ]

    # Find already installed fonts
    installed_fonts = run(
        "brew list --cask", shell=True, stdout=PIPE
    ).stdout.splitlines()

    installed_fonts = [
        font.decode("utf-8")
        for font in installed_fonts
        if "nerd-font" in font.decode("utf-8")
    ]

    brew_fonts = [font for font in brew_fonts if font not in installed_fonts]

    if len(brew_fonts) == 0:
        msg_log("No available NerdFonts found. Stopping")
        msg_log(
            "If you want to install NerdFonts, try running "
            'the command: "brew tap homebrew/cask-fonts"'
        )
    else:
        fonts_total = len(brew_fonts)
        msg_log(f"Got {fonts_total} available fonts")
        for i_font, font_name in enumerate(brew_fonts, start=1):
            msg_log_inner(f"Now installing {font_name} ({i_font}/{fonts_total})")
            run(f"brew install {font_name}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
            msg_log_inner(f"{font_name} installed ({i_font}/{fonts_total})")


def install_plugins() -> None:
    """Installs Vim plugins."""
    msg_log = partial(message_logging, process="install_plugins", indent="  ")
    msg_log("Installing Vim plugins")
    run("vim +'PlugInstall' +qa", shell=True, stdout=DEVNULL, stderr=DEVNULL)
    msg_log("Plugins installed")


def install_vim() -> None:
    """Installs Vim from Homebrew"""
    msg_log = partial(message_logging, process="install_vim", indent="  ")
    msg_log("Installing Vim from Homebrew")
    run("brew install vim", shell=True, stdout=DEVNULL)
    msg_log("Vim installed")


def message_logging(msg: str, process: str, indent: str = "") -> None:
    """Common message logging function.

    :param msg: Message to log.
    :type msg: str
    :param process: Name of the process that does the logging.
    :type process: str
    :param indent: Indentation to use.
    :type indent: str
    """
    logging.info(msg=f"{indent}- {msg}", extra={"procesname": process})


def print_ascii_art() -> None:
    """Prints an ASCII art of the Vim PyDE string.

    ASCII art was taken from: https://patorjk.com/software/taag
    using the Slant fonts.
    """
    print(
        "\n\n\n"
        "   _    ___              ____        ____  ______\n"
        "  | |  / (_)___ ___     / __ \\__  __/ __ \\/ ____/\n"
        "  | | / / / __ `__ \\   / /_/ / / / / / / / __/   \n"
        "  | |/ / / / / / / /  / ____/ /_/ / /_/ / /___   \n"
        "  |___/_/_/ /_/ /_/  /_/    \\__, /_____/_____/   \n"
        "                           /____/                \n"
        "\n"
    )


def main():
    arg_parser = get_argument_parser()
    args = arg_parser.parse_args()

    msg_log = partial(message_logging, process="main", indent="")

    print("\n")
    print("=" * 200)
    msg_log("Set-up script starting")
    print("-" * 200, end="\n\n")

    if args.install_fonts:
        msg_log("Installing fonts from Homebrew process starting")
        install_fonts()
        msg_log("Fonts installing process ended")
    if args.install_vim:
        msg_log("Installing Vim from Homebrew process starting")
        install_vim()
        msg_log("Vim installation process ended")

    msg_log("Making symbolik link of `vimrc` file process startin")
    arrange_files()
    msg_log("Symbolik link creation process ended")

    if args.install_plug:
        msg_log("Downloading Plug process starting")
        download_plug()
        msg_log("Plug downloading process ended")

    if args.install_plugins:
        msg_log("Installing Vim plugins process starting")
        install_plugins()
        msg_log("Plugins installation process ended")

    print("")
    print("-" * 100)
    msg_log("Set-up script ended")
    print("=" * 100)
    print("\n")


if __name__ == "__main__":
    print_ascii_art()
    main()


# EOF
