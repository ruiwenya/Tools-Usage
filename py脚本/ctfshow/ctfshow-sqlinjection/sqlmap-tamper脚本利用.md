#### sqlmap tamper脚本备忘录

#### sqlmap tamper 脚本编写





#### https://blog.csdn.net/solitudi/article/details/110144623     y4taker博客

#### https://blog.csdn.net/rfrder/article/details/113759746?spm=1001.2014.3001.5501 fengji博客





```shell
链接  https://www.cnblogs.com/junsec/p/11607603.html

2019.9更新后翻译

* apostrophemask.py-用其UTF-8全角字符替换撇号（'）（例如'->％EF％BC％87）
* apostrophenullencode.py-用非法的双unicode替换撇号（'）（例如'->％00％27）
* appendnullbyte.py-在有效载荷的末尾附加（访问）NULL字节字符（％00）
* base64encode.py-Base64对给定有效载荷中的所有字符进行编码
* between.py- 替换较大比运算符（'>'）带有'NOT BETWEEN 0 AND＃'，等于运算符（'='）与'BETWEEN＃AND＃'
* bluecoat.py-用有效的随机空白字符替换SQL语句后的空格字符。然后用运算符LIKE替换字符'='
* chardoubleencode.py-双重URL编码给定有效负载中的所有字符（未处理已编码）（例如SELECT->％2553％2545％254C％2545％2543％2554）
* charencode.py-URL编码中的所有字符给定的有效载荷（不处理已经编码的）（例如SELECT->％53％45％4C％45％43％54）
* charunicodeencode.py-Unicode-URL编码给定的有效载荷中的所有字符（不处理已经编码的）（例如SELECT->％u0053％u0045％u004C％u0045％u0043％u0054）
* charunicodeescape.py-Unicode转义给定有效负载中的未编码字符（未处理已编码的字符）（例如SELECT-> \ u0053 \ u0045 \ u004C \ u0045 \ u0043 \ u0054）
* commalesslimit.py-用'LIMIT N OFFSET M'替换（MySQL）实例，例如'LIMIT M，N'
* commalessmid.py-用'MID（A FROM B FOR C）'替换（MySQL）实例，例如'MID（A，B，C）'
* commentbeforeparentheses.py-在括号前加（内联）注释（例如（（-> / ** /（）
* concat2concatws.py-用'CONCAT_WS（MID（CHAR（0），0，0），A，B）' 等价物（相当于）替换（MySQL）实例，例如'CONCAT（A，B）' 。
* equaltolike.py- 将所有出现的等于（'='）运算符替换为'LIKE'
* escapequotes.py-斜杠转义单引号和双引号（例如'-> \'）
* great.py- 替换大于运算符（'>' ）和'GREATEST'对应
* Halfversionedmorekeywords.py-在每个关键字
* hex2char.py-替换每个（MySQL）0x等效的CONCAT（CHAR（），...）编码字符串
* htmlencode.py-HTML编码（使用代码点）所有非字母数字字符（例如'->'）
* ifnull2casewhenisnull.py-替换'IFNULL（ A，B）'与'CASE WHEN ISNULL（A）THEN（B）ELSE（A）END'对应
* ifnull2ifisnull.py-用'IF（ISNULL（A），B）替换'IFNULL（A，B）'之类的实例，A）'对应
* informationschemacomment.py-在所有出现的（MySQL）“ information_schema”标识符的末尾添加一个内联注释（/ ** /）
* least.py 用'LEAST'对应替换大于运算符（'>'）
* lowercase.py-用小写值替换每个关键字字符（例如SELECT->选择）
* luanginx.py-LUA-Nginx WAF绕过（例如Cloudflare）
* modsecurityversioned.py-包含带有（MySQL）版本注释的完整查询
* modsecurityzeroversioned.py-包含带有（MySQL）零版本注释的完整查询
* multiplespaces.py-在SQL关键字周围添加多个空格（''）
* overlongutf8.py-将给定有效载荷中的所有（非字母数字）字符转换为超长UTF8（未处理已编码）（例如'->％C0％A7）
* overlongutf8more.py-将给定有效载荷中的所有字符转换为超长UTF8（尚未处理编码）（例如SELECT->％C1％93％C1％85％C1％8C％C1％85％C1％83％C1％94）
* percent.py-在每个字符前面添加一个百分号（'％'） （例如SELECT->％S％E％L％E％C％T）
* plus2concat.py-替换加号运算符（'+'）与（MsSQL）函数CONCAT（）对应
* plus2fnconcat.py-用（MsSQL）ODBC函数{fn CONCAT（）}替换加号（'+'）对应项
* randomcase.py-用随机大小写值替换每个关键字字符（例如SELECT-> SEleCt）
* randomcomments.py -在SQL关键字内添加随机内联注释（例如SELECT-> S / ** / E / ** / LECT）
* sp_password.py-将（MsSQL）函数'sp_password'附加到有效负载的末尾，以便从DBMS日志中自动进行混淆
* space2comment.py-用注释'/ ** /' 替换空格字符（''）
* space2dash.py-用短划线注释（'-'）替换空格字符（''），后跟一个随机字符串和一个新的行（'\ n'）
* space2hash.py-用井字符（'＃'）替换（MySQL）空格字符（''）实例，后跟随机字符串和换行（'\ n'）
* space2morecomment.py-替换（MySQL）带注释'/ ** _ ** /' 的空格字符（''）实例
* space2morehash.py-用井号（'＃'）后面跟一个随机字符串替换（MySQL）空格字符（''）实例和新行（'\ n'）
* space2mssqlblank.py-用有效的替代字符集中的随机空白字符替换空间字符（''）的（MsSQL）实例
* space2mssqlhash.py-替换空间字符（'' ）和井号（'＃'），后接换行（'\ n'）
* space2mysqlblank.py-用有效替代字符集中的随机空白字符替换（MySQL）空格字符（''）实例
* space2mysqldash.py-用破折号（'-'）替换空格字符（''） ）后跟换行（'\ n'）
* space2plus.py-用加号（'+'）替换空格字符（''）
* space2randomblank.py-用空格中的随机空白字符替换空格字符（''）有效的替代字符集
* substring2leftright.py-用LEFT和RIGHT替换PostgreSQL SUBSTRING
* symbolicologic.py-用其符号对应物（&&和||）替换AND和OR逻辑运算符
* unionalltounion.py-用UNION SELECT对应项替换UNION ALL SELECT的实例
* unmagicquotes.py-用多字节组合％BF％27替换引号字符（'），并在末尾添加通用注释（以使其起作用）
* uppercase.py-用大写值替换每个关键字字符（例如select -> SELECT）
* varnish.py-附加HTTP标头'X-originating-IP'以绕过Varnish防火墙
* versionedkeywords.py-用（MySQL）版本注释将每个非功能性关键字括起来
* versionedmorekeywords.py-将每个关键字包含（MySQL）版本注释
* xforwardedfor.py-附加伪造的HTTP标头'X-Forwarded-For'
```



```shell
https://blog.csdn.net/rfrder/article/details/113759746?spm=1001.2014.3001.5501


space2comment.py用/**/代替空格

apostrophemask.py用utf8代替引号

equaltolike.pylike代替等号

space2dash.py　绕过过滤‘=’ 替换空格字符（”），（’–‘）后跟一个破折号注释，一个随机字符串和一个新行（’n’）

greatest.py　绕过过滤’>’ ,用GREATEST替换大于号。

space2hash.py空格替换为#号,随机字符串以及换行符

apostrophenullencode.py绕过过滤双引号，替换字符和双引号。

halfversionedmorekeywords.py当数据库为mysql时绕过防火墙，每个关键字之前添加mysql版本评论

space2morehash.py空格替换为 #号 以及更多随机字符串 换行符

appendnullbyte.py在有效负荷结束位置加载零字节字符编码

ifnull2ifisnull.py　绕过对IFNULL过滤,替换类似’IFNULL(A,B)’为’IF(ISNULL(A), B, A)’

space2mssqlblank.py(mssql)空格替换为其它空符号

base64encode.py　用base64编码替换

space2mssqlhash.py　替换空格

modsecurityversioned.py过滤空格，包含完整的查询版本注释

space2mysqlblank.py　空格替换其它空白符号(mysql)

between.py用between替换大于号（>）

space2mysqldash.py替换空格字符（”）（’ – ‘）后跟一个破折号注释一个新行（’ n’）

multiplespaces.py围绕SQL关键字添加多个空格

space2plus.py用+替换空格

bluecoat.py代替空格字符后与一个有效的随机空白字符的SQL语句,然后替换=为like

nonrecursivereplacement.py双重查询语句,取代SQL关键字

space2randomblank.py代替空格字符（“”）从一个随机的空白字符可选字符的有效集

sp_password.py追加sp_password’从DBMS日志的自动模糊处理的有效载荷的末尾

chardoubleencode.py双url编码(不处理以编码的)

unionalltounion.py替换UNION ALLSELECT UNION SELECT

charencode.py　url编码

randomcase.py随机大小写

unmagicquotes.py宽字符绕过 GPCaddslashes

randomcomments.py用/**/分割sql关键字

charunicodeencode.py字符串 unicode 编码

securesphere.py追加特制的字符串

versionedmorekeywords.py注释绕过

space2comment.py替换空格字符串(‘‘) 使用注释‘/**/’

halfversionedmorekeywords.py关键字前加注释
```





tamper脚本编写

```python
链接		https://y4er.com/post/sqlmap-tamper/

#!/usr/bin/env python

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

from lib.core.enums import PRIORITY
__priority__ = PRIORITY.LOW # 当前脚本调用优先等级

def dependencies(): # 声明当前脚本适用/不适用的范围，可以为空。
    pass

def tamper(payload, **kwargs): # 用于篡改Payload、以及请求头的主要函数
    return payload


分为了import部分、__priority__ 属性、dependencies函数、tamper函数以及用户自定义的函数


#!/usr/bin/env python

"""
Copyright (c) 2006-2019 sqlmap developers (http://sqlmap.org/)
See the file 'LICENSE' for copying permission
"""

import random

from lib.core.compat import xrange
from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def randomIP():
    numbers = []

    while not numbers or numbers[0] in (10, 172, 192):
        numbers = random.sample(xrange(1, 255), 4)

    return '.'.join(str(_) for _ in numbers)

def tamper(payload, **kwargs):
    """
    Append a fake HTTP header 'X-Forwarded-For'
    """

    headers = kwargs.get("headers", {})
    headers["X-Forwarded-For"] = randomIP()
    headers["X-Client-Ip"] = randomIP()
    headers["X-Real-Ip"] = randomIP()
    return payload



import
这一部分我们可以导入sqlmap的内部库，sqlmap为我们提供了很多封装好的函数和数据类型，比如下文的PRIORITY就来源于sqlmap/lib/core/enums.py


PRIORITY
PRIORITY是定义tamper的优先级，PRIORITY有以下几个参数:

LOWEST = -100
LOWER = -50
LOW = -10
NORMAL = 0
HIGH = 10
HIGHER = 50
HIGHEST = 100
如果使用者使用了多个tamper，sqlmap就会根据每个tamper定义PRIORITY的参数等级来优先使用等级较高的tamper，如果你有两个tamper需要同时用，需要注意这个问题。



编写tamper来双写绕过
def tamper(payload, **kwargs):
    payload = payload.lower()
    payload = payload.replace('select','seleselectct')
    payload = payload.replace('union','ununionion')
    return payload

没有使用tamper之前，我们加上--tech=U来让sqlmap只测试联合查询注入，--flush-session意思是每次刷新会话，清理上次的缓存。



基于http头
我们使用sqlmap\tamper\xforwardedfor.py的tamper来讲解

def tamper(payload, **kwargs):
    """
    Append a fake HTTP header 'X-Forwarded-For'
    """

    headers = kwargs.get("headers", {})
    headers["X-Forwarded-For"] = randomIP()
    headers["X-Client-Ip"] = randomIP()
    headers["X-Real-Ip"] = randomIP()
    return payload

从kwargs中取出headers数组，然后修改了xff值达到随机IP的效果
```

