def task_one():
    print("What is your name?")
    name = input()
    def greet_user(name):
        print("Hi there", name, "how are you today?")
    greet_user(name)

def task_one_part2():
    print("Provide two numbers for this exercise: ")
    number_one = int(input("Enter first number: "))
    number_two = int(input("Enter second number: "))
    total = number_one + number_two
    def add_numbers(sum_value):
        print("The sum is", sum_value)
    add_numbers(total)

def task_two():
    print("Name your pet for this exercise:")
    pet = input()
    print("What kind of animal is", pet + "?")
    animal = input()
    def describe_pet(pet_name, animal_type):
        print("I have a pet named " + pet_name + " and they are a " + animal_type)
    describe_pet(pet, animal)

def task_three():
    print("How many toppings would you like on your sandwich? (Max 3 toppings)")
    number = int(input("Enter number of toppings: "))
    if number > 3:
        print("Sorry, you cannot add more than three toppings.")
        return
    toppings = []
    if number >= 1:
        greens = input("Would you like any greens? (Type the name or 'none'): ")
        if greens.lower() != 'none':
            toppings.append(greens)
    if number >= 2:
        condiments = input("Would you like any condiments? (Type the name or 'none'): ")
        if condiments.lower() != 'none':
            toppings.append(condiments)
    if number == 3:
        cheese = input("Would you like any cheese? (Type the name or 'none'): ")
        if cheese.lower() != 'none':
            toppings.append(cheese)
    if toppings:
        print("Making a sandwich with the following ingredients:", ", ".join(toppings))
    else:
        print("Making a plain sandwich with no toppings.")

def task_four():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)

    fact_result = factorial(5)
    fib_result = fibonacci(6)
    print(f"Factorial of 5 is {fact_result}. The 6th Fibonacci number is {fib_result}.")

task_one()
task_one_part2()
task_two()
task_three()
task_four()
