#python env:/bin/lib/python3.8
#!------------utf8------------
# > Author     : lunar
# > Mail       : lunar_ubuntu@qq.com
# > Create Time: Sat 18 Jul 2020 09:50:24 PM CST

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

if __name__ == '__main__':
    app.run()
