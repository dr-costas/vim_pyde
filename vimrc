" ~/.vimrc file starts
"
" ==================================
" VIM settings file
" ==================================
"
" Directives that go on top and are not tracked by git
" The file: myvim_files/other_files/directives_that_go_on_top.vimsettings
" has to be manually created.
source ~/.myvim_files/other_files/directives_that_go_on_top.vimsettings
"
" Necessary directives
set nocompatible              			" be iMproved, required
filetype plugin indent on    			" required
"
" Make Vimspector mapping to HUMAN before loading it
let g:vimspector_enable_mappings = 'HUMAN'
" ----------------------Plugin settings----------------------------------
"
" Start Plug
call plug#begin('~/.vim/plugged')
" 	Currently using plugins ---------------------------------------------
Plug 'scrooloose/nerdtree'               		" File browser in VIM
Plug 'Xuyuanp/nerdtree-git-plugin'        		" Plugin for NERDTRee and Git
Plug 'neoclide/coc.nvim', {'branch': 'release'} " Coc plugin
Plug 'puremourning/vimspector' 		  			" Debugging plugin
Plug 'tpope/vim-fugitive'                 		" GIT integration
Plug 'tpope/vim-markdown' 		  				" Markdown fancy stuff
Plug 'Yggdroot/indentLine' 						" Vertical bars for indentation
Plug 'airblade/vim-gitgutter' 					" Git indication at sign column
Plug 'tibabit/vim-templates' 					" Template files
Plug 'altercation/vim-colors-solarized' 		" Solarized colorscheme
Plug 'itchyny/lightline.vim'                    " Status line
Plug 'vim-python/python-syntax' 				" Python syntax highlight
Plug 'mhinz/vim-startify'						" Vim start screen
Plug 'jiangmiao/auto-pairs' 					" Brackets and more pair handling
Plug 'tpope/vim-surround' 						" Postfix surrounding
Plug 'taohexxx/lightline-buffer' 			    " Show open buffers in lightline
Plug 'heavenshell/vim-pydocstring', { 'do': 'make install' } " Docstrings
Plug 'sillybun/vim-repl'                        " REPL Python terminal for Vim
" 	Recently used but uninstalled ---------------------------------------
" Plug 'bling/vim-bufferline' 				      " Show open buffers list
" Plug 'NLKNguyen/papercolor-theme'               " Papercolor theme
" Plug 'mhinz/vim-signify' 						  " Indication of file changes
call plug#end()
"
" ----------------------General settings---------------------------------
"
" General settings file
source ~/.myvim_files/vim_settings/general_settings.vimsettings
"
" Appearance settings file
source ~/.myvim_files/vim_settings/appearance_settings.vimsettings
"
" ------------Mappings and plugins settings------------------------------
"
" Mappings
source ~/.myvim_files/plugins_settings/mappings.vimsettings
"
" NERDTree related
source ~/.myvim_files/plugins_settings/nerdtree.vimsettings
"
" COC related
source ~/.myvim_files/plugins_settings/coc.vimsettings
"
" Solarized related
source ~/.myvim_files/plugins_settings/solarized.vimsettings
" 
" Vimspector related
source ~/.myvim_files/plugins_settings/vimspector.vimsettings
"
" IndentLine related
source ~/.myvim_files/plugins_settings/indent_line.vimsettings
"
" Vim-templates related
source ~/.myvim_files/plugins_settings/vim_templates.vimsettings
"
" Lightline related
source ~/.myvim_files/plugins_settings/lightline.vimsettings
"
" Lightline buffer related
source ~/.myvim_files/plugins_settings/lightline_buffer.vimsettings
"
" Python doctsring related
source ~/.myvim_files/plugins_settings/python_docstring.vimsettings
"
" REPL related
source ~/.myvim_files/plugins_settings/repl.vimsettings
"
" ----------------------Appearance settings------------------------------
"
" Highlight comments
highlight Comment cterm=bold
" 
" Cursor line appearance
" highlight CursorLine cterm=NONE ctermbg=236 ctermfg=NONE
"
" Highlight bad space
highlight BadWhitespace ctermbg=red guibg=red
"
" Clear highlight on the sign column
highlight clear SignColumn
"
" ----------------------Misc settings------------------------------------
"
" Enable folding
set foldmethod=indent
set foldlevel=99
"
" See doc strings for folded code
let g:SimplyFold_docstring_preview=1
"
" EOF
