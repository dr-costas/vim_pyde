# Vim and Vim plugin settings 

This is a git repository, containing a working set-up of Vim-related files,
containing the `.vimrc` file, settings for the plugins used in `.vimrc`, 
spelling files, and template files. 

In this README file is described the set-up process of the current files
and the content of the files. 

## Table of contents
1. [Setting up Vim with the files in this repo](#setting-up-this-repo)
    1. Setting up Vim
    2. Setting up plugin manager
    3. Using this repo
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
then you can check [this blog post](#https://kdrossos.net/blog/12/) on how to install
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


