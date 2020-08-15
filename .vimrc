colo ron

set noeb vb t_vb=
au GUIEnter * set vb t_vb=

set nocompatible
syntax on
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set backspace=indent,eol,start
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile

highlight LineNr term=bold cterm=NONE ctermfg=DarkGrey ctermbg=NONE gui=NONE guifg=DarkGrey guibg=NONE

nnoremap <Space><F5> :!python "%"<CR>
nnoremap i<F5> :!python -i "%"<CR>
nnoremap t<F5> :!python -m pytest "%"<CR>
