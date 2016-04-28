from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	# Prints everything in the file

def rewind(f):
	f.seek(0)
	# resets the "cursor" back to the beginning of the file

def print_a_line(line_count, f):
	print line_count, f.readline()
	# Pass it the line number and file you want it to read from

current_file = open(input_file)
# Reads the file into memory

print "First let's print the whole file:\n"

print_all(current_file)
# Prints all lines in the current file

print "Now let's rewind, kind of like a tape."

rewind(current_file)
# Sets the "cursor" back to the beginning of the file

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)
# print line one

current_line = current_line + 1
print_a_line(current_line, current_file)
# Prints line two after incrementing up from one

current_line = current_line + 1
print_a_line(current_line, current_file)
# Prints line three after incrementing up from two