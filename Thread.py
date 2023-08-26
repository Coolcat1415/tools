#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Thread.py
@Time    :   2023/08/26 16:40:12
@Author  :   Rao Guangxiang 
@Version :   1.0
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

# import threading


# def task():
#     print("任务开始")


# thread = threading.Thread(target=task)

# thread.start()

# thread.join()

# print("主线程结束")
import threading
import time


def print_num(num):
    if num == "test2":
        time.sleep(5)
    print(num)


def main():
    threads = []
    a = ["test1", "test2", "test3", "test4", "test5"]
    for i in a:
        # 创建线程对象，传递待执行的函数和参数
        t = threading.Thread(target=print_num, args=(i,))
        threads.append(t)
        # 启动线程
        t.start()

    for t in threads:
        # 等待线程执行完成
        t.join()


if __name__ == '__main__':
    main()
