# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import os, sys
import re
import os.path
import PIL.Image
#对文件操作的工具模块


#索引文件夹及子目录返回所有文件路径
def all_path(dirname)->list:
    filelistlog = dirname + "\\filelistlog.txt"  # 保存文件路径
    postfix = [".jpg",".png"]  # 设置要保存的文件格式
    all_path = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            
            apath = os.path.join(maindir, filename)
            if(os.path.splitext(apath)[1] in postfix):
                all_path.append(apath)
    
    return all_path

def change_imaeg_size(path_name):
    try:
        infile = path_name
        outfile = path_name
        str_path = os.path.splitext(path_name)[0]
        str_name = os.path.splitext(path_name)[1]
        x_s = 800
        y_s = 480
        im = PIL.Image.open(infile)
        (x,y) = im.size #read image size
        if y > x:
            x_s = 480
            y_s = 800
        if y != x:
            out = im.resize((x_s,y_s),PIL.Image.ANTIALIAS) #resize image with high-quality
            out.save(outfile)
        if y == x:
            if str_name == ".png":
                im = im.convert('RGB')
            out = im.resize((32,32),PIL.Image.ANTIALIAS) #resize image with high-quality
            out.save(str_path+"32"+".jpg")
            out = im.resize((64,64),PIL.Image.ANTIALIAS) #resize image with high-quality
            out.save(str_path+"64"+".jpg")
            out = im.resize((128,128),PIL.Image.ANTIALIAS) #resize image with high-quality
            out.save(str_path+"128"+".jpg")
    except Exception as e:
        print("图片损坏")
        pass



if __name__ == '__main__':
    copy_file('../data/test1.txt', '../data/text.txt','UTF-8')
    contents = read_file_list('../dict/time.dict','UTF-8')
    print(contents)

