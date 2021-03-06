import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

num_features = 2
num_iter = 2000
display_step = int(num_iter / 10)
learning_rate = 0.1

num_input = 2
num_hidden1 = 2
num_output = 1


def multi_layer_perceptron_xor(x, weights, biases):

    hidden_layer1 = tf.add(tf.matmul(x, weights['w_h1']), biases['b_h1'])
    hidden_layer1 = tf.nn.sigmoid(hidden_layer1)

    out_layer = tf.add(tf.matmul(hidden_layer1, weights['w_out']), biases['b_out'])

    return out_layer

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], np.float32)
y = np.array([0, 1, 1, 0], np.float32)              
y = np.reshape(y, [4,1])                         

X = tf.placeholder('float', [None, num_input])
Y = tf.placeholder('float', [None, num_output])

weights = {
    'w_h1' : tf.Variable(tf.random_normal([num_input, num_hidden1])),
    'w_out': tf.Variable(tf.random_normal([num_hidden1, num_output]))
}
biases = {
    'b_h1' : tf.Variable(tf.random_normal([num_hidden1])),
    'b_out': tf.Variable(tf.random_normal([num_output]))
}


model = multi_layer_perceptron_xor(X, weights, biases)

loss_func = tf.reduce_sum(tf.nn.sigmoid_cross_entropy_with_logits(logits=model, labels=Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss_func)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for k in range(num_iter):
    tmp_cost, _ = sess.run([loss_func, optimizer], feed_dict={X: x, Y: y})
    if k % display_step == 0:
        print('loss= ' + "{:.5f}".format(tmp_cost))

W = np.squeeze(sess.run(weights['w_h1']))
b = np.squeeze(sess.run(biases['b_h1']))

sess.close()


plot_x = np.array([np.min(x[:, 0] - 0.2), np.max(x[:, 1]+0.2)])
plot_y =  -1 / W[1, 0] * (W[0, 0] * plot_x + b[0])
plot_y = np.reshape(plot_y, [2, -1])
plot_y = np.squeeze(plot_y)

plot_y2 = -1 / W[1, 1] * (W[0, 1] * plot_x + b[1])
plot_y2 = np.reshape(plot_y2, [2, -1])
plot_y2 = np.squeeze(plot_y2)

plt.plot([0,1], [0,1], 'rx')
plt.plot([0,1], [1,0], 'bx')
plt.plot(plot_x, plot_y, color='k', linewidth=2)    # line 1
plt.plot(plot_x, plot_y2, color='k', linewidth=2)   # line 2
plt.xlim([-0.2, 1.2]); plt.ylim([-0.2, 1.25]);

plt.xticks([0.0, 0.5, 1.0]); plt.yticks([0.0, 0.5, 1.0])
plt.show()

