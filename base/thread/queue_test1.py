
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
    q = Queue.Queue()   # 初始化一个Queue对象
    for i in range(5): # 向Queue生产任务
        q.put(2)

    work(q)

if __name__ == "__main__":
    main() 