import os

import utils


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    user_name = 'ubuntu'
    host_name = 'ec2-52-35-185-162.us-west-2.compute.amazonaws.com'
    source_dir = BASE_DIR
    target_base_dir = '/home/ubuntu/SfccPro'

    utils.remoteMkdir(user_name, host_name, target_base_dir)
    utils.rsync(user_name, host_name, source_dir, target_base_dir)
