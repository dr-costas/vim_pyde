# Vim Python Development Environment - Vim PyDE

     _    ___              ____        ____  ______
    | |  / (_)___ ___     / __ \__  __/ __ \/ ____/
    | | / / / __ `__ \   / /_/ / / / / / / / __/
    | |/ / / / / / / /  / ____/ /_/ / /_/ / /___
    |___/_/_/ /_/ /_/  /_/    \__, /_____/_____/
                             /____/


Welcome to the GitHub repository of the Vim PyDE!

Here you can find instruction on how to set up the Vim PyDE
and how to use it. Please not that Vim PyDE is just a collection
of Vim plugins, set-up together to work without problems and for
convenient Python development.

At the moment, Vim PyDE is only for macOS.

----

## Table of contents

1. [Introduction](#introduction)
2. [How to set-up Vim PyDE](#how-to-set-up-vim-pyde)
3. [Plugins used]
4. [Common development cases]
5. [Debugging]
6. [Git integration]
7. [Terminal and REPL integration]
8. [Virtual environments]
9. [Other functionalities]

----

## Introduction

Through the years, I have gathered some Vim plugins that can
allow a nice experience to work with Vim and Python. I have set-up
these plugins to work without conflicts, and bundled them altogether
in a easily re-usable code. 

Vim PyDE offers all, if not more, of the functionality that one can
find in standard Python IDEs, like PyCharm or VSCode. This is mostly
due to the work of the developers of the plugins and, of course, due
to the powerful Vim.

Please note that this repository is offered without any warranty and
it should be used by your own responsibility. All plugins maintain their
licences, since this code is just a Vim set-up that uses plugins.

Finally, to use Vim PyDE it is required some familiarity with Vim.
For example, one should already know how to quit Vim or how to navigate
around. Most of the extra functionality is covered by the used plugins
and the remaining is explained here.

## How to set-up Vim PyDE

To set-up Vim PyDE you have to use [Homebrew](https://brew.sh) and
[Plug](https://github.com/junegunn/vim-plug).  [Homebrew](https://brew.sh)
is a package manager for macOS and [Plug](https://github.com/junegunn/vim-plug)
is a plugin manager for Vim.

Then, to set-up Vim PyDE you have to:

1. Clone this repository somewhere on your computer by using:

   ```bash
   git clone https://github.com/dr-costas/myvim_files
   ```

   This will create the directory `myvim_files` which will call now `ROOT` directory.

2. Execute the set-up script `set_up_vim.py` from within the `ROOT` directory and
  using the following flags:

   * `--install-vim` to install [Vim](https://github.com/vim/vim) using [Homebrew](https://brew.sh).
   * `--install-plug` to install [Plug](https://github.com/junegunn/vim-plug).
   * `--install-fonts` to install [NERDFonts](https://github.com/ryanoasis/nerd-fonts) for [Vim](https://github.com/vim/vim)
   * `--install-plugins` to install the plugins for Vim PyDE

   For example, to use all the above flags, you can do from inside `ROOT` directory:

   ```bash
   python set_up_vim.py --install-vim --install-plug --install-fonts --install-plugins
   ```

   All the above should be installed. The only reason for not installing them is
   if you already have them installed. For example, you might already have some NERDFonts
   installed and you do not need new all you already have installed Vim from [Homebrew](https://brew.sh).

And your are ready!
