# #function defination
# def loop_function():
#     for i in range(10):
#         print(i)
#
# loop_function() #Function Call


def loop_function(counter):
    for i in range(counter):
        print(i)
        return 0
count = int(input('Enter a number: '))
loop_function(count)
print(loop_function(count))