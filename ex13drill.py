from sys import argv
# imports the argv module

script, first, second = argv
third = raw_input("How do you feel? ")

print "Your first argument is %s." % first
print "Your second argument is %s." % second
print "That makes me feel %s." % third
