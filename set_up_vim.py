# -*- coding: utf-8 -*-

"""This script sets up the
Vim related files, using the
`myvim_files` repo.

Brew is needed to use this script.
"""

__author__ = 'Konstantinos Drossos'
__docformat__ = 'reStructuredText'

from pathlib import Path
from subprocess import run, PIPE


def arrange_files() -> None:
    run(f'ln -s vimrc {Path().home().joinpath(".vimrc")}', shell=True)


def install_fonts() -> None:
    # Get all available fonts from homebrew
    brew_fonts = run(
        'brew search "/font-/"',
        shell=True,
        stdout=PIPE
    ).stdout.splitlines()

    # Keep on the Nerd Fonts
    brew_fonts = [
        font.decode('utf-8') for font in brew_fonts
        if 'nerd-font' in font.decode('utf-8')
    ]

    for font_name in brew_fonts:
        run(f'brew install {font_name}', shell=True)


def download_plug() -> None:
    run(
        'curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
        , shell=True)


def install_plugins() -> None:
    pass


def main():
    install_fonts()


if __name__ == '__main__':
    main()


# EOF
