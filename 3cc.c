#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
  if (argc != 2) {
    fprintf(stderr, "Incorrect number of arguments");
    return 1;
  }

  printf("format MS64 COFF\n");
  printf("section '.text' code readable executable\n");
  printf("start:\n");
  printf("\tmov rax, %d\n", atoi(argv[1]));
  printf("\tret\n");
  return 0;
}