
import Queue,time

def work(q):
    while True:
        if q.empty():
            return
        else:
            t = q.get()
            print "sleep %d " % t
            time.sleep(t)

def main():
    q = Queue.Queue()
    for i in range(10):
        q.put(1)

    thread_num = 10
    threads = []
    for i in range(thread_num):
        # args需要输出的是一个元组，如果只有一个参数，后面加，表示元组，否则会报错
        t = threading.Thread(target = work, args = (q,)) 
        threads.append(t)

    for i in range(thread_num):
        threads[i].start()

    for i in range(thread_num):
        threads[i].join()