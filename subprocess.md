---
author: lunar
date: Sun 23 Aug 2020 12:04:28 AM CST
---

### Python3 subprocess

python subprocess模块允许我们启动一个新进程，并连接到它们的输入/输出/错误管道，从而获取返回值。

subprocess模块首先推荐使用的是run方法，语法格式为
```python
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
```

- args: 要执行的命令，字符串或者字符串列表
- stdin,stdout,stderr: 标准输入，输出，错误。其值可以是subprocess.PIPE或者已经存在的文件描述符
- timeout: 命令超时时间
- check: 如果设置为True，则如果进程退出状态码不为0，报CalledProcessError异常
- shell: 如果设置为True，则通过操作系统的shell执行命令

返回一个类，类中的`returncode`属性为子进程退出状态码

#### Popen() 方法

Popen是subprocess的核心，子进程的创建和管理都靠它处理。

构造函数
```python
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, 
preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, 
startupinfo=None, creationflags=0,restore_signals=True, start_new_session=False, pass_fds=(),
*, encoding=None, errors=None)
```

- bufsize: 缓冲区大小。当创建标准流的管道对象时使用，默认-1.
    - 0： 不使用缓冲区
    - 1：行缓冲
    - 正数：缓冲区大小
    - 负数： 使用系统默认缓冲区大小
- cwd: 设置子进程的当前目录
- env: 指定子进程的环境变量，为None则从父进程继承。

Popen对象方法
- poll(): 检查进程是否终止，终止则返回returncode，否则返回None
- wait(timeout): 等待子进程终止
- communicate(input, timeout): 和子进程交互，发送和读取数据
- send_signal(signal): 发送信号到子进程
- terminate(): 停止子进程,发送SIGTERM信号
- kill(): 杀死子进程，发送SIGKILL信号

