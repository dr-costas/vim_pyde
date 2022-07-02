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
3. [Plugins used](#plugins-used)
4. [Vim settings used](vim-settings-used)
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

----

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
   installed and you do not need new all you already have installed
   [Vim](https://github.com/vim/vim) from [Homebrew](https://brew.sh).

And your are ready!

----

## Plugins used

Multiple plugins are used in order to make Vim PyDE happen. These will be listed here
in alphabetical order, together with links to their GitHub repository.

* [Auto-pairs](https://github.com/jiangmiao/auto-pairs): The auto-pairs plugin allows
to insert or delete brackets, quotes, etc., in pairs

* [Black](https://github.com/psf/black): Black is the "uncompromising" Python code formatter.

* [CoC](https://github.com/neoclide/coc.nvim): Conquest of Completion (CoC) is a
completion plugin and a platform with various add-ons.

* [CSV](https://github.com/chrisbra/csv.vim): CSV is a plugin for handling and nicely
formatting CSV files.

* [FzF](https://github.com/junegunn/fzf.vim): FzF is a plugin that provides a wrapper
function for the functionalities of the [Fuzzy Finder](https://github.com/junegunn/fzf).

* [Gruvbox](https://github.com/morhetz/gruvbox): Gruvbox is a retro color scheme for Vim,
and the color scheme currently used by Vim PyDE.

* [IndentLine](https://github.com/Yggdroot/indentLine): IndentiLine is a Vim plugin to
display line indentation.

* [LightLine](https://github.com/itchyny/lightline.vim): LightLine is a status and tabline
plugin.

* [LightLineBuffer](https://github.com/mengelbrecht/lightline-bufferline): LightLineBuffer
is a plugin to display open buffers in the LightLine.

* [NERDCommenter](https://github.com/preservim/nerdcommenter): NERDCommenter is a plugin
that offers flexible commenting functionalities.

* [NERDTree](https://github.com/preservim/nerdtree): NERDTree is a file explorer for Vim.

* [NERDTree Git](https://github.com/Xuyuanp/nerdtree-git-plugin): NERDtree Git is a plugin
to display git status of files in NERDTree.

* [Python syntax](https://github.com/vim-python/python-syntax): Python syntax is a Python
syntax highlighting plugin.

* [Tagbar](https://github.com/preservim/tagbar): Tabgbar is a plugin that displays project
structure/class outline.

* [Vim-Devicons](https://github.com/ryanoasis/vim-devicons): Vim-Devicons is a plugin that
adds icons to files at NERDTree.

* [Vim-Fugitive](https://github.com/tpope/vim-fugitive): Vim-Fugitive is a git wrapper for
Vim.

* [Vim-Gitgutter](https://github.com/airblade/vim-gitgutter): Vim-Gitgutter id a plugin
that shows git diff in the sign column.

* [Vim-Markdown](https://github.com/preservim/vim-markdown): Vim-Markdown is a plugin that
offers markdown syntax highlighting.

* [Vim-Pydocstring](https://github.com/heavenshell/vim-pydocstring): Vim-Pydocstring offers
generation of docstrings templates.

* [Vim-REPL](https://github.com/sillybun/vim-repl): Vim-REPL is a plugin that offers REPL
functionalities for Vim.

* [Vim-Templates](https://github.com/tibabit/vim-templates): Vim-Templates offers usage
of templates for file types.
