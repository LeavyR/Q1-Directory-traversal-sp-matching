import os
import re


class fileReader:
    def __init__(self):
        self.totalCount=0

    def sumNum(self,path):
        file_object = open(path, 'rU')
        try:
            for line in file_object:
                # Find all assosiate number
                result = re.findall("MSRA-(\d+)", line)
                for num in result:
                    self.totalCount+=int(num)
        finally:
            file_object.close()


    def get_File(self,rootdir):
        list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            path = os.path.join(rootdir, list[i])
            if os.path.isfile(path):
                self.sumNum(path)

            else:
                self.get_File(path)  # 列出文件夹下所有的目录与文件



def main():
    fr = fileReader()
    rootdir="C:/Users/leavy/Desktop/MSRA-Interview-Gaoyuan/MSRA-Interview-Gaoyuan/Q2/Test_folder"
    fr.get_File(rootdir)
    print(fr.totalCount)

if __name__ == "__main__":
   main()

