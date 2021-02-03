import os
import shutil
import time
from math import sin

import tensorflow as tf


def create_incremental_log_dir(path):
    """Creates a log directory and returns the path"""
    i = 1
    result = f'{path}_{i}'
    while os.path.exists(result):
        i = i + 1
        result = f'{path}_{i}'
    os.makedirs(result)
    return result


def create_valohai_log_snapshot(logs_path, outputs_path):
    """Uploads a snapshot of logs to Valohai"""
    for filename in os.listdir(logs_path):
        log_file = os.path.join(logs_path, filename)

        # Append current time to log filename to make it unique and sortable
        output_file = os.path.join(outputs_path, filename)

        # Move log file to Valohai outputs folder to be saved
        shutil.copy2(log_file, output_file)

        # Change the log file to read-only
        # causing Valohai to upload the file immediately
        # instead of at the end of the execution
        os.chmod(output_file, 292)


# Get Valohai outputs directory path
# which is by default /valohai/outputs
valohai_outputs_path = os.getenv('VH_OUTPUTS_DIR')
is_running_in_valohai = True if valohai_outputs_path else False

logs_path = create_incremental_log_dir(os.path.join('logs', 'local'))

for step in range(10):
    print(f'step: {step}')

    writer = tf.summary.create_file_writer(logs_path)
    with writer.as_default():
        # Save a data point for myvar at the current step
        # with value sin(step) to plot something in our chart
        tf.summary.scalar('myvar', sin(step), step=step)
        writer.flush()

        if is_running_in_valohai:
            create_valohai_log_snapshot(logs_path, valohai_outputs_path)

        writer.close()

    time.sleep(1)
