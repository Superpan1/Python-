#微信爬虫(对爬虫限制很多) http://weixing.sougou.com/
#应对封IP，限制访问等问题
#使用代理服务器爬取网址！
#必须开启flipped代理服务器
#作者：master_g
#作品：我的第一个爬虫小程序
import urllib.request
import urllib.error
import re
import time
def use_proxy(proxy_addr,url):
	#建立异常处理机制
	try:
		req=urllib.request.Request(url)
		req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0")
		proxy=urllib.request.ProxyHandler({'http':proxy_addr})#以上三个步骤创建代理服务器缺一不可
		opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
		urllib.request.install_opener(opener)
		data=urllib.request.urlopen(req).read()
		return data
	except urllib.error.URLError as e:#URL异常
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)
			timesleep(10)
	except Exception as e:#普通异常
		print("Exception"+str(e))
		time.sleep(1)

key="Python"
proxy="127.0.0.1:8888"
for i in range(1,5):
	key=urllib.request.quote(key)
	thispageurl="http://weixin.sogou.com/weixin?type=2&query="+str(key)+"&_sug_type_=&s_from=input&_sug_=n&type=2&+page="+str(i)+"&ie=utf8"
	thispagedata=use_proxy(proxy,thispageurl)
	print(len(str(thispagedata)))
	pat1='a target="_blank" href="(.*?)"' 
	rs1=re.compile(pat1,re.S).findall(str(thispagedata))
	if(len(rs1)==0):
		print("第"+str(i)+"页没有成功")
		continue
	for j in range(0,len(rs1)):
		thisurl=rs1[j]
		thisurl=thisurl.replace("amp;","") #匹配后的网址有可能不能直接访问需要与原网址进行比较
		file="D:\python_pc\html/第"+str(i)+"页第"+str(j)+"篇文章.html"
		thisdata=use_proxy(proxy,thisurl)
		try:
			fh=open(file,"wb")
			fh.write(thisdata)
			fh.close()
			print("第"+str(i)+"页第"+str(j)+"篇文章成功")
		except Exception as e:
			print(e)
			print("第"+str(i)+"页第"+str(j)+"篇文章失败")