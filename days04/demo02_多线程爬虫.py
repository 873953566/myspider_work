# -*- coding:utf-8 -*-

import requests
import random
import Queue
import threading


lock = threading.Lock()
#多个线程访问共享数据|Rlock()当前线程频繁访问自己的数据：递归

url_queue = Queue.Queue()

ua = [
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
]
user_agent = random.choice(ua)

for pageno in range(0,15):
    url_queue.put("https://tieba.baidu.com/f?kw=%E5%85%A8%E8%81%8C%E9%AB%98%E6%89%8B&ie=utf-8&pn=" + str(pageno * 50))

print url_queue.queue

def spider(urlqueue):
    while urlqueue.qsize() > 0:
        if lock.acquire():
            url = urlqueue.get()

            print '剩余数据:%s;线程%s开始对%s进行爬取' % (urlqueue.qsize(),threading.currentThread().name,url)

        headers = {
            "Referer":url,
            "User-agent":user_agent
        }
        response = requests.get(url,headers=headers)
        filename = url[-20:]+'.html'
        with open(filename,'w') as f:
            f.write(response.text.encode('utf-8'))

        #爬取结束
        print '爬取结束:对%s目标地址爬取完成' % url

        lock.release()
if __name__ == '__main__':
    #声明一个变量，保存多个线程
    threads = []
    #生命一个变量，控制启动多少个线程
    threads_num = 3
    for ct in range(0,threads_num):

        current_thread = threading.Thread(target=spider,args=(url_queue,))
        current_thread.start()
        #将线程保存在列表中
        threads.append(current_thread)
    for t in threads:
        t.join()

    print '程序运行结束.'
