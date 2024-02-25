import datetime

def create_content(filename, entry):
    with open(filename, "a") as f:
        f.write(str(get_date()) + " " + entry + "\n")
    print("Data is inserted.")

def read_content(filename):
    with open(filename, "r") as f:
        content = f.readlines()
    print(content)

def get_date():
    return datetime.datetime.now()

def read_data():
    if client == "Rohan":
        if type == "food":
            read_content("Rohan_food.txt")
        else:
            read_content("Rohan_exercise.txt")
    elif client == "Harry":
        if type == "food":
            read_content("Harry_food.txt")
        else:
            read_content("Harry_exercise.txt")
    elif client == "Ajay":
        if type == "food":
            read_content("Ajay_food.txt")
        else:
            read_content("Ajay_exercise.txt")

def insert_data():
    if client == "Rohan":
        if type == "food":
            create_content("Rohan_food.txt", data)
        else:
            create_content("Rohan_exercise.txt", data)
    elif client == "Harry":
        if type == "food":
            create_content("Harry_food.txt", data)
        else:
            create_content("Harry_exercise.txt", data)
    elif client == "Ajay":
        if type == "food":
            create_content("Ajay_food.txt", data)
        else:
            create_content("Ajay_exercise.txt", data)

insert_or_read = input("What do you want to do? Insert data or read? ").lower()
client = input("Enter the name of the client: ").capitalize()
type = input("What do you want to " + insert_or_read + "? Food or Exercise? ").lower()

if insert_or_read == "insert":
    data = input("Enter entry to insert: ").lower()
    insert_data()
elif insert_or_read == "read":
    read_data()
