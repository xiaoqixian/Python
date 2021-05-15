# !/usr/bin/python3
# -*- coding: utf-8 -*-
# > Author          : lunar
# > Email           : lunar_ubuntu@qq.com
# > Created Time    : Thu 06 May 2021 11:32:09 PM CST
# > Location        : Shanghai
# > Copyright@ https://github.com/xiaoqixian

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--address", "-d", help = "address", default = None, nargs='*')
    args = parser.parse_args()

    print(args.address)
