import feedparser
from bs4 import BeautifulSoup #导入bs4库
import urllib.request
import sys
import os
import time
import sqlite3
def parse_url(str1,file):
  data = feedparser.parse(str1)
  if os.path.exists('test.db'):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
  else:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    sql_text_1 = '''CREATE TABLE scores 
              ( ID NUMBER,
                URL TEXT);''' 
    cur.execute(sql_text_1)
  
  for entry in data.entries:
    url = entry.link
    exe2= "SELECT * FROM scores WHERE URL == " + '"'+url+'"'
    print(exe2)
    result = cur.execute(exe2)
    count = 0
    for i in result:
      print(i)
      count = count + 1
    # exe3 = "select * from scores"
    # result1 = cur.execute(exe3)
    # for i in result1:
    #   print(i)
    print(count)
    if count == 0:
      exe1 = 'INSERT INTO scores VALUES(1,"'+url+'")'
      print(exe1)
      cur.execute(exe1)
      conn.commit()
      headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
      req=urllib.request.Request(url, headers=headers)
      try:
        resp=urllib.request.urlopen(req)
      except:
        print( 'We failed to reache a server.')
      else:
        try:
          data=resp.read().decode('utf-8','ignore')
          soup = BeautifulSoup(data,'lxml')
          file.writelines("\n\n### [" +str(soup.title.get_text())+"]("+url+")")
          contentdata=soup.find_all('p', attrs={'class':'article__summary'})
          for content_i in contentdata:
            file.writelines("\n\n"+content_i)
        except:
          print("except")
        else:
           print('data get failed')


def main():
  localtime = time.localtime(time.time())
  file_name = str(localtime.tm_year)+"/"+str(localtime.tm_mon)+'-'+str(localtime.tm_mday)+".md"
  is_exists = os.path.exists(file_name)
  file=open(file_name,"a")
  if not is_exists:
    file.write("\n# "+str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday))
  url_list = open('list.txt','r').read().splitlines()
  for url in url_list:
    parse_url(url, file)
  file.close()
  if not is_exists:
    readme = open("README.md","a")
    readme.writelines("\n\n["+str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)+"]("+file_name+")")
    readme.close()
  
if __name__ == "__main__":
  main()
