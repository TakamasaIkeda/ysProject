"dein.vim
"read this page to setup(http://wonderwall.hatenablog.com/entry/2016/03/12/233846)
if &compatible 
  set nocompatible
endif


filetype plugin indent on

"¹ÔÈÖ¹æ
set number
set ruler
set cursorline

"¥¿¡¼¥ß¥Ê¥ëÀÜÂ³¤ò¹âÂ®¤Ë¤¹¤ë
set ttyfast 

"Ê£¿ô¥Õ¥¡¥¤¥ë¤ÎÊÔ½¸¤ò²ÄÇ½¤Ë
set hidden
"¥¦¥£¥ó¥É¥¦¥¿¥¤¥È¥ë
set title
"syntax
syntax on

"256colours in terminal
set t_Co=256

set nobackup

"indent
set expandtab
set tabstop=2
set shiftwidth=2
set softtabstop=2
set autoindent
set ambiwidth=double
"set smartindent

"³ç¸ÌÊä´°
inoremap { {}<Left>
inoremap {<Enter> {}<Left><CR><ESC><S-o>
inoremap [ []<Left>
inoremap ( () <Left>
inoremap (<Enter> ()<Left><CR><ESC><S-o>
inoremap " ""<Left>
set showmatch

"encoding auto-distinction
:set encoding=utf-8

"cron¤Î¼Â¹Ô»þ¤Ëvimrc¤Î¥Ð¥Ã¥¯¥¢¥Ã¥×¥Õ¥¡¥¤¥ë¤¬¼ÙËâ¤·¤Æcron¤¬Æ°¤«¤Ê¤¤¤Î¤òËÉ¤°
set backupskip=/tmp/*,/private/tmp/*

nnoremap O :<C-u>call append(expand("."), "")<Cr>j

"man command
runtime ftplugin/man.vim

"search words
set ignorecase
set wrapscan
set wildmenu
set hlsearch
set incsearch
set smartcase
imap <c-j> <esc>
