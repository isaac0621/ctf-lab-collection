#include <stdio.h>
#include <stdlib.h>

// ret2libc Challenge
// Compile: gcc -fno-stack-protector -o ret2libc ret2libc.c

void vulnerable() {
    char buf[64];
    gets(buf);  // Buffer overflow
}

int main() {
    printf("Exploit me!\n");
    vulnerable();
    return 0;
}
