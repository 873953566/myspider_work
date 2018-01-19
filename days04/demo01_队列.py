# -*- coding:utf-8 -*-

import Queue
# 1. 常规队列LILO队列【FIFO】
q1 = Queue.Queue()

q1.put('a')
q1.put('b')
q1.put('c')
q1.put('d')
q1.put('e')

print q1.queue,q1.qsize()

q1.get()
q1.get()
q1.get()
print q1.queue,q1.qsize()

print '#####################################'
# 2. 栈队列_LIFO
q2 = Queue.LifoQueue()

q2.put('1')
q2.put('2')
q2.put('3')
q2.put('4')
q2.put('5')
q2.put('6')
print q2.queue,q2.qsize()
q2.get()
q2.get()
q2.get()
q2.get()
print q2.queue,q2.qsize()

print '#####################################'
# 3.优先队列：添加的数据在提取时符合一定的优先规则
q3 = Queue.PriorityQueue()

# 4.两端队列
q4 = Queue.deque()
q4.append('1')
q4.append('2')
q4.append('3')
q4.append('4')
q4.append('5')
q4.append('6')
q4.appendleft('a')
q4.appendleft('b')
q4.appendleft('c')
q4.appendleft('d')
q4.appendleft('e')
print '#'*10
print q4
q4.pop()
q4.pop()
q4.pop()
print '#'*10
print q4
q4.popleft()
q4.popleft()
q4.popleft()
print '#'*10
print q4







