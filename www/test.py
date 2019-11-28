'''
@Author: guojijie
@Date: 2019-11-28 20:34:40
@LastEditTime: 2019-11-28 21:55:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \awesome-python3-webapp\www\test.py
'''
# test
from Common import rehelper,common


def main():
    tel = input("请输入手机号")
    v =  rehelper.verifyPhone(tel)

    if v is True:
        print("手机格式正确！")
    else:
        print("手机格式错误")
    
    eml = input("请输入邮箱地址")
    u =  rehelper.verifyEmails(tel)

    if v is True:
        print("邮箱地址正确！")
    else:
        print("邮箱地址错误")

if __name__ == "__main__":
    main()

    