#! /usr/bin/env python
#coding:utf-8
	
print("请输入任意一个整数数字：")
	
number = int(input())

if number == 10:
    print("您输入的数字是：{}".format(number))
    print("You are SMART.")
elif number > 10:
    print("您输入的数字是：{}".format(number))
    print("This number is more than 10.")
elif number < 10:
    print("您输入的数字是：{}".format(number))
    print("This number is less than 10.")
else:
    print("Are you a human?")
    
