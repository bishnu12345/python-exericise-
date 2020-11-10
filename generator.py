# def new_list(num):
#     count = 0
#     nlist=[]
#     while count<=num:
#         nlist.append(count)
#         count+=1
#     return nlist
#
# value = new_list(5)
# print(value)


#keyword---->yield
# def new_list(num):
#     count = 0
#     while count<=num:
#         yield count
#         count+=1
# value = new_list(5)
# v = list(value)
# print(v)



def odd_num():
    a=10
    while a<20:
        if(a%2!=0):
            yield a
        a+=1

v = odd_num()
value = list(v)
print(value)