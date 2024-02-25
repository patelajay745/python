# ls=[]

# for i in range(1,100):
#     if i%3==0:
# #         ls.append(i)

# ls=[i for i in range(1,100) if i%3==0]

# print(ls)


# dict1={ 0:"item0",
#        1:"item1",
#        2:"item2"}

# print(dict1)

# dict2={
#     f"item{i}":i for i in range(1,101) if i%3==0
# }


# dict2={value:key for key,value in dict2.items()}
# print(dict2)


# # genrator
# evens= (i for i in range(1,100) if i%3==0)

# print(evens.__next__())

list_item=[]


no_of_item=int(input("How many items :"))
for i in range(0,no_of_item):
    list_item.append(input("Enter the item : "))

type_compre=int(input("what you want to generate: 1 for list , 2 for dict, 3 for set comprehenation : "))

if(type_compre==1):
    ls=[item for item in list_item]
    print(ls)
elif(type_compre==2):
    dict2={i:f"{item}" for i,item in enumerate(list_item)  }
    print(dict2)
elif(type_compre==3):
    # Create a set using a set comprehension
    set1 = {item for item in list_item}

    # Print the set
    print(set1)