def search_name():
    
    # Open the file and read its content
    with open("file_to_read.txt", 'r') as file:
        content = file.read()
    print("Starting coroutine")
    while True:
        text = (yield)
        if text in content:
            print("Found")
        else:
            print("Not found")

# Create the coroutine with the pre-loaded content
search = search_name()

# Start the coroutine and move to the first yield statement
next(search)

# Send values to the coroutine
for i in range(5):
    search.send(input("Enter text to search:"))

# Close the coroutine
search.close()
