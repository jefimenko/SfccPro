import os

import utils


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    user_name = 'ubuntu'
    host_name = 'ec2-52-35-185-162.us-west-2.compute.amazonaws.com'
    source_dir = BASE_DIR
    target_parent_dir = '/home/ubuntu'

    utils.rsync(user_name, host_name, source_dir, target_parent_dir, ignore=['db.sqllite3'])

    utils.remoteApache2(user_name, host_name, 'restart')
