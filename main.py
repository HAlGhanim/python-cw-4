# الجزء الاول
def my_name():
    name = "Humoud"
    return "My name is " + name
print(my_name())

# الجزء الثاني
def my_meal(food, drink):
    print(f"I like to eat {food} and while drinking {drink}")
my_meal("Burgers","Coke")  

# الجزء الثالث
def cube(number):
    cubed = number **3
    return print(f"The number to the power of the is {cubed}")
def by_three(number):  
    if number%3==0:
        cube(number)
    else:
        print(False)
number = eval(input("Enter a number: ")) 
by_three(number)
