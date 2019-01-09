# coding: utf-8
#web1をハッシュ対応させた
#複数のurlをファイルに記述。そのファイルを利用して死活監視そしたい
import requests
import time
import subprocess
import datetime
import hash

#改ざん検知
def webtext(url):
    i=url
    nr=requests.get(i)
    nowtext=hash.hash(nr.text)
    print(deftext)
    print(nowtext)
    if nowtext != deftext:
        return('There is a possibility that this page has been tampered with.')
    else:
        return('OK')


#webページが見れるか確認
def webstatus(url):
    i=url

    try:
        rq = requests.get(i)
        if rq.status_code != 200:
            print('NO Web page')
            now=datetime.datetime.now()
            print(now)
        else:
            txt=webtext(i)
            print(txt)

    except:
        print('NO Web page!')
        now=datetime.datetime.now()
        print(now)



if __name__ == '__main__':
    inp=input('URL=>')
    r=requests.get(inp)
    deftext=hash.hash(r.text)
    while(True):
        sta=webstatus(inp)
        #print(sta)
        time.sleep(5)
