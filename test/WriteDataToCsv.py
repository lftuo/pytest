#!/usr/bin/python
# -*- coding:utf8 -*-
# @Author : tuolifeng
# @Time : 2017/11/29 17:07
# @File : WriteDataToCsv.py
# @Software : IntelliJ IDEA
import csv
import random
import string

import datetime


class WriteDataToCsv(object):
    def write_csv(self):
        csvFile = open('csvData_hive.txt','wb')
        write = csv.writer(csvFile)
        for i in range(13000000):
            #write.writerow([str(i),write_test.get_random_str(),write_test.get_random_str(),write_test.get_random_str()])
            write.writerow([str(i),
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女",
                            "0:否",write_test.get_random_int(),"1:男","1:是",write_test.get_random_int(),write_test.get_random_int(),"0:女"])
        csvFile.close()


    def get_random_str(self):
        '''
        获取随机字符串，8位长度
        :return:
        '''
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        return ran_str

    def get_random_int(self):
        '''
        获取随机数字 0-10之间
        :return:
        '''
        ran_int = random.randint(0,10)
        return ran_int

if __name__ == '__main__':
    #starttime = datetime.datetime.now()
    write_test = WriteDataToCsv()
    #write_test.write_csv()
    #endtime = datetime.datetime.now()
    #print endtime,starttime
    for i in range(210):
        print write_test.get_random_str()