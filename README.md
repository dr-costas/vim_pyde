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
2. [How to set-up]
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



# Vim and Vim plugin settings 

This is a git repository, containing a working set-up of Vim-related files,
containing the `.vimrc` file, settings for the plugins used in `.vimrc`, 
spelling files, and template files. 

In this README file is described the set-up process of the current files
and the content of the files. 

## Table of contents
1. [Setting up Vim with the files in this repo](#setting-up-this-repo)
    1. [Setting up Vim](#set-up-your-vim)
    2. [Setting up plugin manager](#set-up-the-plugin-manager)
    3. [Using this repo](#set-up-the-files-in-this-repo)
2. Contents of this repo
    1. `vimrc` file
    2. Settings files
    3. Spelling files
    4. Template files

## Setting up this repo

To set up this repo, you have to

1. Clone it to your computer
2. Set-up your Vim
3. Set-up the plugin manager of your Vim
4. Set-up the files in this repo

The following subsections describe steps 2 to 4. 

### Set-up your Vim

To use this repo, first you have to make sure that you have Vim installed. Then,
you have to check the version of your Vim, by using in terminal

```bash
$ vim --version
```

This repo is tested with Vim version >= 8.2. If you have not at least Vim version 8.0,
then you can check [this blog post](https://kdrossos.net/blog/12/) on how to install
it for macOS. For Linux, the process should be similar. 

### Set-up the plugin manager

This repo is based on the Plug plugin manager for Vim. To install Plug, you have to clone
it in your `$HOME` directory, by using:

```bash
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

For more information, you can check [the GitHub repository of Plug](https://github.com/junegunn/vim-plug).

### Set-up the files in this repo

First, navigate to you home directory

```bash
$ cd ~
```

Then, clone this repository, by using

```bash
$ git clone git@github.com:dr-costas/myvim_files.git ~/.myvim_files
```

**Check if you already have a `.vimrc` file**. If you do, then keep a backup
by doing

```bash
$ mv ~/.vimrc ~/.vimrc_bak
```

Then, make a symbolik link of the `vimrc` file in the `myvim_file` directory, 
to your home directory, by doing

```bash
$ ln ~/.myvim_files/vimrc ~/.vimrc
```

Open vim and install the plugins by using the `PlugInstall`. 

Finally, using your terminal, go to `~/.vim/plugged/vimspector/` and do

```bash
$ ./install_gadget.py --all --disable-tcl
```

So that the `vimspector` plugin will install the necessary gadgets for debugging. 

That's it! 

