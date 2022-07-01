# -*- coding: utf-8 -*-

"""This script sets up the
Vim related files, using the
`myvim_files` repo.

Brew is needed to use this script.
"""

__author__ = "Konstantinos Drossos"
__docformat__ = "reStructuredText"

from argparse import ArgumentParser
from functools import partial
import logging
from pathlib import Path
from subprocess import DEVNULL, PIPE, run


DATE_FORMAT = "%d-%b-%y %H:%M:%S"
FORMAT = "[Vim-PyDE | %(asctime)s | %(procesname)s | %(levelname)s]: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt=DATE_FORMAT)


def message_logging(msg: str, process: str, indent: str = "") -> None:
    logging.info(msg=f"{indent}- {msg}", extra={"procesname": process})


def get_argument_parser() -> ArgumentParser:
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


def arrange_files() -> None:
    msg_log = partial(message_logging, process="arrange_files", indent="  -")
    home_dir = Path().home()

    target_file_path = home_dir.joinpath(".vimrc")
    source_file_path = home_dir.joinpath(".myvim_files", "vimrc")

    if not target_file_path.is_symlink():
        msg_log(f"Making symbolik link of {source_file_path} to {target_file_path}")
        run(f"ln -s {source_file_path} {target_file_path}", shell=True, stdout=DEVNULL)
        msg_log("Link created")
    else:
        msg_log(f"File {target_file_path} already exists, will not override")
        msg_log(
            "If you want to use the `.vimrc` file created by this script, "
            "please rename/remove the existing one"
        )


def install_fonts() -> None:
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

    if len(brew_fonts) == 0:
        msg_log("No available NerdFonts found. Stopping")
        msg_log(
            "If you want to install NerdFonts, try running "
            'the command: "brew tap homebrew/cask-fonts"'
        )
    else:
        msg_log(f"Got {len(brew_fonts)} available fonts")
        for font_name in brew_fonts:
            msg_log_inner(f"Now installing {font_name}")
            run(f"brew install {font_name}", shell=True, stdout=DEVNULL, stderr=DEVNULL)
            msg_log_inner(f"{font_name} installed")


def install_vim() -> None:
    run("brew install vim", shell=True, stdout=DEVNULL)


def download_plug() -> None:
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


def install_plugins() -> None:
    run("vim +'PlugInstall' +qa", shell=True, stdout=DEVNULL, stderr=DEVNULL)


def main():
    arg_parser = get_argument_parser()
    args = arg_parser.parse_args()

    msg_log = partial(message_logging, process="main", indent="")

    if args.install_fonts:
        msg_log("Installing fonts from Homebrew")
        install_fonts()
        msg_log("Fonts installed")
    if args.install_vim:
        msg_log("Installing Vim from Homebrew")
        install_vim()
        msg_log("Vim installed")

    msg_log("Making symbolik link of `vimrc` file")
    arrange_files()
    msg_log("Symbolik link created")

    if args.install_plug:
        msg_log("Downloading Plug")
        download_plug()
        msg_log("Plug downloaded")

    if args.install_plugins:
        msg_log("Installing Vim plugins")
        install_plugins()
        msg_log("Plugins installed")


if __name__ == "__main__":
    main()


# EOF
