import urllib2
import re

text_file = open("Output.txt", "r")
r=open("urls.txt","a")
def ge():
     check=text_file.read()
     p=re.compile(r'\bhref="/url\?q=https?://(?!webcache)\S+"')
     result=p.findall(check)
     p=re.compile(r'\bq=\S+&amp;sa')
     refine=' '.join(result)
     result=p.findall(refine)
     it=0
     for i in result:
          result[it]=i.strip(r'q=&amp;sa')
          r.write(urllib2.unquote(result[it])+"\n")
          it=it+1
     text_file.close()
     
     

ge()
