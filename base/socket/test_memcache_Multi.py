import memcache, time

mc = memcache.Client(['localhost:11211','localhost:11212','localhost:11213'], debug=0)
mc.set("key1","value1")
mc.set("key2","value2")
mc.set("key3","value3")
mc.set("key4","value4")
time.sleep (2)
print mc.get("key1")
print mc.get("key2")
print mc.get("key3")
print mc.get("key4")

#depend on python-memcached-1.54.tar.gz