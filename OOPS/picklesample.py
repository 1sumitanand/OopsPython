import pickle

test = dict({"key1": 1, "key2": 2})

with open('configfile.txt', 'wb') as pick:
    tes = pickle.dump(test, pick)

with open('configfile.txt', 'rb') as pick:
    tes = pickle.load(pick)

print(tes)