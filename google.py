import urllib2

text_file = open("Output.txt", "w")
def ge():
     user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
     url='http://www.google.com/search?q=inurl:\"pages.php?id=\"&start=10&num=100'
     headers={'User-Agent':user_agent,}
     request=urllib2.Request(url,None,headers)
     response = urllib2.urlopen(request)
     html = response.read()
     text_file.write(html)
     text_file.close()


ge()
