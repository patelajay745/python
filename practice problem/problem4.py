def find_next_palindrome(n):
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            return n

no = int(input("How many numbers do you want to check? "))
a_list = [int(input("Enter the number to find the next palindrome: ")) for _ in range(no)]
palindrom_list=[]

for num in a_list:
    if(num<10):
        palindrom_list.append(num)
    else:    
        next_palindrome = find_next_palindrome(num)
        palindrom_list.append(next_palindrome)
    
print(f"palindrom list is {palindrom_list}")

