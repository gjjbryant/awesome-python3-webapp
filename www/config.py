#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration  简化读取配置文件，可以把所有配置读取到统一的config.py中

zip函数
>>>a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
 
>>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
>>>
'''

__author__ = 'GJJ'

import config_default

class Dict(dict):
    '''
    把这个dict转化成自己定义的Dict类型 好处是可以通过d.key 这种方法来取值
    Simple dict but support access as x.y style.
    '''
    def __init__(self,names=(),values=(),**kw):
        super(Dict,self).__init__(*kw)
        for k,v in zip(names,values):
            self[k] = v

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
    
def merge(defaults,override):
    r = {}
    for k,v in defaults.items():
        if k in override:
            if isinstance(v,dict):
                r[k] = merge(v,override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def toDict(d):
    D = Dict()
    for k,v in d.items():
        D[k] = toDict(v) if isinstance(v,dict) else v
    return D

configs = config_default.configs

try:
    import config_override
    configs = merge(configs,config_override.configs)
except ImportError:
    pass

configs = toDict(configs)
