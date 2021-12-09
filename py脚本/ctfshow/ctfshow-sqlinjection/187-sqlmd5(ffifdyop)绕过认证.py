'''$sql = "SELECT * FROM admin WHERE pass = '".md5($password,true)."'";
将密码转换成16进制的hex值以后，再将其转换成字符串后包含’ ‘or ’ 6’

SELECT * FROM admin WHERE pass=’ ‘or ’ 6’
很明显可以注入了
难点就在如何寻找这样的字符串，网上有
提供两个字符串： ffifdyop、129581926211651571912466741651878684928
但题目有长度限制，所以输入ffifdyop即可获取flag
再转成字符串:’ ’ ‘or’ 6
解析:存在 or 即代码的两边有一边为真既可以绕过，其实为垃圾代码没有任何用的。
or 后面有6，非零值即为真。既可以成功绕过。


在mysql里面，在用作布尔型判断时，以1开头的字符串会被当做整型数。
要注意的是这种情况是必须要有单引号括起来的，比如password=‘xxx’ or ‘1xxxxxxxxx’
那么就相当于password=‘xxx’ or 1 ，也就相当于password=‘xxx’ or true，所以返回值就是true。
当然在后来测试中发现，不只是1开头，只要是数字开头都是可以的。
当然如果只有数字的话，就不需要单引号，比如password=‘xxx’ or 1，那么返回值也是true。（xxx指代任意字符）

'''

