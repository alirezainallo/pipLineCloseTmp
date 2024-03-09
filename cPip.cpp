#include <stdio.h>
#include <stdint.h>
#include <windows.h>

int main(int arg, char *args[]){
    FILE * pipLine = popen("python myTask.py", "r");
    printf("[main] open pip line\n");
    
    // Sleep(5000);
    DWORD timeOut = GetTickCount() + 5000;
    while(timeOut > GetTickCount()){
        printf("%c", (char)getc(pipLine));
    }
    pclose(pipLine);
    printf("[main] close pip line\n");
    return 0;
}