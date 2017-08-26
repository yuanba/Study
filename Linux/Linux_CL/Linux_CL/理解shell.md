### 父子进程的概念

进程可以理解成是正在运行的程序,子进程汇集成父进程中的部分变量和环境但是无法影响到父进程的环境

```bash
ps -al --forest    # 可以快速的查看我们的进程关系
```

#### bash启动方式

```bash
bash -c string    # 从字符串中接受不启动新的bash
bash -r    # 启动受限制的bash
```

#### 进程列表

```bash
# ()可以创建子进程,在子进程中运行括号内运行指定命令组
# {}不启动子进程,在当前组内运行命令,但是该方式使用的时候必须严格按照排版 { command; }两个空格和分号一个都不能少
```

#### BASH_SUBSHELL环境变量

1. 该环境变量记录当前的bash shell的子进程层级,0是最高父进程,1,2,...

2. ```bash
   echo $$    # 输出当前的bash shell的PID
   ```

#### 子shell和后台运行

1. 子shell的进程会使得父进程阻塞,暂停CLI的交互执行

2. 后台运行可以让父进程停止对子进程的阻塞(目前理解)

   ```bash
   sleep &
   jobs -l    # jobs可以查看后台程序状态,-l参数可以显示PID 
   ```

3. 进程列表 + 后台运行

   后台运行可以讲进程列表的子进程在后台执行并放弃父进程的阻塞,空余出父进程的CLI

   ```bash
   (sleep 10) &   # 父进程开启子进程并且停止阻塞
   (sleep 10 &)   # 另一种奇怪的用法,进程脱离父进程被别的进程收养
   ```

4. 协程命令

   ```bash
   # 暂时不懂协程的原理,但是目前的运行状态时后台运行但是截断输出,父进程是当前的bash shell
   coproc command
   coproc name { command; }
   ```

#### 外部 / 内部命令

* 外部命令

  Linux存在外部命令和内部命令的区别,首先外部命令的操作是创建自己成的(forking衍生)

* 内部命令

  Linux将很多的shell命令都集成在我们的shell环境中,调用内建命令会加快运行效率,因为不需要开启子进程

```bash
type command_name    # 区别命令是否是内建命令或者是外部命令,是外部命令都存放在/bin/目录下
type -a command_name   # 有的命令有存在內建和外部的两种实现方式,-a参数可以罗列出来所有的命令的两种情况
which command_name    # which命令只会显示出命令的外部实现方式
# 滴啊用程序的外部命令
/bin/command_name
```

#### history

histor命令是Linux下一款非常强大的命令,可以查看跟踪当前的执行过的命令的历史记录,**默认保留1000条历史记录(存储在HISTSIZE环境变量中HISTTIMEFORMAT环境变量存储history的历史记录表现形式比如行号(方便我们的!调用历史记录))**

* !! : 执行上一条命令
* !n : 之心ghistory中编号是n的历史命令

history是不会立即写入.bash_history文件存储的,想要强制写入可以使用history -a参数命令

#### alias

别名操作可以辅助我们减少命令的输入量

别名如果没有设定在.bashrc文件中的话是只默认在定义的shell环境中有效

```bash
alias -p    # 显示当前系统的别名
alias newname='command line ...'    # 命令行的别名设置,可以设置成函数或者其他组合命令的简写别名
```

