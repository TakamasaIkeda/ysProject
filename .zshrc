#$B%3%^%s%IJd40(B
autoload -Uz compinit 
compinit
zstyle ":completion:*" matcher-list "m:{a-z}={A-Z}"
zstyle ":completion:*:sudo:*" command-path /usr/local/sbin /usr/local/bin \
                     /usr/sbin /usr/bin /sbin /bin /usr/X11R6/bin
#$B4D6-JQ?t(B
export LANG=ja_JP.UTF-8

#$B%W%m%s%W%H@_Dj(B
PROMPT='[%F{red}%B%n%b%f@%F{blue}%U%m%u%f]# '
RPROMPT='[%F{green}%d%f]'

#umask(permission)
umask 022

#$BMzNr(B
HISTFILE=~/.zsh_history
HISTSIZE=100000
SAVEHIST=100000
setopt hist_ignore_all_dups
setopt share_history
setopt append_history
setopt inc_append_history
setopt hist_no_store
setopt EXTENDED_GLOB

#setopt
setopt auto_cd
setopt pushd_ignore_dups
setopt share_history
setopt hist_ignore_all_dups
setopt hist_reduce_blanks
setopt extended_glob
setopt correct
setopt no_beep
setopt nonomatch

#alias 
alias rm='rm -i'
alias sl='ls'
alias pip-update="pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs pip install -U"
#rbenv
export PATH=/usr/local/bin:$PATH

#golang
export GOPATH=$HOME/.go:$PATH

#dein
export XDG_CONFIG_HOME=$HOME/.config
