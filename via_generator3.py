# -*- coding: UTF-8 -*-
import os


def get_Filelist_C(dire):
    Filelist = []
    home1 = None
    global cppFlag, via_dir
    cppFlag = 0
    if not os.path.exists(os.path.join(dire, "via")):
        os.mkdir(os.path.join(dire, "via"))
    for home, dirs, files in os.walk(dire):
        for filename in files:
            if filename.endswith('.h') | filename.endswith('.hh') | filename.endswith('.hpp'):  # 匹配
                if home != home1:
                    Filelist.append('-i "' + os.path.join(home) + '"')
                    Filelist.append('-i "' + os.path.join(os.path.dirname(home)) + '"')
                    home1 = home
            if filename.endswith('.cpp') or filename.endswith('.cc') or filename.endswith('.cxx') or filename.endswith(
                    '.c++') and cppFlag == 0:
                cppFlag = 1
        # Filelist.append( filename)
    with open('./via/headerfiles_c.via', 'w') as f:
        for list_mem in Filelist:
            f.write(list_mem + "\n")
        return cppFlag


def get_filelist_Cpp(dire):
    Filelist = []
    home1 = None
    for home, dirs, files in os.walk(dire):
        for filename in files:
            if filename.endswith('.h') | filename.endswith('.hh') | filename.endswith('.hpp'):  # 匹配
                if home != home1:
                    Filelist.append('-si "' + os.path.join(home) + '"')
                    Filelist.append('-si "' + os.path.join(os.path.dirname(home)) + '"')
                    home1 = home
        # Filelist.append( filename)
    with open('./via/headerfiles_cpp.via', 'w') as f:
        for list_mem in Filelist:
            f.write(list_mem + "\n")


if __name__ == "__main__":
    path = os.path.abspath('.')
    cppFlag = get_Filelist_C(path)
    if cppFlag == 1:
        get_filelist_Cpp(path)
