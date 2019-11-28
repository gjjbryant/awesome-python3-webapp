'''
@Author: guojijie
@Date: 2019-11-28 21:37:57
@LastEditTime: 2019-11-28 21:41:37
@LastEditors: Please set LastEditors
@Description: 常用通用方法     注：文件头注释（ctrl+alt+i） 和函数头注释（ctrl+alt+t）工具，一键生成头注释
@FilePath: \awesome-python3-webapp\www\Common\common.py
'''


'''
@字符串后缀匹配
@param {type} 
@return: 
'''
def endwith(s,*endstring):
    resultArray = map(s.endswith,endstring)
    if True in resultArray:
        return True
    else:
        return False
