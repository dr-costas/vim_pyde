" ~/.vimrc file starts
"
" ==================================
" VIM settings file
" ==================================
"
set nocompatible              			" be iMproved, required
filetype plugin indent on    			" required
"
" ----------------------Plugin settings------------------
"
" Start Plug
call plug#begin('~/.vim/plugged')
" Add plugins
"
" Plug 'scrooloose/nerdtree'               	" File browser in VIM
" Plug 'jistr/vim-nerdtree-tabs'           	" File browser support for tabs
Plug 'neoclide/coc.nvim', {'branch': 'release'} " Coc plugin
Plug 'puremourning/vimspector' 		  	" Debugging plugin
" Plug 'Xuyuanp/nerdtree-git-plugin'        	" Plugin for NERDTRee and Git integration
Plug 'tpope/vim-fugitive'                 	" GIT integration
Plug 'tpope/vim-markdown' 		  	" Markdown fancy stuff
Plug 'Yggdroot/indentLine' 			" Vertical bars for indentation
Plug 'mhinz/vim-signify' 			" Indication of file changes
Plug 'tibabit/vim-templates' 			" Template files
"       Color schemes
Plug 'NLKNguyen/papercolor-theme'               " Papercolor theme
Plug 'itchyny/lightline.vim'                    " Status line
"
call plug#end()            			" required

" ----------------------General settings------------------
"
" Setting of variables
set hlsearch! 				" Clear the highlight of last search
"
syntax on           			" Syntax highlight.
"
set encoding=utf8   			" Encoding.
"
set t_Co=256        			" 256 colours
"
set number          			" Absolute line numbers.
"
set relativenumber  			" Relative line numbers
"
set cursorline 				" Enable cursor line
"
set splitright      			" Vertical split adds new window to the right.
"
set hidden          			" Allows you to switch from an unsaved buffer
		            		" without saving it first. Also allows
                    			" you to keep an undo history for multiple files.
                    			" Vim will complain if you try to quit without
                    			" saving, and swap files will keep you safe if
                    			" your computer crashes.
"
set autoindent	    			" When opening a new line and no filetype-specific
		            		" indenting is enabled, keep the same indent as
		            		" the line you're currently on. Useful for READMEs, etc.
"
set nostartofline   			" Stop certain movements from always going to the
					" first character of a line. While this behavior
		            		" deviates from that of Vi, it does what most users
		            		" coming from other editors would expect.
"
set wildmenu        			" Better command-line completion
"
set ruler  	        		" Display the cursor position on the last line of
        		    		" the screen or in the status line of a window.
"
set hlsearch        			" Highlight searches (use <C-L> to temporarily turn
                    			" off highlighting; see the mapping of <C-L>
	        	    		" below)
"
set ignorecase      			" Use case insensitive search, except when using
"
set smartcase 	    			" capital letters
"
set confirm	        		" Instead of failing a command because of unsaved
		            		" changes, instead raise a dialogue asking if you
        		    		" wish to save changed files
"
set visualbell	    			" Use visual bell instead of beeping when doing
		            		" something wrong
"
set t_vb=	        		" And reset the terminal code for the visual bell.
        		    		" If visualbell is set, and this line is also included,
        		    		" vim will neither flash nor beep.  If visualbell
        		    		" is unset, this does nothing.
"
set mouse=a 	    			" Enable use of the mouse for all modes
"
set cmdheight=1	    			" Set the command window height to 2 lines, to avoid
		            		" many cases of having to "press <Enter> to continue"
"
set pastetoggle=<F2> 			" Use <F2> to toggle between 'paste' and 'nopaste'
"
set backspace=indent,eol,start  	" Allow backspacing over autoindent,
					" line breaks and start of insert action
"
set notimeout ttimeout ttimeoutlen=200  " Quickly time out on keycodes, but
				        " never time out on mappings
"
set clipboard=unnamed 			" Access system clipboard
"
set spellfile=~/.vim/spell/en.utf-8.add " Spell file
"
" Set syntax highlight for .vimsettings files
autocmd BufNewFile,BufRead *.vimsettings set filetype=vim
"
" ------------General and plugins settings------------------
"
" Mappings
source ~/.myvim_files/plugins_settings/mappings.vimsettings
"
" NERDTree related
""source ~/.myvim_files/plugins_settings/nerdtree.vimsettings
" 
" NETRW related
source ~/.myvim_files/plugins_settings/netrw.vimsettings
"
" COC related
source ~/.myvim_files/plugins_settings/coc.vimsettings
"
" PaperColor related
source ~/.myvim_files/plugins_settings/paper_color.vimsettings
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
" ----------------------Appearance settings------------------
"
" Highlight comments
highlight Comment cterm=bold
" 
" Cursor line appearance
highlight CursorLine cterm=NONE ctermbg=236 ctermfg=NONE
"
" Highlight bad space
highlight BadWhitespace ctermbg=red guibg=red
"
"
" ----------------------Misc settings------------------
"
" Enable folding
set foldmethod=indent
set foldlevel=99
"
" See doc strings for folded code
let g:SimplyFold_docstring_preview=1
"
" EOF
