import pickle

# cars=["Audi","BMW","Maruti"]

# file="mycar.pkl"

# fileobj=open(file,'wb')

# pickle.dump(cars,fileobj)

# fileobj.close

with open("mycar.pkl",'rb') as fileobj:
    print(pickle.load(fileobj))

    pickle.loads()
