#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>
#include <stdlib.h>

/*
   1. 父进程创建子进程1,子进程1创建子进程2
   2. 子进程1立即结束，子进程2成为zombie进程，父进程捕捉到子进程1的结束，父进程退出
   3. 子进程2被init1号进程领养，打印出init1的PID并退出
 */

int main()
{
    pid_t pid;
    if((pid = fork()) < 0)
    {
        printf("fork error\n");
        exit(0);
    }
    else if(pid == 0)    //第一个子进程
    {
        if((pid = fork()) < 0)
        {
            printf("error fork\n");
            exit(0);
        }
        else if(pid > 0)
            exit(0);
        sleep(2);
        printf("第二个子进程的父进程 %d\n" , getppid());
        exit(0);
    }

    if(waitpid(pid , NULL , 0) != pid)
    {
        printf("waitpid error\n");
        exit(0);
    }
    exit(0);
}
