#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def generate_log_entry():
    return f"{generate_random_ip()} - [{datetime.datetime.now()}] \"GET /projects/260 HTTP/1.1\" {random.choice([200, 301, 400, 401, 403, 404, 405, 500])} {random.randint(1, 1024)}"

for i in range(10000):
    sleep(random.random())
    log_entry = generate_log_entry()
    sys.stdout.write(f"{log_entry}\n")
    sys.stdout.flush()
