import time
from math import sin

import tensorflow as tf

writer = tf.summary.create_file_writer('./logs/run1')

with writer.as_default():
    for step in range(10):
        print(f'step: {step}')

        tf.summary.scalar('myvar', sin(step), step=step)
        writer.flush()

        time.sleep(0.1)
