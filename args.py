# # *args-->variable length argument(*names)
# def display_name(*names):
#     for name in names:
#         print('Hi {}'.format(name))
#
# display_name('Sahan','Eresh','Apoorba')



# **kwargs--> key word argument (**names)

def display_name(**names):
    for k,v in names.items():
        print('{}----{}'.format(k,v))

display_name(fname='Apoorba',lname='Rana')