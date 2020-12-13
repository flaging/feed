import feedparser
from bs4 import BeautifulSoup #导入bs4库
import urllib.request
import sys
import os
import time
def parse_url(str,file):
  data = feedparser.parse(str)
  
  for entry in data.entries:
    url = entry.link
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req=urllib.request.Request(url, headers=headers)
    try:
      resp=urllib.request.urlopen(req)
    except (urllib.HTTPError,e):
      print('Error code:', e.code)
    except (urlllib.URLError, e):
      print( 'We failed to reache a server.')
      print('Reason:', e.reason)
    else:
      data=resp.read().decode('utf-8')
      soup = BeautifulSoup(data,'lxml')
      file.writelines("\n\n### [" +str(soup.title.get_text())+"]("+url+")")


def main():
  localtime = time.localtime(time.time())
  file_name = str(localtime.tm_year)+"/"+str(localtime.tm_mon)+str(localtime.tm_mday)+".md"
  file=open(file_name,"a")
  file.write("\n# "+str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday))
  url_list = ['http://export.arxiv.org/rss/cs.AR','http://120.53.237.72:1200/weibo/user/6134470959']
  for url in url_list:
    parse_url(url, file)
  file.close()
  readme = open("README.md","a")
  readme.writelines("\n\n["+str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)+"]("+file_name+")")
  readme.close()
  

if __name__ == "__main__":
  main()
