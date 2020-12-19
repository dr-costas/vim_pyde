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
" Plugin settings file
source ~/.myvim_files/vim_settings/plugins_settings.vimsettings
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
" Appearance settings file
source ~/.myvim_files/vim_settings/appearance_settings.vimsettings 
"
" EOF
