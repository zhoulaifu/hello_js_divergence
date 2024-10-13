#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generate_random(int n) {
    srand(time(0));
    for (int i = 0; i < n; i++) {
        printf("%d ", rand() % (n + 1));
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <n>\n", argv[0]);
        return 1;
    }
    int n = atoi(argv[1]);
    generate_random(n);
    return 0;
}

