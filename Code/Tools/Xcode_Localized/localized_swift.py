#!/usr/local/bin/python3.6.5
# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 PM9:36
# @Author  : L
# @Email   : L862608263@163.com
# @File    : localized_swift.py
# @Software: PyCharm

import os

file_path = '/Users/l/Desktop/阿里云git项目/A113D/pannel86_ios/A113D/A113D/SupportingFiles/en.lproj/Localizable.strings'

def desktop_path():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


def create_localizable_file():
    os.chdir(desktop_path())
    create_file = "touch LocalizedUtils.swift"
    os.system(create_file)

def open_file():
    pass

