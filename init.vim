""" Plugins!
call plug#begin('C:\Users\Brutter1\AppData\Local\nvim\plugged')
Plug 'navarasu/onedark.nvim'
Plug 'junegunn/vim-journal'
Plug 'itchyny/lightline.vim'
Plug 'junegunn/rainbow_parentheses.vim'
Plug 'nightsense/forgotten'
Plug 'arcticicestudio/nord-vim'
Plug 'mhinz/vim-startify'
Plug 'junegunn/goyo.vim'
Plug 'tpope/vim-sensible'
Plug 'preservim/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'
Plug 'jiangmiao/auto-pairs'
Plug 'sheerun/vim-polyglot'
Plug 'chrisbra/Colorizer'
Plug 'psliwka/vim-smoothie'
Plug 'w0rp/ale'
Plug 'ncm2/ncm2'
Plug 'roxma/nvim-yarp'
Plug 'ncm2/ncm2-bufword'
Plug 'ncm2/ncm2-path'
Plug 'ncm2/ncm2-jedi'
Plug 'Chiel92/vim-autoformat'
call plug#end()

""" Main Configurations
filetype plugin indent on
set tabstop=4 softtabstop=4 shiftwidth=4 expandtab smarttab autoindent
set incsearch ignorecase smartcase hlsearch
set wildmode=longest,list,full wildmenu
set ruler laststatus=2 showcmd showmode
set list listchars=trail:»,tab:»-
set fillchars+=vert:\ 
set wrap breakindent
set encoding=utf-8
set textwidth=0
set hidden
set number
" set title
set mouse=a

""" Coloring

" Main Coloring Configurations
syntax on
colorscheme onedark

" Enable True Color Support (ensure you're using a 256-color enabled $TERM, e.g. xterm-256color)
set termguicolors

""" Plugin Configurations

" Deoplete
let g:deoplete#enable_at_startup = 1

" NERDTree
let NERDTreeShowHidden=0

" Startify
let g:startify_fortune_use_unicode = 1

" Startify + NERDTree on start when no file is specified
autocmd VimEnter *
    \   if !argc()
    \ |   Startify
    \ |   NERDTree
    \ |   wincmd w
    \ | endif

" vim-autoformat
noremap <F3> :Autoformat<CR>

" NCM2
augroup NCM2
  autocmd!
  " enable ncm2 for all buffers
  autocmd BufEnter * call ncm2#enable_for_buffer()
  " :help Ncm2PopupOpen for more information
  set completeopt=noinsert,menuone,noselect
  " When the <Enter> key is pressed while the popup menu is visible, it only
  " hides the menu. Use this mapping to close the menu and also start a new line.
  inoremap <expr> <CR> (pumvisible() ? "\<c-y>\<cr>" : "\<CR>")
augroup END

" Ale
let g:ale_lint_on_enter = 0
let g:ale_lint_on_text_changed = 'never'
let g:ale_echo_msg_error_str = 'E'
let g:ale_echo_msg_warning_str = 'W'
let g:ale_echo_msg_format = '[%linter%] %s [%severity%]'
let g:ale_linters = {'python': ['flake8']}

" context.vim
let g:context_nvim_no_redraw =1

""" Filetype-Specific Configurations
" Markdown
autocmd FileType markdown setlocal shiftwidth=2 tabstop=2 softtabstop=2
" Python
autocmd FileType python imap <buffer> <Space><F5> <esc>:w<CR>:exec '!clear' <CR>:exec '!python' shellescape(@% 1)<CR>

let g:lightline = {
      \ 'colorscheme': 'one',
      \ 'active': {
      \   'left': [ ['mode'] ],
      \ },
      \ }

""" Custom Functions

" Trim Whitespaces
function! TrimWhitespace()
    let l:save = winsaveview()
    %s/\\\@<!\s\+$//e
    call winrestview(l:save)
endfunction

""" Custom Mappings

let mapleader=","
nmap <leader>m :NERDTreeToggle<CR>
nmap <leader>t :call TrimWhitespace()<CR>
nmap <leader>z :Goyo<CR>
