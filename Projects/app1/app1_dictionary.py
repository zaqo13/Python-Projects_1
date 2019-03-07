# """1. json file handling"""
#
# import json
# import difflib
# from difflib import SequenceMatcher
# from difflib import get_close_matches
#
# data=json.load(open('076 data.json'))
# def convt(w):
#     if w in data:
#         return data[w]
#     elif len(get_close_matches(w,data.keys())) > 0:
#         cw= input("Do you mean '%s' insted???? Enter 'Y' if that's the word you want to search : " %get_close_matches(w,data.keys()) [0])
#         # print('the cw value ',cw)
#         if cw ==('y' or 'Y'):
#             print('here is your result: ',data[get_close_matches(w,data.keys()) [0] ])
#         else:
#             # print('im in else block')
#             aw=input('Enter the word again or press Enter to exit')
#             # print('im in aw block',aw)
#             if len(aw) >0:
#                 convt(aw)
#             else:
#                 return None
#     else:
#         return ('The word does not exit in dictionary.')
# a=input('Enter the word:- ')
# print(convt(a))

# """lib = difflib == to match the sequence(str)"""
#
# import difflib
# from difflib import SequenceMatcher as sq
# sq=(None,"rainn","rain").ratio()
# print(sq)


# """2. json file handling = 'water' word defination error(UnicodeEncodeError:); solved"""
# #Getting error when we choose 3rd options (enterning 'water' word== becoz in 'water' defn include ('H\u20820') word which causing UnicodeEncodeError: )
# #above code is woking fine
# import json
# import difflib
# from difflib import get_close_matches
#
# data=json.load(open('076 data.json'))
# def convt(w):
#     if w in data:
#         return data[w]
#     elif len(get_close_matches(w,data.keys())) > 0:
#         cw= input("Do you mean '%s' insted???? \nopt1: Enter 'Y' if that's the word you want to search\nopt2: Enter the 'N' to exit.\nopt3: Enter the word again\n " %get_close_matches(w,data.keys()) [0])
#         if cw ==('y' or 'Y'):
#             print('here is your result: ',data[get_close_matches(w,data.keys()) [0] ])
#         elif cw == ('n' or 'N'):
#             print( "the word doesnt exist")
#         else:
#             if len(cw)>1:
#                 print('here is cw',cw)
#                 print (convt(cw))
#     else:
#         return ('The word does not exit in dictionary.')
# a=input('Enter the word:- ')
# print(convt(a))

# """3. json file handling = user friendly & understanding program flow"""
#
# # from difflib import SequenceMatcher
# import json
# import difflib
# from difflib import get_close_matches
#
# data=json.load(open('076 data.json'))
# def convt(w):
#     if w in data:
#         return data[w]
#     elif len(get_close_matches(w,data.keys())) > 0:
#         cw= input("Do you mean %s insted???? Enter Y if that's the word you want to search : " %get_close_matches(w,data.keys()) [0])
#         # print('the cw value ',cw)
#         if cw ==('y' or 'Y'):
#             return data[get_close_matches(w,data.keys()) [0] ]
#         else:
#             return "Sorry, try again"
#     else:
#         return ('The word does not exit in dictionary.')
# a=input('Enter the word:- ')
# op= convt(a)
# # print(op)
# # print(type(op),len(op))
# # print('type of op',type(op))
# # a=[] # if type(op)==type(a):
#
# if type(op)== type(list()):
# # if len(op)>1:
#     n=0
#     for x in op:
#         print('%s :'%(n+1),op[n])
#         n+=1
# else:
#     print(op)


# """4. json file handling = optimise & userfriendly"""
#
# # from difflib import SequenceMatcher
# import json
# import difflib
# from difflib import get_close_matches
#
# data=json.load(open('076 data.json'))
# def convt(w):
#     matches=get_close_matches(w,data.keys())#this will search for close match of w obj in data.json file; this willbe list of objs; objs==max 3 matches(default value n==3)
#     if w in data:
#         return data[w] # this will return list(), obj in list= 0,1,2,3,...n;depends upon defn off word
#     elif len(matches) > 0:
#         cw= input("Do you mean %s insted???? Enter Y if that's the word you want to search or Enter the word again : " %matches [0])
#         if cw ==('y' or 'Y'):
#             return data[matches [0] ]# this will return list(), obj in list= 0,1,2,3,...n;depends upon defn off word
#         elif len(cw)>1:
#             return data[get_close_matches(cw,data.keys()) [0] ]
#         elif cw == ("n" or "N"):
#             return "Sorry, try again later"
#
#     else:
#         return ('The word does not exit in dictionary.')
# a=input('Enter the word:- ')
# op= convt(a)
# if type(op)== type(list()):
#     n=0
#     for x in op:
#         print('%s :'%(n+1),op[n])
#         n+=1
# else:
#     print(op)


# """4. json file handling = optimise & userfriendly"""
#
# # from difflib import SequenceMatcher
# import json
# import difflib
# from difflib import get_close_matches
#
# data=json.load(open('076 data.json'))
# def convt(w):
#     matches=get_close_matches(w,data.keys())
#     w=w.lower()
#     if w in data:
#         return data[w]
#     elif w.title() in data:
#         return data[w.title()]
#     elif w.upper() in data:
#         return data[w.upper()]
#
#     elif len(matches) > 0:
#         cw= input("Do you mean %s insted???? Enter Y if that's the word you want to search or Enter the word again : " %matches [0])
#         if cw ==('y' or 'Y'):
#             return data[matches [0] ]
#         elif len(cw)>1:
#             return data[get_close_matches(cw,data.keys()) [0] ]
#         elif cw == ("n" or "N"):
#             return "Sorry, try again later"
#
#     else:
#         return ('The word does not exit in dictionary.')
# a=input('Enter the word:- ')
# op= convt(a)
# if type(op)== type(list()):
#     n=0
#     for x in op:
#         print('%s :'%(n+1),op[n])
#         n+=1
# else:
#     print(op)
