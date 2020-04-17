FILENAME='test.txt'
STRING='Hello World'

file_string_test() {
	if grep -sq "${STRING}" ${FILENAME}; then
		echo -e "\\033[8m<done>2</done>\\033[0m"; 
	fi
}

file_string_test