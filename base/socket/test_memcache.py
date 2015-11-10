import memcache, time

mc = memcache.Client(['localhost:11211'], debug=0)
mc.set("var_ever", "2000")
mc.set("var_temp", "222",1)
time.sleep (2)
value = mc.get("var_ever")
print value
value = mc.get("var_temp")
print value


#depend on python-memcached-1.54.tar.gz