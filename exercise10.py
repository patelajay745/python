import requests
import pickle
import json
import zipfile
import io
import os

response = requests.get('https://archive.ics.uci.edu/static/public/53/iris.zip')
zip_data = io.BytesIO(response.content)
with zipfile.ZipFile(zip_data, 'r') as zip_ref:
        zip_ref.extractall('iris_dataset')
print("Download and extraction successful.")

iris_data_path = os.path.join('iris_dataset', 'iris.data')

with open(iris_data_path, 'r') as iris_data_file:
        iris_data_contents = iris_data_file.read()
        # iris_data_contents = iris_data_file.read()
        
with open("myiris.pkl",'wb') as fileobj:
        pickle.dump(iris_data_contents,fileobj)

with open("myiris.pkl",'rb') as fileobj:
    print(pickle.load(fileobj))

    