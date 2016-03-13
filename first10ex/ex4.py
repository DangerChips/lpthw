cars = 100
# assigns the variable "cars" the integer value of 100

space_in_a_car = 4.0
# assigns the variable "space_in_a_car" the floating point value of 4.0

drivers = 30
# assigns the variable "drivers" the integer of 30

passengers = 90
# assigns the variable "passengers" the integer of 90

cars_not_driven = cars - drivers
# assigns the "cars_not_driven" variable the cars (100) minus drivers (30) to equal 70

cars_driven = drivers
# assigns "cars_driven" the value of drivers (30)

carpool_capacity = cars_driven * space_in_a_car
# assigns "carpool_capacity" with the value of cars_driven (30) times the value of space_in_a_car (4.0)

average_passengers_per_car = passengers / cars_driven
# assigns "average_passengers_per_car" the value of passengers (90) divided by cars_driven (30)
# will need to account for the Driver!

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There wil be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
