
FILENAME='test.txt'
STRING='Hello World'

init() {
	unset precmd_functions
	unset preexec_functions
	rm -f ${FILENAME};
}