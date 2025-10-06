try:
    value=int(input('Enter a number: '))
    print(10/value)
except ValueError:
    print('Please enter a number')
except ZeroDivisionError:
    print('cannot divide by zero')
finally:
    print('Execution finished')
