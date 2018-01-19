# -*- coding:utf-8 -*-

import requests
import re,random

ua = [
    "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0;",
    "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
]

user_agent = random.choice(ua)

my_header = {
    "Cookie":'ll="118237"; bid=a6BgWF76HAQ; __utmz=30149280.1515589089.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=vKYE4qqDJYBPfEiyi7WBr7Iauxj5oH60; _vwo_uuid_v2=D05C8933B32568F2E72E2BEEFACDD127|7a7d410b36421532c978f1adf1af5338; ap=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1515632524%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_spt%3D1%26rsv_iqid%3D0xcaec990c000327dc%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D4%26rsv_sug1%3D2%26rsv_sug7%3D101%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1739501385.1515589089.1515589089.1515632524.2; __utmb=30149280.0.10.1515632524; __utmc=30149280; __utma=223695111.456818446.1515589089.1515589089.1515632524.2; __utmb=223695111.0.10.1515632524; __utmc=223695111; __utmz=223695111.1515632524.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; _pk_id.100001.4cf6=f2fca1389774d330.1515589089.2.1515635112.1515592400',
    "Referer":'https://movie.douban.com/explore'

}
num = raw_input("请输入想爬取页数:")

for i in range(0,20 * int(num),20):
    params = {
        'type':'movie',
        'tag':'热门',
        'sort':'recommend',
        'page_limit':20,
        'page_start':i,
    }
    url = ""
