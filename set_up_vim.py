# -*- coding: utf-8 -*-

"""This script sets up the
Vim related files, using the
`myvim_files` repo.

Brew is needed to use this script.
"""

__author__ = "Konstantinos Drossos"
__docformat__ = "reStructuredText"

from argparse import ArgumentParser
from pathlib import Path
from subprocess import PIPE, run


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
    target_file_path = Path().home().joinpath(".vimrc")
    source_file_path = Path().home().joinpath(".myvim_files", "vimrc")
    if not target_file_path.is_symlink():
        run(f"ln -s {source_file_path} {target_file_path}", shell=True)


def install_fonts() -> None:
    # Get all available fonts from homebrew
    brew_fonts = run(
        'brew search "/font-/"', shell=True, stdout=PIPE
    ).stdout.splitlines()

    # Keep on the Nerd Fonts
    brew_fonts = [
        font.decode("utf-8")
        for font in brew_fonts
        if "nerd-font" in font.decode("utf-8")
    ]

    for font_name in brew_fonts:
        run(f"brew install {font_name}", shell=True)


def install_vim() -> None:
    run("brew install vim", shell=True)


def download_plug() -> None:
    run(
        "curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
        shell=True,
    )


def install_plugins() -> None:
    run("vim +'PlugInstall' +qa", shell=True)


def main():
    arg_parser = get_argument_parser()
    args = arg_parser.parse_args()

    if args.install_fonts:
        install_fonts()
    if args.install_vim:
        install_vim()

    arrange_files()

    if args.install_plug:
        download_plug()

    if args.install_plugins:
        install_plugins()


if __name__ == "__main__":
    main()


# EOF
