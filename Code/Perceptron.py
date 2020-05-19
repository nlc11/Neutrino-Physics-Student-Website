import matplotlib.pyplot as plt
import numpy as np

def predict(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i+1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0

def train_weights(train, l_rate, n_epoch):
    weights = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        sum_error = 0.0
        for row in train:
            prediction = predict(row, weights)
            error = row[-1] - prediction
            sum_error += error**2
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row)-1):
                weights[i+1] = weights[i+1] + l_rate * error *row[i]
        print(">epoch=%d, lrate=%.3f, error=%.3f" % (epoch, l_rate, sum_error))
    return weights

dataset = [[3.7,2.0,0],
[2.4,-2.3,0],
[3.3,4.4,0],
[1.3,-4.8,0],
[1.0,3.0,0],
[5.6,8.7,1],
[4.3,9.0,1],
[6.9,1.7,1],
[7.6,-1.2,1],
[6.6,3.5,1]]
l_rate=0.1
n_epoch = 100
weights = train_weights(dataset, l_rate, n_epoch)
print(weights)

for row in dataset:
	prediction = predict(row, weights)
	print("Expected=%d, Predicted=%d" % (row[-1], prediction))

plt.figure(1)
for i in dataset:
    c = "co" if i[2]==0 else "mo"
    plt.plot(i[0], i[1], c)

x = np.linspace(1, 8, 100)

m = -(weights[0]/weights[2])/(weights[0]/weights[1])
c = -weights[0]/weights[2]

plt.plot(x, m*x+c, "k")
plt.show()