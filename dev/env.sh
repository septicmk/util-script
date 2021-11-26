export HOME="/root"
export PATH="$HOME/runtime/bin:$PATH"
export PATH="/usr/local/bin:$PATH"
export PATH="$HOME/script:$PATH"
export FZF_DEFAULT_COMMAND="rg --files --hidden -g'!.git'"
alias cmake="cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=on"

export RUST_HOME="~/.cargo"
export PATH="${RUST_HOME}/bin:$PATH"

export CUDA_HOME="/usr/local/cuda"
export PATH="$CUDA_HOME/bin:$PATH"
export LD_LIBRARY_PATH="/lib64/:$LD_LIBRARY_PATH"

export LD_LIBRARY_PATH="$HOME/runtime/lib:$LD_LIBRARY_PATH"
export LIBRARY_PATH="$HOME/runtime/lib:$LIBRARY_PATH"
export C_INCLUDE_PATH="$HOME/runtime/include/:$C_INCLUDE_PATH"
export CPLUS_INCLUDE_PATH="$HOME/runtime/include/:$CPLUS_INCLUDE_PATH"

export CPLUS_INCLUDE_PATH="/root/runtime/arrow/apache-arrow-0.17.1/cpp/src/:$CPLUS_INCLUDE_PATH"

alias vim="vim -u $HOME/.vimrc"
#alias mpirun="mpirun --allow-run-as-root"
function git_branch {
  branch="`git branch 2>/dev/null | grep "^\*" | sed -e "s/^\*\ //"`"
    if [ "${branch}" != "" ];then
        if [ "${branch}" = "(no branch)" ];then
            branch="(`git rev-parse --short HEAD`...)"
        fi
        echo " ($branch)"
    fi
}

export PS1='\[\033]0;\u@24CPU:\W\007\]\[\033[01;33m\][\u@24CPU]\[\033[01;37m\] \W\[\033[01;32m\]$(git_branch)\[\033[01;34m\] \$\[\033[00m\] '
