# f=open("file_to_ready.txt")
# # content=f.read()
# for lines in f:
#     print(lines,end="")
# f.close()


# f=open("file_to_ready.txt","a")
# a=f.write("Ajay, you can do this \n")
# print(a)
# f.close()

sum=0
with open("skip_earning.csv") as my_file:
    # print(my_file.read())
    for lines in my_file:
        earninig=float(lines.split(",CA$")[1].split(",")[0])
        # print(f"earninig: {earninig} sum: {sum}")
        sum=sum+earninig
    
print("%.2f" %sum)
