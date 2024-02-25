import time
 
initial=time.time()

k=0
while(k<45):
    print("test")
    k+=1
print(f"While loop ran time is {time.time()-initial} seconds")

initial2=time.time()
for i in range(45):
    print("this is for loop")
print(f"For loop ran time is {time.time()-initial2} seconds")
  