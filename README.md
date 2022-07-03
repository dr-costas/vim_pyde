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
4. [Working with files](#working-with-files)
5. [Debugging](#debugging)
6. [Git integration](#git-integration)
7. [Virtual environments](#virtual-environments)
8. [Terminal and REPL](#terminal-and-repl)
9. [View and change settings](#view-and-change-settings)
10. [Spelling](#spelling)

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

 * [Vimspector](https://github.com/puremourning/vimspector): Vimspector is a Vim debugger
 with full functionalities.

* [Vim-Startify](https://github.com/mhinz/vim-startify): Vim-Startify is a plugin that
adds a nice and fancy start screen.

* [Vim-Surround](https://github.com/tpope/vim-surround): Vim -Surround provides fast
ways to alter and add surroundings, e.g. brackets.

----

## Working with files

To explore, open, move, and delete, you can use the provided functionality from NERDTree.
Typical movements and operations are described in the
[NERDTRee's GitHub](https://github.com/preservim/nerdtree) or help file.

To add a new file, you either use NERDTree or the Vim-Templates plugin. Currently,
templates exist for Python files (`.py`), YAML files (`.yaml`), Vimspector
settings (`.vimspector.json`), and Vim specific files. A full list of the
templates can be see at the `ROOT/templates` directory.

For example, to start a new file in the current buffer you can do:


```vim
:e my_python_file.py
```

and the new file `my_python_file.py` will open, having the pre-specified structure
from the Python file template. If you want to edit the template, you can consult
the [Vim-Templates](https://github.com/tibabit/vim-templates) plugin documentation.

----

## Debugging

Debugging is happening by the [Vimspector](https://github.com/puremourning/vimspector)
plugin. Vimspector needs a settings file in the project's root folder or somewhere
visible for Vimspector (check at the Vimspector's documentation for other than project's
root folder locations).

To generate a Vimspector settings file, you can use the Vim-Templates and the provided
template for Vimspector JSON file. Just do `vsp .vimspector.json` and the template
will be created in the Vim's current working directory. 

Vimspector has some available mappings for its operations. You can see those mappings
at the [Vimspector's GitHub](https://github.com/puremourning/vimspector). Additionally,
Vim PyDE has the following added mappings:

| Mapping       | Function                       |
| :---          | :----                          |
| `<leader>F3`  | Completely close Vimspector    |
| `<leader>F4`  | Fresh start of Vimspector      |
| `<leader>dF9` | Delete all breakpoints         |

----

## Git integration

Git is integrated in Vim PyDE through [Vim-Fugitive](https://github.com/tpope/vim-fugitive)
plugin. This plugin offers typical commit/push/pull functions (and many more) through the
`:Git ` command. For example, a git commit would be: 

```vim
:Git commit % -m "A commit"
```

where `%` means the file at the current active buffer. 

----

## Virtual environments

Virtual environments are handled through the `coc-pyright` add on of the `CoC` plugin.
Basically, this means that you do not have to do anything, just log into your virtual
environment before open Vim and `coc-pyright` will take care everything else.

----

## Terminal and REPL

There are two ways to open and work in a terminal from Vim PyDE. The first is using the
built in functionality from Vim and the second is by using the
[Vim-REPL](https://github.com/sillybun/vim-repl) plugin. Vim-PyDE offers mappings for both.

For the first case, you can use the mapping `<leader>(C-T)` (leader key plus Ctrl+T) and
the terminal will open at the `belowright` position of the current buffer. Plus the
environmental variable `PYTHONPATH` will be set as `PYTHONPATH=$PYTHONPATH:.`.

For the second case, you can use the mapping `<leader>zb` and the terminal will open below
everything, without setting up the `PYTHONPATH`.

To open the Python `REPL`, you can use the mapping `<leader>zp`. Additionally, you can
check at the [Vim-REPL](https://github.com/sillybun/vim-repl) documentation what other
functionalities you can have. For example, Vim-REPL plugin allows to send code from a
Python file directly to the REPL console for execution.

----

## View and change settings

Settings of Vim PyDE are divided in two categories. First are the settings that
are for Vim and then are the settings that affect the plugins. Vim settings are
in the `ROOT/vim_settings/` files.

All settings of Vim PyDE are either available from the used plugins or from the
files in the `ROOT/plugins_settings` directory.

From the above two directories, you can see all settings and also modify them to
you taste.

----

## Spelling

Spelling and thesaurus are provided by Vim. For more info you can check the
Vim's spelling documentation.
