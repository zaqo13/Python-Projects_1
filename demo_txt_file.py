# """filDM==[Files data Mixing and saving in single file]"""

# a=['box1','box2','box3']
# cont=['contain1','contain2','contain3']
# for (fn) in a :
#     with open (fn +'.txt','w') as s1:
#         s1.write(b)
#         print (s1.readlines())

# """Creating .txt Files with a=x1,x2,x3,...xn names and x1 contains=y1,y2,y3,...yn;  x2 contains=y1,y2,y3,...yn data"""

# a=['box1','box2','box3']
# cont=['con1','con2','con3']
# for fn in a :
#     for nm in cont:
#         with open(fn+'.txt','a+') as s1:
#             print(s1.tell())
#             s1.write(nm)

# """Copy all data from n different files and storing them in single file"""
#
# a=['box1','box2','box3']
# with open('Big_box.txt','r+') as Bb:
#         with open(b+'.txt','r') as c:
#     for b in a:
            ##Bb.write(c.read()+'\n')
            #cont2=c.readlines()
#             # print('cont',cont2)
#             for d in cont2:
#                 Bb.write(d)
#             Bb.seek(0)
#             print(Bb.readlines())

# """soln - 2; Copying all data from n different files and storing them in single file; filename==current time"""
#
# import datetime
#
# a=['box1','box2','box3']
# with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+'.txt','w') as file:
#     for filename in a:
#         with open (filename+'.txt','r') as f:
#             file.write(f.read()+'\n')
