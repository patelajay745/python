num=[234,35,53,23,2335,3,564]


#map function
square=list(map(lambda x:x*x,num))

print(square)


#filter function
gr_than_99=list(filter(lambda x:x>99,num))

print(gr_than_99)



#reduce function

from functools import reduce
sum_of_num=reduce(lambda x,y:x+y, num)

print(sum_of_num)