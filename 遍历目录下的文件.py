import os

full_names = []


def lookup(path=None):
    global full_names
    if not path:
        dirs = os.getcwd()
    else:
        if os.path.isdir(path):
            dirs = path
        else:
            print(path)
            return
    # 遍历路径下的所有目录，并按顺序排序
    os.chdir(dirs)
    dirs = os.getcwd()
    dir_files = os.listdir(dirs)
    dir_files.sort()
    for dir_file in dir_files:
        if os.path.isfile(dir_file):
            full_name = os.path.join(dirs, dir_file)
            full_names.append(full_name)
        elif os.path.isdir(dir_file):
            lookup(dir_file)
    os.chdir("../")

if __name__ == '__main__':
    dir = input("请输入一个需要遍历的目录")
    lookup(dir)
    for full_name in full_names:
        print(full_name)
