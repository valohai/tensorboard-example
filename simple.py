import tensorflow as tf
import time

tf.reset_default_graph()
myvar = tf.get_variable('myvar', shape=[])
myvar_summary = tf.summary.scalar(name='Myvar', tensor=myvar)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    writer = tf.summary.FileWriter('./logs/run1', sess.graph)
    for step in range(10):
        sess.run(init)
        summary = sess.run(myvar_summary)
        writer.add_summary(summary, step)
        print('step: %i' % step)
        time.sleep(0.1)
