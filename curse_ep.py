# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email       : lunar_ubuntu@qq.com
# > Create Time: Sun 23 Aug 2020 07:12:10 PM CST

#-*- coding: UTF-8 -*-
import curses

stdscr = curses.initscr()

def display_info(str, x, y, colorpair=2):
    '''''使用指定的colorpair显示文字'''
    global stdscr
    stdscr.addstr(y, x,str, curses.color_pair(colorpair))
    stdscr.refresh()

def display_list():
    global stdscr
    stdscr.addstr(10, 8, "歌曲搜索列表", curses.color_pair(1))
    global lst
    lst = [
            "1. Smooth Criminal",
            "2. lemon",
            "3. 江南",
            "4. break my heart"
          ]
    stdscr.addstr(11, 8, lst[0], curses.color_pair(3))
    for i in range(1, len(lst)):
        stdscr.addstr(11+i, 8, lst[i], curses.color_pair(4))
    stdscr.refresh()

def get_ch_and_continue():
    '''''演示press any key to continue'''
    global stdscr
    global lst
    #设置nodelay，为0时会变成阻塞式等待
    stdscr.nodelay(0)
    start = 0
    while True:
        ch = stdscr.getch()
        if ch == ord('q'):
            return True
        elif ch == ord('j'):
            stdscr.addstr(11+start, 8, lst[start], curses.color_pair(4))
            start += 1
            stdscr.addstr(11+start, 8, lst[start], curses.color_pair(3))
        elif ch == ord('k'):
            stdscr.addstr(11+start, 8, lst[start], curses.color_pair(4))
            start -= 1
            stdscr.addstr(11+start, 8, lst[start], curses.color_pair(3))
    #重置nodelay,使得控制台可以以非阻塞的方式接受控制台输入，超时1秒
    stdscr.nodelay(1)
    return True

def set_win():
    '''''控制台设置'''
    global stdscr
    #使用颜色首先需要调用这个方法
    curses.start_color()
    #文字和背景色设置，设置了两个color pair，分别为1和2
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
    #关闭屏幕回显
    curses.noecho()
    #输入时不需要回车确认
    curses.cbreak()
    #设置nodelay，使得控制台可以以非阻塞的方式接受控制台输入，超时1秒
    stdscr.nodelay(1)

def unset_win():
    '''控制台重置'''
    global stdstr
    #恢复控制台默认设置（若不恢复，会导致即使程序结束退出了，控制台仍然是没有回显的）
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    #结束窗口
    curses.endwin()
if __name__=='__main__':
    try:
        set_win()
        display_list()
        get_ch_and_continue()
    except Exception as e:
        raise e
    finally:
        unset_win()
