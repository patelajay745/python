from datetime import datetime

fileExtension=".jpg"
timestamp = str(int(datetime.now().timestamp()))+fileExtension
print(timestamp)
