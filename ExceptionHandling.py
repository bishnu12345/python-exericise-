# try:
#     age = int(input('Enter your age: '))
#     print('Your age is {}'.format(age))
# except:
#     print('Exception occurred')



# try:
#     age = int(input('Enter your age: '))
#     print('Your age is {}'.format(age))
# except ValueError:
#     print('That is not a number')



# try:
#     num1= int(input('Enter first number'))
#     num2 = int(input('Enter second number'))
#     div = num1/num2
# except(ValueError,ZeroDivisionError):
#     print('Exception occurred')



# try:
#     num1= int(input('Enter first number'))
#     num2 = int(input('Enter second number'))
#     div = num1/num2
# except ValueError:
#     print('Exception occurred')
# except ZeroDivisionError:
#     print('Division by 0 not possible')



# try:
#     num1= int(input('Enter first number'))
#     num2 = int(input('Enter second number'))
#     div = num1 / num2
# except ValueError:
#     print('Exception occurred')
# except ZeroDivisionError:
#     print('Division by 0 not possible')
# else:
#     print('division done')
# finally:
#     print('Finally Block')


try:
    age = int(input('Enter your age:'))
    if(age<0):
        raise ValueError('Age should be greater than 0')
except ValueError as e:
    print(e)
else:
    print(age)