# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import os, sys
import re
import FileUtilty

def main():
    image_path_list =  FileUtilty.all_path(r"F:\新建文件夹\待上\游戏")

    for image_path in image_path_list:
        #print(image_path)
        FileUtilty.change_imaeg_size(image_path)
if __name__ == "__main__":
    main()
    input('press enter key to exit') 
