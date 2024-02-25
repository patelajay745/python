operator=(input("Choose Operation from *,+,/,- : "))
varibale_one=(float(input("Enter the first value: ")))
varibale_second=(float(input("Enter the second value: ")))

if (varibale_one== 45.0 or varibale_second == 45.0) and (varibale_one== 3.0 or varibale_second == 3.0) and (operator=="*"):
    print("555")
elif (varibale_one== 56.0 or varibale_second == 56.0) and (varibale_one== 9.0 or varibale_second == 9.0) and (operator=="+"):
    print("77")
elif (varibale_one== 56.0 or varibale_second == 56.0) and (varibale_one== 6.0 or varibale_second == 6.0) and (operator=="/"):
    print("4")
else:
    # Use the format function to concatenate strings and variables
    result = eval(f"{varibale_one}{operator}{varibale_second}")
    print(result)

