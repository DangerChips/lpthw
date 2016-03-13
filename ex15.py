from sys import argv
# imports argv module from sys library

script, filename = argv
# asks for 1 argument which will be appended to the 'filename' variable

txt = open(filename)
# declares the txt variable passing it the value of the filename's contents.

print "Here's your file %r: " % filename
# prints string with filename variable.
print txt.read()
# prints the content of txt variable

print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)

print txt_again.read()