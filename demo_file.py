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

# file= open("054 example.txt",'w')
# file.write("Line 1\n")# this data wil get lost as we call write method on same file
#
# file=open('060.txt','w')# here file get furnished as a new file as 060.txt (1kb)
# num=[1,2,3,4,5,6,7,8]
# for a in num:
#     file.write(str(a)+'\n')#here previous written data get wipedout  and new data get saved using for loop
# file.close()
# fileR=open('060.txt','r')
# print(fileR.readlines())
# fileR.close()
##
##!!!this is not working::work::'r+' should write at begaining of the file and 'a+' pointer should at end ofthe file.
# file1=open('060.txt','r+')
# print("1st readlins()",file1.readlines())
# print("1st tell()",file1.tell())
# file1.write("this obj is at EOL(End Of the Line)\n ")
# print("2nd tell()",file1.tell())
# print(file1.seek(0))
# print(file1.readlines())
# file1.close()
#
# file2=open('060.txt','a+')
# print(file2.seek(0))
# print('1st tell()',file2.tell())
# # print('file2',file2.readlines())
# file2.write('this obj is at SOL(Start of the Line)\n')
# print(file2.tell())
# print(file2.seek(0))
# print(file2.readlines())
# file2.close()

# with open ('060.txt','a+') as file:
#     file.seek(0)
#     content=file.write("\nthyyyyyyis is with 'with=8'" )
#     print(file.readlines())
