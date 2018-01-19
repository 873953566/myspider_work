#coding:utf-8

import requests,re

url = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1515722423.8200002"

headers = {
    "Referer":'http://neihanshequ.com/',
    'X-CSRFToken':'baf73baa745154754b66feec393b7623',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

num = 0
while num < 10:
    response = requests.get(url,headers=headers)

    content = response.text

    # joke_list = re.findall(r'"content": "(.*?)"', content)
    joke_list = re.findall(r'"content": "(.*?)"',content)

    print joke_list

    f = open("joke.txt",'w')
    for joke in joke_list:
        print (joke.decode("unicode-escape"))
        f.write(joke.decode("unicode-escape").encode("utf-8"))
        f.write("\r\n########################################\r\n")

    f.close()
    num +=1