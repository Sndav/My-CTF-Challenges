#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    setbuf(stdout,0);
    setbuf(stdin,0);

    alarm(1);
    srand(time(0));
    int a,b,c;
    a = rand() % 1000;
    b = rand() % 1000;
    
    printf("%d + %d = ?\n",a,b);
    scanf("%d",&c);
    if(c == a+b){
        char buf[100];
        FILE *fd = fopen("/flag","r");
        fgets(buf,100,fd);
        puts(buf);
    }
    return 0;

}