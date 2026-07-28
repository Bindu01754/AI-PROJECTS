import numpy as np
arr = np.array([10,25,3,15,45])
minimum = np.min(arr)
maximum = np.max(arr)
print("Minimum value:",minimum)
print("Maximum vale:",maximum)



import pandas as pd
data={
    "Name":["Alice","Bob","Charlie"],
    "Age":[20,21,22],
    "Marks":[85,90,88]
}
df = pd.DataFrame(data)
print(df)

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.title("line graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

from sklearn.tree import DecisionTreeClassifier

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[2]]))