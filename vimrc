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
source other_files/directives_that_go_on_top.vimsettings
"
" -----------------------------------------------------------------------
" 		Plugin definitions
" -----------------------------------------------------------------------
"
" ---- Plugin settings
source vim_settings/plugins.vimsettings
"
" -----------------------------------------------------------------------
" 		General settings
" -----------------------------------------------------------------------
"
" ---- General settings
source vim_settings/general_settings.vimsettings
"
" ---- Functions and commands
source vim_settings/functions_and_commnads.vimsettings
"
" ---- Mappings
source vim_settings/mappings.vimsettings
"
" ---- Miscellaneous 
source vim_settings/misc_settings.vimsettings
"
" -----------------------------------------------------------------------
" 		Mappings and plugins settings
" -----------------------------------------------------------------------
"
" ---- COC
source plugins_settings/coc.vimsettings
"
" ---- Gruvbox 
source plugins_settings/gruvbox.vimsettings
" 
" ---- IndentLine
source plugins_settings/indent_line.vimsettings
"
" ---- Lightline
source plugins_settings/lightline.vimsettings
"
" ---- Lightline buffer
source plugins_settings/lightline_buffer.vimsettings
"
" ---- NERDTree
source plugins_settings/nerdtree.vimsettings
"
" ---- Python docstring
source plugins_settings/python_docstring.vimsettings
"
" ---- REPL
source plugins_settings/repl.vimsettings
"
" ---- Tagbar
source plugins_settings/tagbar.vimsettings
"
"---- Vim templates
source plugins_settings/vim_templates.vimsettings
"
" ---- Vimspector
source plugins_settings/vimspector.vimsettings
"
" EOF
