# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import os, sys,shutil
import re
import FileUtilty


postfix = [".apk"]
tag_path = [r"F:\huoxing\SparkTool1\apk",r"F:\huoxing\SparkTool2\apk",r"F:\huoxing\SparkTool3\apk",r"F:\huoxing\SparkTool4\apk",
            r"F:\huoxing\SparkTool5\apk",r"F:\huoxing\SparkTool6\apk",r"F:\huoxing\SparkTool7\apk",r"F:\huoxing\SparkTool8\apk",
            r"F:\huoxing\SparkTool9\apk",r"F:\huoxing\SparkTool10\apk",]

result_path = [r"F:\huoxing\SparkTool1\finish",r"F:\huoxing\SparkTool2\finish",r"F:\huoxing\SparkTool3\finish",r"F:\huoxing\SparkTool4\finish",
            r"F:\huoxing\SparkTool5\finish",r"F:\huoxing\SparkTool6\finish",r"F:\huoxing\SparkTool7\finish",r"F:\huoxing\SparkTool8\finish",
            r"F:\huoxing\SparkTool9\finish",r"F:\huoxing\SparkTool10\finish",]


get_apk_path = FileUtilty.all_path(r"F:\新建文件夹\待上\外\20180919\1",postfix)
#print(get_apk_path)
#shutil.copyfile(srcfile,dstfile)

resultdict = {}


def rm_filedir(rootdir):
    filelist=[]
    filelist=os.listdir(rootdir)
    for f in filelist:
        filepath = os.path.join( rootdir, f )
        if os.path.isfile(filepath):
            os.remove(filepath)
            print (filepath+" removed!")
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath,True)
            print ("dir "+filepath+" removed!")
while(True):

    cmd = input("请输入命令 c,m,d,q :")

    if str(cmd) == "c":
        num = 0
        for apk_path in get_apk_path:
            shutil.copyfile(apk_path,tag_path[num]+r"\1.apk")
            resultdict[result_path[num]] = os.path.dirname(apk_path)
            num += 1
    if str(cmd) == "m":
        for apk_finish,result_name in resultdict.items():
            shutil.move(apk_finish+r"\1.apk",result_name+r"\1.apk")
    if str(cmd) == "d":
        for rootdir in tag_path:
            rm_filedir(rootdir)
    if str(cmd) == "q":
        try:
            resultdict.clear()
            os._exit(0)
        except:
            print("died")
