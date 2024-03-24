// slow python momets fixing library
#include <stdio.h>
#include <stdlib.h>
#include <macros.h>

// for example, let's make REAL exit() function)
void $exit(int status) {
    exit(status);
}

int *$__array_init__(int size) {
    return (int *)malloc(sizeof(int)*size);
}

int $__array_getitem__(int *self, int index) {
    return self[index];
}

void $__array_setitem__(int *self, int index, int value) {
    self[index] = value;
}
