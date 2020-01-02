import queue

# 创建一个队列
q = queue.Queue()

# 往队列中放数据
q.put("冯涛1")
q.put("冯涛2")


# 去队列中获取数据
v1 = q.get()
v2 = q.get()
print(v1,v2)

try:
    v3 = q.get(timeout=3)
    print(v3)
except queue.Empty as e:
    pass