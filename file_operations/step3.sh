FILENAME='test.txt'
STRING='Hello World'

output_text() {

  if [[ "${1}" == "cat ${FILENAME}" ]] ; then
  	    echo -e "\\033[8m<done>3</done>\\033[0m"; 
  fi
}

output_text
