import feedparser
from bs4 import BeautifulSoup #导入bs4库
import urllib.request
import sys
import os
import time
import sqlite3
def parse_url(str1,file):
  try:
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
      articletitle= entry.title
      exe2= "SELECT * FROM scores WHERE URL == " + '"'+url+'"'
      print(exe2)
      result = cur.execute(exe2)
      count = 0
      for i in result:
        count = count + 1
      print(count)
      if count == 0:
        exe1 = 'INSERT INTO scores VALUES(1,"'+url+'")'
        print(exe1)
        cur.execute(exe1)
        conn.commit()
        file.writelines('\n\n### ['+articletitle +']('+url+')')
  except:
    file.writelines('\n\n; error read: '+str1)
  else:
    print('parse success')

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
