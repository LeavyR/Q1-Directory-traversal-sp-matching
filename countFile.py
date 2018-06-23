import os
import re
import threading


class fileReader:
    def __init__(self):
        self.totalCount=0
        self. threads = []
    def sumNum(self,path):
        file_object = open(path, 'rU')
        try:
            for line in file_object:
                # Find all assosiate number
                result = re.findall("MSRA-(\d+)", line)
                for num in result:
                    # 如果获取数据，则计算结果
                    self.totalCount+=int(num)
        finally:
            file_object.close()
            # threading.sleep(10)

    def get_File(self,rootdir):
        list = os.listdir(rootdir)  # 获取文件夹下所有的目录与文件
        for i in range(0, len(list)):
            path = os.path.join(rootdir, list[i])
            if os.path.isfile(path):
                # 获取的路径为文件，声明线程
                t1 = threading.Thread(target=self.sumNum, args=(path,))
                self.threads.append(t1)
            else:
                self.get_File(path)  # 获取的路径为文件夹--递归列出文件夹下所有的目录与文件

    def run_Thread(self):
        for t in self.threads:
            # setDaemon(True)将线程声明为守护线程
            t.setDaemon(True)
            # 启动线程
            t.start()
            # join()方法，用于等待线程终止，在子线程完成运行之前，这个子线程的父线程将一直被阻塞
            t.join()



def main():
    # 实例化类
    fr = fileReader()
    # 获取文件夹
    rootdir="C:/Users/leavy/Desktop/MSRA-Interview-Gaoyuan/MSRA-Interview-Gaoyuan/Q2/Test_folder"
    # 获取文件夹下文件
    fr.get_File(rootdir)
    # 运行线程
    fr.run_Thread()
    # 打印结果
    print(fr.totalCount)


if __name__ == "__main__":
   main()

