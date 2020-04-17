#!/bin/bash

# Copyright Mario Di Francesco 2020


FILENAME='test.txt'
STRING='Hello World'

init() {
unset precmd_functions
unset preexec_functions
rm -f ${FILENAME};
}


create_file_test() {
if [[ -f "${FILENAME}" ]]; then
echo "file test done" ;
echo -e "\\033[8m<done>1</done>\\033[0m"; 
fi
}

file_string_test() {
if grep -sq "${STRING}" ${FILENAME}; then
echo "string is present"
echo -e "\\033[8m<done>2</done>\\033[0m"; 
fi
}

output_test() {
if [[ "$(echo ${1} | tr -s '[:space:]')" == "cat ${FILENAME}" ]] ; then
echo "output_test successfully done"
fi
}
