#include <stdio.h>
#include <string.h>

// Buffer Overflow Challenge
// Compile: gcc -z execstack -fno-stack-protector -m32 -o bof bof.c

void vulnerable() {
    char buf[32];
    gets(buf);  // Vulnerable! No bounds checking
}

int main() {
    printf("Input your payload: ");
    vulnerable();
    printf("Done!\n");
    return 0;
}
