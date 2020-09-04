---
author: lunar
date: Mon 24 Aug 2020 04:31:25 PM CST
---

### Requests库高级用法 - 会话对象

会话对象使得能够跨请求保持某些参数。它也会在同一个Session实例发出的所有请求之间保持cookie，期间使用urllib3的`connection pooling`功能。所以如果向同一台主机发送多个请求，底层的TCP连接将会被重用，带来显著的性能提升。

跨请求保持一些cookie:
```python
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'
```

