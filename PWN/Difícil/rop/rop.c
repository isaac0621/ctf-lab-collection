#include <stdio.h>
#include <string.h>

// ROP Chain Challenge
// Compile: gcc -fno-stack-protector -o rop rop.c

int main() {
    char buf[32];
    printf("ROP Challenge!\n");
    printf("Enter payload: ");
    fgets(buf, sizeof(buf), stdin);
    
    // Trigger vulnerability
    return 0;
}
