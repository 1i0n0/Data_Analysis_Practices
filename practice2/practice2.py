#!/usr/bin/python3
# -*- coding = UTF-8 -*-

# 导入第三方模块
import pandas as pd

# 利用read_excel函数读取电子表格数据
data = pd.read_excel(io='./data2.xlsx',  # 指定文件的路径
                     header=None,  # 不需要将原始数据中的第一行读作表头
                     names=['id', 'date', 'prod_name', 'price', 'colour'],  # 重新为各列起变量名称
                     converters={'id': str},  # 对id变量进行类型转换，避免开头的00消失
                     na_values="未知"  # 将原始表中"未知"值转换为缺失值
                     )

# 返回数据内容
print(data)
