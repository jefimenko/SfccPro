import os
import subprocess


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rsync(user_name, host_name, target_base_dir):
    command = ['rsync', '-azv', BASE_DIR, '{}@{}:{}'.format(user_name, host_name, target_base_dir)]
    print ' '.join(command)

    return subprocess.call(command)


def remoteMkdir(user_name, host_name, target_base_dir):
    command = ['ssh', '{}@{}'.format(user_name, host_name), 'mkdir -p {}'.format(target_base_dir.rstrip('/'))]
    print ' '.join(command)

    return subprocess.call(command)
