import sys, os, re, socket, random
from threading import Thread
from time import sleep
import requests
from requests.auth import HTTPDigestAuth
from decimal import *

ips = open(sys.argv[1], "r").readlines()
motherthreads = int(sys.argv[2]) #2-1000
motherthread_count = len(ips) / motherthreads
motherthread_chunks = [ips[x:x+motherthread_count] for x in xrange(0, len(ips), motherthread_count)]

lol = ["18.141.53.197", "142.93.228.111", "178.238.231.155"]

def dump(count):
	count = int(count)
	for i in motherthread_chunks[count]:
		try:
                        i = i.strip("\n")
                        oof = random.choice(lol)
                        r = requests.get("http://"+oof+":3001/api/addr/"+i+"/?noTxList=1", timeout=12)
                        #print(r.text)        
                        if "addrStr" in r.text:
			   print(r.text)
                           file = open("balances.txt", "a+")
                           file.write(r.text+"\n")
                           file.close()
                           motherthread_chunks[count] = motherthread_chunks[count].remove(i)
			   sock.close()
                           time.sleep(0.001)                        

		except:
			pass

for x in xrange(motherthreads):
	try:
		thread = Thread(target=dump, args=(x,))
		thread.start()
	except KeyboardInterrupt:
		sys.exit("STOPPING!")
	except:
		pass
