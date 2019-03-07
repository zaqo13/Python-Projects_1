# s1=open('054 example.txt','r')
# print(type(s1))
# new2=s1.read()
# print(new2)
# print(type(new2))
# s1.seek(0)
# print(s1.readlines())
# new2=[i.rstrip("\n") for i in new2]
# print(new2)
# print(type(new2))

# file= open("054 example.txt",'a')
# # print('reading the file= ',file.read())
# print('seeking the pointer at=0 ',file.seek(0))
# print('telling the pointer where it is= ',file.tell())
# # print('reading the file & return list= ',file.readlines())
# print(file.append('hi sagar this is 2nd line'))
# print(file.tell)
# print(file.readlines())

# a=open('dfile.txt','r')
# print(a.readline())
# print(a.tell())
# a=open('dfile.txt','w')
# a.write(' thisis write function')
# # print(a.readline())
# a.close()
# a=open('dfile.txt','r')
# a.read()
# print(a.tell())
# a.close()
# a=open('dfile.txt','a')
# a.write(' this is append fuction line')
# print(a.tell())
# a=open('dfile.txt','r')
# print(a.tell())
# print(a.read())
# a.close()

# a=open('dfile.txt','r')
# b=a.readlines()
# # print(b)
# list1=[]
# for c in b:
#     print('c is =',c)
#     print(type(c))
#     list1.append(c)
#     print('list1 1 is ',list1)

# a=open('dfile.txt','w')
# list=['line 1','line 2','line 3']
# for b in list:
#     a.write(b+'\n')
#     # print(a)
# a.close()

# file=open('dfile.txt','r')
# print(file.readlines())
# file.seek(0)
# print(file.readline())
# print(file.tell())
# print(file.readline())
# print(file.tell())
# file.close()



# for c in (file.readlines()):
#     print(c)
#     print(type(c))
