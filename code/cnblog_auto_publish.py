# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email       : lunar_ubuntu@qq.com
# > Create Time: Sat 19 Sep 2020 11:19:25 PM CST

# Automatically push articles to cnblogs.com by python xmlrpc.
import xmlrpc.client as xmlrpclib
import json
import time
import ssl
import os
import sys
# Have no idea about this line.
ssl._create_default_https_context = ssl._create_unverified_context

url = appkey = blogid = usr = passwd = ""
server = None
metablog = None
title2id = {}
recent_num = 99999
debug = True

# read configuration from json file.
def get_cfg(config):
    global url, appkey, blogid, usr, passwd, server, metablog
    with open(config, "r", encoding = "utf-8") as f:
        cfg = json.load(f)
        url = cfg["url"]
        appkey = cfg["appkey"]
        usr = cfg["usr"]
        passwd = cfg["passwd"]
    if debug:
        print("configuration: ", cfg)
    if "blogid" not in cfg:
        try:
            server = xmlrpclib.ServerProxy(url)
            userInfo = server.blogger.getUsersBlogs(
                appkey, usr, passwd)
            cfg["blogid"] = userInfo[0]["blogid"]
            blogid = userInfo[0]["blogid"]
        except:
            raise Exception("something went wrong")
        with open(config, "w", encoding = "utf-8") as f:
            json.dump(cfg, f, indent = 4, ensure_ascii = False)
    else:
        blogid = cfg["blogid"]
    if debug:
        print("configuration: ", cfg)
    if not server:
        server = xmlrpclib.ServerProxy(url)
    metablog = server.metaWeblog
    # get recent post, cause if the article is already published,
    # republish means edit.
    recent_post = metablog.getRecentPosts(cfg["blogid"], cfg["usr"], cfg["passwd"], recent_num)
    if debug:
        print("post type: ", type(recent_post[0]))
    for post in recent_post:
        # 1. transfer datetime into string
        dt = post["dateCreated"]
        post["dateCreated"] = dt.__str__()
        title2id[post["title"]] = post["postid"]
    if debug:
        print("title2id: ", title2id)

def get_newpost_id(post, publish):
    while True:
        try:
            postid = metablog.newPost(blogid, usr, passwd, post, publish)
            break
        except:
            time.sleep(5)
    return postid

def post_article(path, publish = True):
    title = os.path.basename(path) # get file name for article name.
    [title, _] = os.path.splitext(title)
    if debug:
        print("title: ", title)
    with open(path, "r", encoding = "utf-8") as f:
        post = dict(description = f.read(), title = title)
        post["categories"] = ["[Markdown]"]
        if not publish:
            pass
        else:
            # check if the article was already published
            if title in title2id.keys():
                metablog.editPost(title2id[title], usr, passwd, post, publish)
                print("Update: [title = %s][postid = %s][publish = %r]" % (title, title2id[title], publish))
                return (title, title2id[title], publish)

            else:
                postid = new_post(blogid, usr, passwd, post, publish)
                print("New: [title = %s][postid = %s][publish = %r]" % (title, title2id[title], publish))
                return (title, postid, publish)

def new_post(blogid, usr, passwd, post, publish):
    while True:
        try:
            postid = metablog.newPost(blogid, usr, passwd, post, publish)
            break
        except:
            time.sleep(5)
    return postid

if __name__ == "__main__":
    get_cfg("config.json")
    # temporarily only receive a file name as an argument.
    mdfile = sys.argv[1]
    post_article(mdfile, True)
