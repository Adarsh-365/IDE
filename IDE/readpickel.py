import pickle
import os

if os.path.getsize("data.pickle") > 0:
    with open("data.pickle", 'rb') as f:
        pik = pickle.load(f)
    print(pik)
else:
    print("data.pickle is empty.")