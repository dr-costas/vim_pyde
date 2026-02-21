"
" ==================================
" Vim run commands file
" ==================================
"
" -----------------------------------------------------------------------
" 		Directives that go on top
" -----------------------------------------------------------------------
"
" Directives that go on top and are not tracked by git
" The file: myvim_files/other_files/directives_that_go_on_top.vimsettings
" has to be manually created.
source ~/vim_pyde/other_files/directives_that_go_on_top.vimsettings
"
" -----------------------------------------------------------------------
" 		Plugin definitions
" -----------------------------------------------------------------------
"
" ---- Plugin settings
source ~/vim_pyde/vim_settings/plugins.vimsettings
"
" -----------------------------------------------------------------------
" 		General settings
" -----------------------------------------------------------------------
"
" ---- General settings
source ~/vim_pyde/vim_settings/general_settings.vimsettings
"
" ---- Functions and commands
source ~/vim_pyde/vim_settings/functions_and_commnads.vimsettings
"
" ---- Mappings
source ~/vim_pyde/vim_settings/mappings.vimsettings
"
" ---- Miscellaneous 
source ~/vim_pyde/vim_settings/misc_settings.vimsettings
"
" -----------------------------------------------------------------------
" 		Mappings and plugins settings
" -----------------------------------------------------------------------
"
" ---- COC
source ~/vim_pyde/plugins_settings/coc.vimsettings
"
" ---- Gruvbox 
source ~/vim_pyde/plugins_settings/gruvbox.vimsettings
" 
" ---- IndentLine
source ~/vim_pyde/plugins_settings/indent_line.vimsettings
"
" ---- Lightline
source ~/vim_pyde/plugins_settings/lightline.vimsettings
"
" ---- Lightline buffer
source ~/vim_pyde/plugins_settings/lightline_buffer.vimsettings
"
" ---- NERDTree
source ~/vim_pyde/plugins_settings/nerdtree.vimsettings
"
" ---- Python docstring
source ~/vim_pyde/plugins_settings/python_docstring.vimsettings
"
" ---- REPL
source ~/vim_pyde/plugins_settings/repl.vimsettings
"
" ---- Tagbar
source ~/vim_pyde/plugins_settings/tagbar.vimsettings
"
"---- Vim templates
source ~/vim_pyde/plugins_settings/vim_templates.vimsettings
"
" ---- Vimspector
source ~/vim_pyde/plugins_settings/vimspector.vimsettings
"
set noautochdir
"
" -----------------------------------------------------------------------
" 		Directives that go last
" -----------------------------------------------------------------------
"
" Directives that go last and are not tracker by Git
" The file: myvim_files/other_files/directives_that_go_last.vimsettings
" has to be manually created.
source ~/vim_pyde/other_files/directives_that_go_last.vimsettings
"
" EOF
