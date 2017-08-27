import os,shutil
import logging
logging.basicConfig(level=logging.INFO)



allFiles = []                    #所有符合要求文件路径集合
preFix = ("pdf","jpg")           #需要筛选的后缀
oriPath = "E:\\Temp"         #原始路径
destPath = "D:\\Temp\\pycopy"          #目标路径
oprtMode = "copy"         #操作模式 copy 复制  move 移动

#遍历文件夹，找到符合条件的文件
for folderName,subFolders,fileNames in os.walk(oriPath):

    for fileName in fileNames:
        spFileName = fileName.split('.')

        if spFileName[len(spFileName)-1] in preFix:                    #按"."分割文件名，分割结果最后一组即为后缀
            allFiles.append(os.path.join(folderName,fileName))          #使用系统拼接目录功能，拼接目录和文件名


#移动文件至指定文件夹
if not os.path.exists(destPath):
    os.makedirs(destPath)

for files in allFiles:

    if oprtMode == "copy":
        shutil.copy(files, destPath)

    elif oprtMode == "move":
        shutil.move(files, destPath)

#TODO 增加进度条显示
#FIXME 如果文件夹内有重名文件，移动后会导致后入重名文件覆盖先入重名文件
#TODO 增加按照关键字复制移动功能
#TODO 增加按照正则表达式复制移动功能

