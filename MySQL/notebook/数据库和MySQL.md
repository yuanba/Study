### 1 数据库简介

按照某种规则对数据进行收集和其他操作的一种软件

* 数据库管理系统

  DBMS存放数据的容器,完成数据的创建,读取,更新,删除等操作

* 数据库应用程序

  DBMS对用户不友好,所以我们使用应用程序作为媒介是的用户可以良好的体验到数据库的便利

### 2 MySQL细节

1. 必须要在语句后加`;`

2. 大小写不敏感

3. 基础语句

   ```mysql
   # show命令通常用来显示数据库内的信息
   show databases;    # 显示所有数据库
   show tables;    # 显示某个数据库下的所有的表
   drop database;    # 删除数据库
   drop table table_name;    # 删除表
   create database database_name;    # 创建数据库
   use database_name;    # 使用某一个数据库
   grant all privileges on database_name.* to name@localhost identified by 'xxxxxxx'     # all privileges可以替换成具体的数据库操作,亦可以对数据库的某个表加权限,创建完之后需要退出使用 mysql -u ... -p 登录就可以
   select database();    # 查看现在使用的是什么数据库
   des table_name;    # 显示建立后的表的结构

   # 建表操作
   create table table_name(
     column_name type [...] ,
     ...
   )auto_increment=n,charset=utf8;    # charset选项设定表的编码方式
   # 创建数据表的操作,制定域名和数据类型以及相应的完整性约束

   # DML插入数据和查询数据
   insert into table_name(1...) values(2...);    # 1是可选的,1如果不写的话2必须要使用建表的顺序填写数据
   select * from table_name where ... group by .... order by ... # 查询语句
   delete from table_name where ...    # 删除数据

   # 注释
   /**/
   ```

4. 基础数据库

   * mysql : 存储运行的相关信息和用户等重要信息
   * information_schema : 信息架构,管理着数据库的组成信息

5. MySQL基本的数据类型

   * 数值(unsigned属性设置无符号)
     * tinyint :-128~127
     * smallint : -32768~32767
     * mediumint : -8388608 ~ 8388607
     * int : 21亿
     * bigint
     * float : `-E^38 `~ `E^38`
     * double : `-E^308 `~ `E^308`
     * decimal : 精确计算的数据类型
   * 字符串类型   引号确认
     * char(size) : 固定长度字符串
     * varchar(size) : 可变长字符串
     * longtext : `2^64-1`可变长字符串,存储网页在再合适不过
     * tinytext : `2^8-1`可变长
     * text : `2^16-1`
     * mediumtext : `2^24-1`可变长
   * 日期类型  引号确认
     * datetime : 精确日期类型 xxxx-xx-xx xx:xx:xx
     * date : xxxx-xx-xx
   * 二进制类型
     * longblob : `2^32-1`字节
     * tinyblob : `2^8-1`
     * blob : `2^16-1`
     * mediumblob : `2^24-1`

6. MySQL基本列选项(表级完整性约束)

   * auto_increment : 

     自增序列,建表的时候制定完,可以在插入的时候插入`null`数据,默认会开始自增长建立

     auto_increment一个表只能有一个并且必须是主键

     * 数据必须是int类型(tinyint,into,smallint,longint,mediumint)
     * 列后必须要加auto_increment属性
     * 必须是唯一的,primary key或者unique限制

     删除之前的数据之后,自增长id会自动的调整

   * default 'xxx' : 设定默认值,没有默认值的NULL会被自动的转成default

   * index :定义索引

   * unique : 唯一,唯一可以是NULL

   * check : 约束

   * null / not null : 是否空,未指定默认是可以为NULL

   * primary key : 定义主键

   ```mysql
   create table people(
     name varchar(20) unique , 
     birthday datetime not null,
     age int,
     html longtext,
     id int auto_increment primary key)auto_increment=n,charset=utf8;    # 建表之后使用语句设定自增长的值

   # 设定auto_increment的两种办法
   1.就是上面的建表指定
   2.alter table table_name auto_increment = x;
   ```

### 3 SQL

1. DML数据操作语言

   select / insert / update / delete

2. DDL数据定义语言

   create / drop / alter

3. DCL数据控制语言

   grant / revoke / ...

4. 比较运算符

   * =,>,<,>=,<=,<>,IS,NOT,LIKE,BETWEEN,IN

   LIKE模糊匹配

   ```mysql
   select * from people where name like "李%"    # 查找李性同学,%类似于*,_类似与.
   ```

5. NULL的where的特殊性

   **匹配NULL的时候,我们不可以使用[=],只能使用IS操作符号**

6. selectde order by排序语句 + limit语句

   ```mysql
   select * from people order by sex ASC , birth DESC;    # ASC升序,DESC降序,NULL最小值
   # limit语句类似于Linux中的head语句
   ```

7. select group by语句 + 集函数

   * AVG
   * COUNT : count比较特殊,我们最好使用COUNT(*),否则使用具体的列count只会统计值不是NULL的数据
   * MAX
   * MIN
   * SUM

8. Select指定别名

   ```mysql
   select sex , count(mid) as total from people group by ...;
   ```

9. SQL运算符和数据库函数

   * +,-,*,DIV(DIV获取结果的整数部分),%

   * length()返回字节数 , concat(),trim(类似python的strip),rand(seed)随机数产生,extract(type from dat)抽取某一个日期具体的时间描述,datediff(dat1,dat2)时间差,MD5(获取哈希值),date_add(date , interval +/-n type)时间加运算

   * extract和date_add运算的type类型常用:year , month,day,hour,minute,second

   * case函数

     ```mysql
     # case语句首先执行第一个条件符合的when语句
     select nam,
     	case sex
     		when 条件表达式1 then ...
     		when .....     then ...
     		else ...
     	end as sex    # 重命名
     from people;
     ```

10. 多表连接查询操作

    ```mysql
    # 实例
    ```

```mysql
insert into table_name(column1 , ...) values (...);    # 后者和前者一一对应
update table_name set column1 = ,column2 = ,... where name = '...';    # 按照set之后的更新
# 对这里的update有必要说一下,我们where指定的内容实际上是杜表中所有的数据进行遍历,对where后面的表达式返回为true的数据进行更改,默认没有where全都返回true
delete from table_name where ...;
select * from table_name where ... ;  # 查询操作
```

### 4 表的更新

