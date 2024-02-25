
a=int(input("enter value: "))
i=1
user_input = input("Enter true or false: ").lower()  # Convert input to lowercase for case-insensitivity

# if user_input == 'true':
#     while i<=a: #i=1 a=5    
#         j=1
#         while j<=i: #j=1 i=1
#             print("*",end="")  #print *
#             j+=1
#         print("")
#         i+=1
# elif user_input == 'false':
#    i=a
#    while i>=0: #i=1 a=5    
#         j=i
#         while j>0: #j=1 i=1
#             print("*",end="")  #print *
#             j-=1
#         print("")
#         i-=1
# else:
#     print("Invalid input. Please enter 'true' or 'false'.")

if user_input == 'true':
    for i in range(1,a+1):
        print("*"*i)
elif user_input == 'false':
    for i in range(a,0,-1):
        print("*"*i)
else:
     print("Invalid input. Please enter 'true' or 'false'.")