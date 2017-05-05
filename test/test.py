# -*- coding: utf-8 -*-

#http://blog.csdn.net/zhaoxinfan/article/details/8656992
  
import urllib2  
import re  
  
#------------------------------------------------------------------------------  
def crawl(keyword_name):  
    a = keyword_name;  
      
    output.write(a+"\t");  
      
    for year in range(2016,2017):  
        for month in range(1,13):  
            begintime=str(year)+"-"+"%02d"%month+"-01";  
            endtime=str(year)+"-"+"%02d"%month+"-31";  
            print begintime,endtime;          
            userMainUrl="http://search.sina.com.cn/?time=custom&stime="+begintime+"&etime="+endtime+"&c=news&q="+a+"&sort=time&range=title";  
            print userMainUrl;  
            req = urllib2.Request(userMainUrl);  
            resp = urllib2.urlopen(req);  
            respHtml = resp.read(); 
         
            #<div class="l_v2">找到相关新闻224篇</div>
            urlpat = re.compile(r'<div class="l_v2">(.*?)</div>');   
            match = urlpat.findall(respHtml);
            print match; 
         
            for numstr in match:  
            	searchnum = numstr[12:-2];  
            	print "searchnum=",searchnum;  
            	output.write(searchnum+"\t");  
                    
    output.write("\r\n");  
  
  
###############################################################################  
if __name__=="__main__":  
    with open('input.txt', 'r') as fp:  
        output = open('output.txt', 'a');  
        for line in fp:  
            keyword = line.strip();  
            crawl(keyword);  
        output.close();       
