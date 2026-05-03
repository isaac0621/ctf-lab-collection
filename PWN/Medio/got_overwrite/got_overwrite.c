#include <stdio.h>
#include <stdlib.h>

extern int printf(const char *, ...);
extern void puts(const char *);

// GOT Overwrite Challenge
void print_flag() {
    printf("CTF{got_overwrite}\n");
}

int main() {
    char buf[64];
    printf("Enter input: ");
    fgets(buf, sizeof(buf), stdin);
    
    printf("You entered: %s\n", buf);  // GOT entry can be overwritten
    
    return 0;
}
