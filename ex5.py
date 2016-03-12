my_name = "Zed A. Shaw"
# string variable
my_age = 35
# integer variable
my_height = 74 # inches
# integer variable
my_weight = 180
# integer variable
my_eyes = "Blue"
# string variable
my_teeth = "White"
# string variable
my_hair = "Brown"
# string variable
# generic white guy

print "Let's talk about %s." % my_name
# %s is a placeholder for my_name variable.
print "He's %d inches tall." % my_height
# %d is a placeholder for the my_height variable.
print "He's %d pounds heavy." % my_weight
# %d is a placeholder for the my_weight variable.
print "Actually that's not too heavy." 
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# %s is a placeholder for the my_eyes, my_hair variables.
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)