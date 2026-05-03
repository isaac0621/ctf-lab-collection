#include <stdio.h>
#include <stdlib.h>

// Fastbin Attack Challenge
// Compile: gcc -o fastbins fastbins.c

int main() {
    // Malloc twice
    void *p1 = malloc(32);
    void *p2 = malloc(32);
    
    printf("p1 at: %p\n", p1);
    printf("p2 at: %p\n", p2);
    
    // Create double free vulnerability
    free(p1);
    free(p1);  // Double free!
    
    // After this, we can control allocation
    void *p3 = malloc(32);
    void *p4 = malloc(32);
    
    printf("p3 at: %p\n", p3);
    printf("p4 at: %p\n", p4);
    
    printf("CTF{fastbin_attack}\n");
    
    return 0;
}
