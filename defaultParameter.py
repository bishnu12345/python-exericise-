def greeting(firstName,lastName,isSenior=False):
    if isSenior:
        print('Namaste {} {}'.format(firstName,lastName))
    else:
        print('Hello {}'.format(firstName))

greeting('Apoorba','Rana')