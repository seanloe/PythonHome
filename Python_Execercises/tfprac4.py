
# coding: utf-8

# Tensorflow practice 4

# External Module import

# In[1]:


import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# Code section begin

# In[2]:


#add a layer
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    bias = tf.Variable(tf.zeros([1,out_size]))
    Wx_plus_b = tf.matmul(inputs, Weights)+bias
    if activation_function == None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs


# In[3]:


x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0,0.05,x_data.shape)
y_data = np.square(x_data)-0.5+noise

xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])
l1 = add_layer(xs,1,10,activation_function=tf.nn.relu)
predition = add_layer(l1,10,1,activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-predition),
                     reduction_indices=[1]))
#train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
train_step = tf.train.MomentumOptimizer(learning_rate=0.1, momentum=0.9,).minimize(loss)
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
plt.ion()
plt.show()

#training loop. Can be marked when run for tensor board
for i in range(1000):
    sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
    if i % 50 ==0:
        #print(sess.run(loss, feed_dict={xs:x_data,ys:y_data}))
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(predition, feed_dict={xs:x_data})
        lines = ax.plot(x_data,prediction_value,'r-',lw=4)
        plt.pause(0.1)


# Visualize output

# In[4]:  





