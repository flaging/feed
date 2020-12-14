import feedparser
from bs4 import BeautifulSoup #导入bs4库
import urllib.request
import sys
import os
import time
def parse_url(str1,file, file_name):
  data = feedparser.parse(str1)
  file_back_name= file_name[0:-3]+'.bk'
  file_back = open(file_back_name,"a+")
  List<String> lines = file_back.read().splitlines()
  for entry in data.entries:
    url = entry.link
    if not lines.__contains__(url):
      file_back.writelines(url+'\n')
      lines.append(url)
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
        data=resp.read().decode('ISO-8859-1')
        soup = BeautifulSoup(data,'lxml')
        file.writelines("\n\n### [" +str(soup.title.get_text())+"]("+url+")")
  file_back.close()


def main():
  localtime = time.localtime(time.time())
  file_name = str(localtime.tm_year)+"/"+str(localtime.tm_mon)+str(localtime.tm_mday)+".md"
  is_exists = os.path.exists(file_name)
  file=open(file_name,"a")
  if not is_exists:
    file.write("\n# "+str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday))
  url_list = open('list.txt','r').read().splitlines()
  for url in url_list:
    parse_url(url, file, file_name)
  file.close()
  if not is_exists:
    readme = open("README.md","a")
    readme.writelines("\n\n["+str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)+"]("+file_name+")")
    readme.close()
  

if __name__ == "__main__":
  main()
