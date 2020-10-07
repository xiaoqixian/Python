---
author: lunar
date: Sun 23 Aug 2020 09:18:53 PM CST
---

### Python curses

Python curses 库为基于文本的终端提供了独立于终端的屏幕绘制和键盘处理功能；这些终端包括 VT100，Linux 控制台以及各种程序提供的模拟终端。显示终端支持各种控制代码以执行常见的操作，例如移动光标，滚动屏幕和擦除区域。

这个库可是专为类Unix系统提供的哦

Python 的curses库只是对于C语言同名库的简单封装

#### 开始和结束 curses应用程序

curses在使用之前必须初始化
```python
import curses
stdscr = curses.initscr()
```

该操作返回一个代表整个屏幕的窗口对象

使用 curses 的应用程序通常会关闭按键自动上屏，目的是读取按键并只在特定情况下展示它们。这需要调用函数 noecho()：
`curses.noecho()`

应用程序也会广泛地需要立即响应按键，而不需要按下回车键后执行；这被称为"cbreak"模式，与通常的缓冲输入模式相对：
`curses.cbreak()`

启用keypad 模式来应对特殊按键对应的多字节转义序列。
`stdscr.keypad(True)`

终止一个curses程序
```python
curses.nocbreak()
curses.keypad(False)
curses.echo()
curses.endwin()
```

#### 窗口和面板

一个窗口对象表示了屏幕上的一个矩形区域，并且提供方法来显示文本、擦除文本、允许用户输入字符串等等。

函数 initscr() 返回的 stdscr 对象覆盖整个屏幕。许多程序可能只需要这一个窗口，但你可能希望把屏幕分割为多个更小的窗口，来分别重绘或者清除它们。函数 newwin() 根据给定的尺寸创建一个新窗口，并返回这个新的窗口对象：
```python
begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)
```

当你调用一个方法来显示或擦除文本时，效果并不会立即显示。需要调用窗口对象的`refresh()`方法来刷新屏幕。

一个面板是一种特殊的窗口，它可以比实际的显示屏幕更大，并且能只显示它的一部分。创建面板只需要指定面板的宽和高，但刷新一个面板需要指定屏幕坐标和面板需要显示的局部。

#### 显示文字

curses提供`addstr()`之类的方法接受多种参数形式。
|形式|描述|
|----|----|
|str或ch|在当前位置显示字符串str或字符ch|
|str或ch, attr|在当前位置使用attr属性显示字符串str或字符ch|
|y,x,str或ch|移动到窗口的y,x位置，并显示str或ch|
|y,x,str或ch,attr|移动到窗口的y,x位置，使用attr属性显示字符串str或字符ch|

curses并不与一般的使用像素定位的相同，curses使用行和列进行定位。(y,x)就表示第y列，第x行。像我的1920×1080的屏幕，在全屏状态下总共有172列，43行。之所这样是因为ACSII码都只占1列，而像汉字就占两列。而两者都只占一行。所以行与列的比例与像素比例不一致。

属性允许以突出显示形态显示文本，比如加粗、下划线、反相或添加颜色。这些属性将来下一小节细说。

#### 属性和颜色

|属性|描述|
|----|----|
|A_BLINK|闪烁文字|
|A_BOLD|粗体|
|A_DIM|半明亮的文字|
|A_REVERSE|反相显示文字|
|A_STANDOUT|可用的最佳突出显示模式|
|A_UNDERLINE|带下划线的文字|

curses 库还支持在提供了颜色功能的终端上显示颜色的功能。为了使用颜色，你必须在调用完函数 initscr() 后尽快调用函数 start_color()，来初始化默认颜色集 (curses.wrapper() 函数自动完成了这一点)。 

某些非常花哨的终端可以将实际颜色定义修改为给定的 RGB 值。 这允许你将通常为红色的 1 号颜色改成紫色或蓝色或者任何你喜欢的颜色。 不幸的是，Linux 控制台不支持此特性，所以我无法尝试它，也无法提供任何示例。 想要检查你的终端是否能做到你可以调用 can_change_color()，如果有此功能则它将返回 True。 如果你幸运地拥有一个如此优秀的终端，请查询你的系统的帮助页面来了解详情。

#### 用户输入

有两个方法可以从窗口获取输入：
- `getch()`会刷新屏幕然后等待用户按键，如果之前调用过 echo() 还会显示所按的键。 你还可以选择指定一个坐标以便在暂停之前让光标移动到那里。
`getch()`方法返回一个整数；如果数值在 0 到 255 之间，它代表所按下键的 ASCII 码。 大于 255 的值为特殊键例如 Page Up, Home 或方向键等。 你可以将返回的值与 curses.KEY_PPAGE, curses.KEY_HOME 或 curses.KEY_LEFT 等常量做比较。
- `getkey()`将做同样的事但是会把整数转换为字符串。 每个字符将返回为长度为 1 个字符的字符串，特殊键例如函数键将返回包含键名的较长字符串例如 KEY_UP 或 ^G。

