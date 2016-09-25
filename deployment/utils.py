import os
import subprocess


def rsync(user_name, host_name, source_dir, target_parent_dir, ignore=[]):
    command = ['rsync', '-azv', source_dir, '{}@{}:{}'.format(user_name, host_name, target_parent_dir)]
    for file_or_dir in ignore:
        command.insert(2, '--exclude={}'.format(file_or_dir))
    print(' '.join(command))

    return subprocess.call(command)

def remoteMkdir(user_name, host_name, target_dir):
    command = ['ssh', '{}@{}'.format(user_name, host_name), 'mkdir -p {}'.format(target_dir.rstrip('/'))]
    print(' '.join(command))

    return subprocess.call(command)

def collectStatic():
    command = ['python', os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'manage.py'), 'collectstatic']
    print(' '.join(command))

    subprocess.call(command)

def remoteApache2(user_name, host_name, apache2_command):
    command = ['ssh', '{}@{}'.format(user_name, host_name), 'sudo service apache2 {}'.format(apache2_command)]
    print(' '.join(command))

    subprocess.call(command)
