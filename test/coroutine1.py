def comsumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print("[PRODUCER] Producing %s..." % n)
        r = c.send(n)
        print("[PRODUCER] Consumer return: %s" % r)
    c.close()

c = comsumer()
produce(c)

#通过yield关键字，consumer函数将r传给了produce函数，而produce将n传给了consumer
