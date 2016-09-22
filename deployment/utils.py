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
