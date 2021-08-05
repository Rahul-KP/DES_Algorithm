import pickle, random

key = []
for i in range(64):
    key.append(random.choice([0, 1]))

with open('key.pkl', 'wb') as k:
    pickle.dump(key, k, pickle.HIGHEST_PROTOCOL)
