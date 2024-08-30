import matplotlib.pyplot as plt

plt.scatter(bream_length, bream_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

plt.scatter(smelt)length, smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

length = bream_length(35) + smelt_length(14)
weight = bream_weight + smelt_weight

len(bream_length)
len(smelt_length)

from sklearn.neighbors import kNeighborsClassifier
kn = KNeighborsClassifier()

fish_data = []

for l, w in zip(length, weight):
    fish_data.append([l, w])

fish_target = [1] * 35 + [0] * 14

kn.fit(fish_data, fish_target)

r = kn.predict([[30.1, 600.123]])

if kn.predict([[30, 600]])[0] == 1:
    print('도미')
else:
    print('빙어')

with open("model.pkl", "rb") as f:
    fish_model = pickle.load(f)

fish_model.predict([[30.1, 600.123]])
