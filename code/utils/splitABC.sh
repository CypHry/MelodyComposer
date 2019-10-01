#!/bin/bash

## splitABC.sh - Splitting huge ABC files utility
##
## This script splits one huge file full of ABC melodies.
## Each created during split file contains one melody.
## USAGE: ./splitABC.sh FILE [-p PREFIX] [-o OUTPUT]
## where FILE is file to split,
## PREFIX is new files prefix (default is abc: abc00, abc01, abc02 ...),
## OUTPUT is output directory (default is .).
##
## exit 1 - indicates no passed arguments

usage() {
    echo USAGE: ./splitABC.sh FILE [-p PREFIX] [-o OUTPUT]
}

if [[ $# -eq 0 ]]; then
    usage
    exit 1
fi

fileName=$1
shift
prefix="abc"
output="."

while getopts "p:o:" opt; do
    case "${opt}" in
        p)
            prefix=$OPTARG
            ;;
        o)
            output=$OPTARG
            ;;
    esac
done

finalPrefix="${output}/${prefix}"
csplit -z -s -f ${finalPrefix} ${fileName} /X:/ '{*}'

# TODO:
# this removes files smaller than 5 bytes in case the files starts with some \n characters
# should be reimplemented later for any number of \n characters at the beginning of the file
# for now 5 bytes is a fine as a valid abc file is much bigger
find ${output} -name "${prefix}*" -type 'f' -size -5c -delete
