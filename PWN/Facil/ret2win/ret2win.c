#include <stdio.h>
#include <stdlib.h>

// ret2win Challenge
// Compile: gcc -fno-stack-protector -o ret2win ret2win.c

void win() {
    system("/bin/sh");
    printf("CTF{ret2win_shell}\n");
}

void vulnerable() {
    char buf[64];
    gets(buf);  // Buffer overflow
}

int main() {
    printf("Overflow me!\n");
    vulnerable();
    return 0;
}
