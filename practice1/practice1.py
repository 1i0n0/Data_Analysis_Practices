#!/usr/bin/python3
# -*- coding = UTF-8 -*-

# 导入第三方模块
import pandas as pd
import sys

# 利用read_table函数读取文本文件的数据
path = sys.path[0]
data1 = pd.read_table(filepath_or_buffer=f'{path}/data1.txt',  # 指定文件的路径，即同工作目录下data1.txt
                      engine='python',  # 使用python引擎解析，可跳过末尾两行
                      sep=',',  # 指定数据中变量之间的分隔符
                      header=None,  # 不需要将原始数据中的第一行读作表头
                      names=['id', 'name', 'gender', 'occupation'],  # 重新为各列起变量名称
                      skiprows=2,  # 跳过起始的两行数据
                      skipfooter=2,  # 跳过末尾的两行数据
                      comment='#',  # 不读取"#"开头的数据行
                      converters={'id': str}  # 对工号变量进行类型转换，避免开头的00消失
                      )

# 返回数据内容
print(data1)
