def multiplication_table(number):
    print("Multiplication Table of {num}")
    for i in range(1,11):
        print(f"{number} * {i} = {i*number}")

num=int(input("enter your number="))
multiplication_table(num)