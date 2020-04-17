FILENAME='test.txt'
STRING='Hello World'

create_file_test() {
	if [[ -f "${FILENAME}" ]]; then
		echo -e "\\033[8m<done>1</done>\\033[0m"; 
	fi
}

create_file_test