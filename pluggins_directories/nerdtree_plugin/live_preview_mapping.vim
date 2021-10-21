" Author        : kostas
" Created       : 05/10/2021
" License       : MIT
" Description   : 
if exists("g:loaded_nerdree_live_preview_mapping")
  finish
endif
let g:loaded_nerdree_live_preview_mapping = 1

call NERDTreeAddKeyMap({
      \ 'key':           '<up>',
      \ 'callback':      'NERDTreeLivePreview',
      \ 'quickhelpText': 'preview',
      \ })
