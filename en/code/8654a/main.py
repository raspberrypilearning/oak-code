from random import randint
questions = 0
while questions <10: 
    a = randint(2,12)
    b = randint(2,12)
    print(a, "times", b, "=")
    answer = int(input())
    product = a * b
    if answer == product:
  	    print("That is correct")
    else:
        print("I am sorry")
        print(a, "times", b, "is", product)
    questions = questions +1