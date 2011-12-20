# wsgi_longpolling/messager2.py
import time
import random

import redis

server = redis.Redis(host='localhost', port=6379, db=0)

while True:
    message = raw_input("What to say: ")
    for i in range(2000):
        server.publish('jaberwocky', message)
        server.publish('points', random.randint(0,20))
        if (i+1) % 20 == 0:
            time.sleep(1)

    if message == 'quit':
        break
