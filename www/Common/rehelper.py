'''
@Author: guojijie
@Date: 2019-11-28 21:42:28
@LastEditTime: 2019-11-28 21:48:42
@LastEditors: Please set LastEditors
@Description: 正则表达式判断
@FilePath: \awesome-python3-webapp\www\Common\rehelper.py
'''
import re


'''
@判断邮箱地址是否正确: 
@param {type} 
@return: 
'''
def verifyEmails(email):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$ '
    if re.match(pattern,email) is not None:
        return True
    else:
        return False


'''
@判断手机号是否正确: 
@param {type} 
@return: 
'''
def verifyPhone(phoneNumber):
    pattern = r"^1[35678]\d{9}$"
    if re.match(pattern,phoneNumber) is not None:
        return True
    else:
        return False
