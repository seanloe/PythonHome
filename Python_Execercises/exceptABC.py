#! /usr/bin/env python
# -*- coding: utf-8 -*-


class A(Exception):
    pass
    
class B(A):
    pass
    
class C(B):
    pass
    
classes =[C,B,A]
for cls in classes:
    try:
      raise cls()
    except C:
        print('Except C raised')
    except B:
        print('Except B raised')
    except A:
        print('Except A raised')
