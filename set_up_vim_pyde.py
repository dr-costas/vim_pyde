# -*- coding: utf-8 -*-

"""This script sets up the
Vim related files, using the
`myvim_files` repo.

Brew is needed to use this script.
"""

__author__: str = "Konstantinos Drossos"
__docformat__: str = "reStructuredText"

from argparse import ArgumentParser, Namespace
from fileinput import FileInput
from functools import partial
import logging
from pathlib import Path
from shutil import copy, move
from string import Template
from subprocess import DEVNULL, PIPE, run


DATE_FORMAT = "%d-%b-%y %H:%M:%S"
FORMAT = "[Vim-PyDE | %(asctime)s | %(procesname)s | %(levelname)s]: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, datefmt=DATE_FORMAT)


def arrange_files() -> None:
    """Makes the .vimrc file"""
    # Create partial message logging function
    msg_log: partial[None] = partial(
        message_logging,
        process="arrange_files",
        indent="  ",
    )

    # Get the path of the vim_pyde directory
    path_parent: Path = Path(__file__).parent.resolve()

    # Create source and destination files
    file_src: Path = path_parent.joinpath("vimrc")
    file_dst: Path = Path.home().joinpath(".vimrc")

    # Check if the destination file exists
    if file_dst.exists():
        suffix: str = ""
        file_dst_bak: Path = file_dst

        # While it exists, add .bak as suffix
        while file_dst_bak.exists():
            suffix: str = f"{suffix}.bak"
            file_dst: Path = file_dst_bak.with_suffix(suffix)

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
    msg_log: partial[None] = partial(
        message_logging, process="download_plug", indent="  "
    )
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
    path_parent: Path = Path(__file__).parent.resolve()

    # Get the path of the ~/.vimrc file
    file_vimrc: Path = Path.home().joinpath(".vimrc")

    # Fix in-place the paths in the ~/.vimrc
    with FileInput(file_vimrc, inplace=True) as f:
        for line in f:
            if line.startswith("source"):
                line_parts: list[str] = line.split(" ")
                path_old: Path = Path(line_parts[1])
                path_new: Path = path_parent.joinpath(
                    path_old.parents[0].name,
                    path_old.name,
                )
                line: str = f"{line_parts[0]} {path_new}"
            print(line, end="")


def get_argument_parser() -> ArgumentParser:
    """Creates and returns an argument parse.

    :return: Argument parser to use.
    :rtype: argparse.ArgumentParser
    """
    arg_parser: ArgumentParser = ArgumentParser()

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
        [
            ["--install-nodejs"],
            {
                "action": "store_true",
                "help": "Install Node JS",
            },
        ],
        [
            ["--install-universal-ctags"],
            {
                "action": "store_true",
                "help": "Install universal CTags",
            },
        ],
        [
            ["--install-everything"],
            {
                "action": "store_true",
                "help": "Install everything, no-matter other choices",
            },
        ],
    ]

    for arg in args:
        arg_parser.add_argument(*arg[0], **arg[1])

    return arg_parser


def install_fonts() -> None:
    """Installs the NerdFonts from Homebrew"""
    msg_log: partial[None] = partial(
        message_logging,
        process="install_fonts",
        indent="  ",
    )

    msg_log_inner: partial[None] = partial(
        message_logging,
        process="install_fonts",
        indent="    ",
    )

    msg_log("Getting available NERDFonts from Homebrew")

    # Get all available fonts from Homebrew
    brew_fonts_bts: list[bytes] = run(
        'brew search "/font-/"',
        shell=True,
        stdout=PIPE,
    ).stdout.splitlines()

    # Keep the Nerd Fonts
    brew_fonts: list[str] = [
        font.decode("utf-8")
        for font in brew_fonts_bts
        if "nerd-font" in font.decode("utf-8")
    ]

    # Find already installed fonts
    installed_fonts_bts: list[bytes] = run(
        "brew list --cask",
        shell=True,
        stdout=PIPE,
    ).stdout.splitlines()

    installed_fonts: list[str] = [
        font.decode("utf-8")
        for font in installed_fonts_bts
        if "nerd-font" in font.decode("utf-8")
    ]

    brew_fonts: list[str] = [font for font in brew_fonts if font not in installed_fonts]

    if len(brew_fonts) == 0:
        msg_log("No available NerdFonts found. Stopping")
        msg_log(
            "If you want to install NerdFonts, try running "
            'the command: "brew tap homebrew/cask-fonts"'
        )
    else:
        fonts_total: int = len(brew_fonts)
        msg_log(f"Got {fonts_total} available fonts")

        for i_font, font_name in enumerate(brew_fonts, start=1):
            msg_log_inner(f"Now installing {font_name} ({i_font}/{fonts_total})")

            run(
                f"brew install {font_name}",
                shell=True,
                stdout=DEVNULL,
                stderr=DEVNULL,
            )

            msg_log_inner(f"{font_name} installed ({i_font}/{fonts_total})")


def install_nodejs() -> None:
    """Installs Node JS from Homebrew"""
    msg_log: partial[None] = partial(
        message_logging,
        process="install_nodejs",
        indent="  ",
    )

    existing_node: str = run(
        [
            "which",
            "node",
        ],
        shell=True,
        stdout=PIPE,
    ).stdout.decode(
        encoding="utf-8",
        errors="strict",
    )

    if existing_node.endswith("node"):
        msg_log(
            "There is existing Node JS installation. "
            "Continuing with existing installation."
        )
    else:
        run(
            ["brew", "install" "node"],
            shell=True,
            stdout=DEVNULL,
        )
        msg_log("Node JS installed")


def install_plugins() -> None:
    """Installs Vim plugins."""
    msg_log: partial[None] = partial(
        message_logging,
        process="install_plugins",
        indent="  ",
    )

    msg_log("Installing Vim plugins")
    run(
        "vim +'PlugInstall' +qa",
        shell=True,
        stdout=DEVNULL,
        stderr=DEVNULL,
    )
    msg_log("Plugins installed")


def install_universal_ctags() -> None:
    """Instals the Universal CTags with Homebrew"""
    msg_log: partial[None] = partial(
        message_logging,
        process="install_universal_ctags",
        indent="  ",
    )

    msg_log("Checking for existing Universal CTags")

    cmd_output: str = (
        run(
            "which ctags",
            shell=True,
            stdout=PIPE,
        )
        .stdout.decode("utf-8")
        .strip()
    )

    if cmd_output.endswith("ctags"):
        msg_log("Found existing CTags")
    else:
        msg_log("Not found CTags, installing Universal CTags from Homebrew")
        run(
            "brew install universal-ctags",
            shell=True,
            stdout=DEVNULL,
        )
        msg_log("Universal CTags installed")


def install_silver_searcher() -> None:
    """Instals the universal searcher with Homebrew"""
    msg_log: partial[None] = partial(
        message_logging,
        process="install_silver_searcher",
        indent="  ",
    )

    msg_log("Checking for existing silver searcher")

    cmd_output: str = (
        run(
            "which ag",
            shell=True,
            stdout=PIPE,
        )
        .stdout.decode("utf-8")
        .strip()
    )

    if cmd_output.endswith("ag"):
        msg_log("Found existing silver searcher")
    else:
        msg_log("Not found silver searcher, installing silver searcher from Homebrew")
        run(
            "brew install silver-searcher",
            shell=True,
            stdout=DEVNULL,
        )
        msg_log("Silver seacher installed")


def install_vim() -> None:
    """Installs Vim from Homebrew"""
    msg_log: partial[None] = partial(
        message_logging,
        process="install_vim",
        indent="  ",
    )

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


def main() -> None:
    arg_parser: ArgumentParser = get_argument_parser()
    args: Namespace = arg_parser.parse_args()

    msg_log: partial[None] = partial(
        message_logging,
        process="main",
        indent="",
    )

    msg_start = Template("Installing $process_name process starting")
    msg_end = Template("$process_name installation process ended")

    print("\n")
    print("=" * 100)
    msg_log("Set-up script starting")
    print("-" * 100, end="\n\n")

    if args.install_fonts or args.install_everything:
        process_name = "NerdFonts from Homebrew"
        msg_log(msg_start.substitute(process_name=process_name))
        install_fonts()
        msg_log(msg_end.substitute(process_name=process_name))

    if args.install_nodejs or args.install_everything:
        process_name = "Node JS from Hombrew"
        msg_log(msg_start.substitute(process_name=process_name))
        install_nodejs()
        msg_log(msg_end.substitute(process_name=process_name))

    if args.install_vim or args.install_everything:
        process_name = "Vim from Hombrew"
        msg_log(msg_start.substitute(process_name=process_name))
        install_vim()
        msg_log(msg_end.substitute(process_name=process_name))

    msg_log("Making symbolik link of `vimrc` file process starting")
    arrange_files()
    msg_log("Symbolik link creation process ended")

    if args.install_plug or args.install_everything:
        process_name = "Plug from GitHub"
        msg_log(msg_start.substitute(process_name=process_name))
        download_plug()
        msg_log(msg_end.substitute(process_name=process_name))

    if args.install_plugins or args.install_everything:
        process_name = "Vim plugins using Plug"
        msg_log(msg_start.substitute(process_name=process_name))
        install_plugins()
        msg_log(msg_end.substitute(process_name=process_name))

    if args.install_universal_ctags or args.install_everything:
        process_name = "Universal CTags"
        msg_log(msg_start.substitute(process_name=process_name))
        install_plugins()
        msg_log(msg_end.substitute(process_name=process_name))

    if args.install_silver_searcher or args.install_everything:
        process_name = "Silver searchers"
        msg_log(msg_start.substitute(process_name=process_name))
        install_plugins()
        msg_log(msg_end.substitute(process_name=process_name))

    print("")
    print("-" * 100)
    msg_log("Set-up script ended")
    print("=" * 100)
    print("\n")


if __name__ == "__main__":
    print_ascii_art()
    main()


# EOF
