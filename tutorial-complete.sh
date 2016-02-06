_tutorial_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _TUTORIAL_COMPLETE=complete $1 ) )
    return 0
}

complete -F _tutorial_completion -o default tutorial;
