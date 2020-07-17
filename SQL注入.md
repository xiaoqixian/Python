
### **SQL注入**

所谓SQL注入，就是通过把SQL命令插入到Web表单提交或输入域名或页面请求的查询字符串，最终达到欺骗服务器执行恶意的SQL命令。具体来说，它是利用现有应用程序，将（恶意的）SQL命令注入到后台数据库引擎执行的能力，它可以通过在Web表单中输入（恶意）SQL语句得到一个存在安全漏洞的网站上的数据库，而不是按照设计者意图去执行SQL语句。

如果使用普通的字符串拼接来构成一个SQL命令，则有可能会出现下面这种情况：

```SQL
strSQL = "SELECT * FROM users WHERE name = '" + userName + "' and pw = '"+ passWord +"';"
```

如果恶意填入：
```java
userName = "1' OR '1' == '1";
passWord = "1' OR '1' == '1";
```

则最终语句变成了：
```SQL
strSQL = "SELECT * FROM users WHERE name = '1' OR '1'='1' and pw = '1' OR '1'='1';"
```

所以WHERE条件恒为真，这就相当于执行：
```SQL
strSQL = "SELECT * FROM users;"
```
于是可以达到无账号密码登录。

#### **Java PreparedStatement**

```java
String sql = “insert into user (name,pwd) values(?,?)”;  
PreparedStatement ps = conn.preparedStatement(sql);  
ps.setString(1, “jack”);   //占位符顺序从1开始
ps.setString(2, “123456”); //也可以使用setObject
ps.executeQuery();
```
对于上述代码，在原始SQL语句中通过'?'进行占位，然后通过`setString`的方式将真正的值填进去。
