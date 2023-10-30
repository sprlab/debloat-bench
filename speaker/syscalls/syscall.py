import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys


def excel_to_dict(file_name):
    df = pd.read_excel(file_name)
    categories = df['category'].unique()
    result_dict = {}

    for category in categories:
        system_calls = df[df['category'] == category]['Items'].tolist()
        result_dict[category] = system_calls

    return result_dict

def file_to_list(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        lines = list(set(lines))
    return lines


def subtract_lists(list_a, list_b):
    result = list_a.copy()  # Create a copy of list_a to avoid modifying the original list
    for item in list_b:
        if item in result:
            result.remove(item)
    return result

callTable = ['read', 'write', 'open', 'close', 'stat', 'fstat', 'lstat', 'poll', 'lseek', 'mmap', 'mprotect', 'munmap', 'brk', 'rt_sigaction', 'rt_sigprocmask', 'rt_sigreturn', 'ioctl', 'pread64', 'pwrite64', 'readv', 'writev', 'access', 'pipe', 'select', 'sched_yield', 'mremap', 'msync', 'mincore', 'madvise', 'shmget', 'shmat', 'shmctl', 'dup', 'dup2', 'pause', 'nanosleep', 'getitimer', 'alarm', 'setitimer', 'getpid', 'sendfile', 'socket', 'connect', 'accept', 'sendto', 'recvfrom', 'sendmsg', 'recvmsg', 'shutdown', 'bind', 'listen', 'getsockname', 'getpeername', 'socketpair', 'setsockopt', 'getsockopt', 'clone', 'fork', 'vfork', 'execve', 'exit', 'wait4', 'kill', 'uname', 'semget', 'semop', 'semctl', 'shmdt', 'msgget', 'msgsnd', 'msgrcv', 'msgctl', 'fcntl', 'flock', 'fsync', 'fdatasync', 'truncate', 'ftruncate', 'getdents', 'getcwd', 'chdir', 'fchdir', 'rename', 'mkdir', 'rmdir', 'creat', 'link', 'unlink', 'symlink', 'readlink', 'chmod', 'fchmod', 'chown', 'fchown', 'lchown', 'umask', 'gettimeofday', 'getrlimit', 'getrusage', 'sysinfo', 'times', 'ptrace', 'getuid', 'syslog', 'getgid', 'setuid', 'setgid', 'geteuid', 'getegid', 'setpgid', 'getppid', 'getpgrp', 'setsid', 'setreuid', 'setregid', 'getgroups', 'setgroups', 'setresuid', 'getresuid', 'setresgid', 'getresgid', 'getpgid', 'setfsuid', 'setfsgid', 'getsid', 'capget', 'capset', 'rt_sigpending', 'rt_sigtimedwait', 'rt_sigqueueinfo', 'rt_sigsuspend', 'sigaltstack', 'utime', 'mknod', 'uselib', 'personality', 'ustat', 'statfs', 'fstatfs', 'sysfs', 'getpriority', 'setpriority', 'sched_setparam', 'sched_getparam', 'sched_setscheduler', 'sched_getscheduler', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_rr_get_interval', 'mlock', 'munlock', 'mlockall', 'munlockall', 'vhangup', 'modify_ldt', 'pivot_root', '_sysctl', 'prctl', 'arch_prctl', 'adjtimex', 'setrlimit', 'chroot', 'sync', 'acct', 'settimeofday', 'mount', 'umount2', 'swapon', 'swapoff', 'reboot', 'sethostname', 'setdomainname', 'iopl', 'ioperm', 'create_module', 'init_module', 'delete_module', 'get_kernel_syms', 'query_module', 'quotactl', 'nfsservctl', 'getpmsg', 'putpmsg', 'afs_syscall', 'tuxcall', 'security', 'gettid', 'readahead', 'setxattr', 'lsetxattr', 'fsetxattr', 'getxattr', 'lgetxattr', 'fgetxattr', 'listxattr', 'llistxattr', 'flistxattr', 'removexattr', 'lremovexattr', 'fremovexattr', 'tkill', 'time', 'futex', 'sched_setaffinity', 'sched_getaffinity', 'set_thread_area', 'io_setup', 'io_destroy', 'io_getevents', 'io_submit', 'io_cancel', 'get_thread_area', 'lookup_dcookie', 'epoll_create', 'epoll_ctl_old', 'epoll_wait_old', 'remap_file_pages', 'getdents64', 'set_tid_address', 'restart_syscall', 'semtimedop', 'fadvise64', 'timer_create', 'timer_settime', 'timer_gettime', 'timer_getoverrun', 'timer_delete', 'clock_settime', 'clock_gettime', 'clock_getres', 'clock_nanosleep', 'exit_group', 'epoll_wait', 'epoll_ctl', 'tgkill', 'utimes', 'vserver', 'mbind', 'set_mempolicy', 'get_mempolicy', 'mq_open', 'mq_unlink', 'mq_timedsend', 'mq_timedreceive', 'mq_notify', 'mq_getsetattr', 'kexec_load', 'waitid', 'add_key', 'request_key', 'keyctl', 'ioprio_set', 'ioprio_get', 'inotify_init', 'inotify_add_watch', 'inotify_rm_watch', 'migrate_pages', 'openat', 'mkdirat', 'mknodat', 'fchownat', 'futimesat', 'newfstatat', 'unlinkat', 'renameat', 'linkat', 'symlinkat', 'readlinkat', 'fchmodat', 'faccessat', 'pselect6', 'ppoll', 'unshare', 'set_robust_list', 'get_robust_list', 'splice', 'tee', 'sync_file_range', 'vmsplice', 'move_pages', 'utimensat', 'epoll_pwait', 'signalfd', 'timerfd_create', 'eventfd', 'fallocate', 'timerfd_settime', 'timerfd_gettime', 'accept4', 'signalfd4', 'eventfd2', 'epoll_create1', 'dup3', 'pipe2', 'inotify_init1', 'preadv', 'pwritev', 'rt_tgsigqueueinfo', 'perf_event_open', 'recvmmsg', 'fanotify_init', 'fanotify_mark', 'prlimit64', 'name_to_handle_at', 'open_by_handle_at', 'clock_adjtime', 'syncfs', 'sendmmsg', 'setns', 'getcpu', 'process_vm_readv', 'process_vm_writev', 'kcmp', 'finit_module', 'sched_setattr', 'sched_getattr', 'renameat2', 'seccomp', 'getrandom', 'memfd_create', 'kexec_file_load', 'bpf', 'execveat', 'userfaultfd', 'membarrier', 'mlock2']

file_name = 'allowed.txt'
allowed = file_to_list(file_name)
not_allowed = subtract_lists(callTable, allowed)

file_name = 'categorization.xlsx'
data_dict = excel_to_dict(file_name)

orginal_dict = {}
for key, value in data_dict.items():
    orginal_dict[key] = len(value)
orginal_dicts = dict(sorted(orginal_dict.items()))
orginal_dict = orginal_dicts
print("original: ",orginal_dict)

filtered_dict = {key: [value for value in values if value in allowed] for key, values in data_dict.items()}
print("filtered_dict: ", filtered_dict)
df = pd.DataFrame.from_dict(filtered_dict, orient='index').transpose()
df.to_excel(sys.argv[1]+'.xlsx', index=False)

debloated_dict = {}
for key, value in filtered_dict.items():
    debloated_dict[key] = len(value)

debloated_dicts = dict(sorted(debloated_dict.items()))
debloated_dict = debloated_dicts
print(debloated_dict)

diff_threshold = 0.90
keys_with_difference = []

for key in orginal_dict:
    if key in debloated_dict:
        value1 = orginal_dict[key]
        value2 = debloated_dict[key]
        percentage_diff = abs(value1 - value2) / max(value1, value2)

        if percentage_diff > diff_threshold:
            keys_with_difference.append(key)

print(keys_with_difference)

categories = list(orginal_dict.keys())
values1 = list(orginal_dict.values())
values2 = list(debloated_dict.values())

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, values1, width, label='Original')
rects2 = ax.bar(x + width/2, values2, width, label='Debloated')

ax.set_ylabel('syscalls count')
ax.set_title('Comparison of syscalls allowed for '+sys.argv[1])
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
plt.xticks(rotation=35, ha='right')
plt.margins(x=0.01, y=0.1)  # Increase bottom margin
plt.text(0.5, -0.25, "Categories which are 90% blocked: "+', '.join(keys_with_difference), transform=ax.transAxes, ha='center')

plt.tight_layout()


if len(sys.argv) > 1:
    image_name = sys.argv[1] + '.png'
    plt.savefig(image_name)
else:
    plt.savefig('barchart.png')
