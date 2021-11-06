
cmake_minimum_required(VERSION 3.13)

project(3cc)

find_program(LIT NAMES "lit")

add_executable(3cc main.c)

add_subdirectory(test)
