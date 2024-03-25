'''
Author: nicho-UJN nicholas9698@outlook.com
Date: 2024-03-19 12:59:31
LastEditors: nicho-UJN nicholas9698@outlook.com
LastEditTime: 2024-03-19 15:19:58
FilePath: /luci-app-campusnet/getSessionId.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#Simulate sign-in to get Cookie
#Cookie expiration time is 30 minutes

import socket
import requests

def get_router_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('223.5.5.5', 53))
        ip = s.getsockname()[0]
    finally:
        s.close()
    
    return ip

routerIP = get_router_ip()
login_url = "http://139.198.3.98/sdjd/protalAction!index.action?wlanuserip="+routerIP+"&basip=124.128.40.39"
res = requests.get(login_url)
cookies_org = res.cookies
cookies = requests.utils.dict_from_cookiejar(cookies_org)
if 'JSESSIONID' in cookies:
    print(cookies["JSESSIONID"])
if 'route' in cookies:
    print(cookies["route"])