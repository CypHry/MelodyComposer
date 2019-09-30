#!/bin/bash

## splitABC.sh - Spliting huge ABC files utility
##
## This script splits one huge file full of ABC melodies.
## Each created during split file contains one melody.
## USAGE: ./splitABC.sh fileToSplit fileToSplit2 ...
## All passed filenames are used. Passing no arguments has no effect.

if [ $# -eq 0 ];
then printf "No file passed as argument.\n";
     printf "\n"
     printf "USAGE: ./splitABC.sh fileToSplit fileToSplit2 ...\n"
fi
