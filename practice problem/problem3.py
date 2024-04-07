

a=[55,44,36,29,27,22,19]

b = a.copy()
b.reverse()
# using first method
print('Reversed List using first method:', b)

c=a
#using second method
print('Reversed List using second method:',c[::-1])

# swapping using third method
n = len(a)


for i in range(n // 2):
    
    a[i], a[n - i - 1] = a[n - i - 1], a[i]


print('Reversed List using third method:',a)
