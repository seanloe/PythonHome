#! /usr/bin/env python
# -*- coding: utf-8 -*-


def fab(n):
  a,b = 0,1
  while b<n:
   print(b)
   a, b = b, a+b
   
fab(1000)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

matrix2 = list(zip(*matrix))
print(matrix2)
