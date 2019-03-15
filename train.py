import tensorflow as tf
import numpy as np
import shutil
import os
import time

def create_valohai_log_snapshot(file_writer):
    from_path = file_writer.get_logdir()
    to_path = os.getenv('VH_OUTPUTS_DIR')
    if not os.path.exists(to_path):
        os.makedirs(to_path)

    file_writer.close()
    for filename in os.listdir(from_path):
        shutil.move(from_path + os.sep + filename, to_path + os.sep + filename)
        os.chmod(to_path + os.sep + filename, 292)
    file_writer.reopen()

def create_incremental_folder(path):
    result = path + '_1'
    i = 0
    while os.path.exists(result):
        i += 1
        result = path + '_%i' % i
    os.makedirs(result)
    return result

valohai = True if os.getenv('VH_OUTPUTS_DIR') else False
tf.reset_default_graph()
myvar = tf.get_variable('myvar', shape=[])
myvar_summary = tf.summary.scalar(name='Myvar', tensor=myvar)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    writer = tf.summary.FileWriter(create_incremental_folder('logs' + os.sep + 'local'), sess.graph)
    for step in range(10):
        sess.run(init)
        summary = sess.run(myvar_summary)
        writer.add_summary(summary, step)
        if valohai:
            create_valohai_log_snapshot(writer)
        print('step: %i' % step)
        time.sleep(1)