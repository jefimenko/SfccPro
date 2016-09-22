import subprocess


def rsync(user_name, host_name, source_dir, target_base_dir):
    command = ['rsync', '-azv', source_dir, '{}@{}:{}'.format(user_name, host_name, target_base_dir)]
    print(' '.join(command))

    return subprocess.call(command)


def remoteMkdir(user_name, host_name, target_base_dir):
    command = ['ssh', '{}@{}'.format(user_name, host_name), 'mkdir -p {}'.format(target_base_dir.rstrip('/'))]
    print(' '.join(command))

    return subprocess.call(command)
