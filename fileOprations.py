import os
 
def TextFileNames():
    path = "saved"
    dir_list = os.listdir(path)
    all_req_files=[]
    for x in dir_list:
        if x.endswith(".txt"):
           all_req_files.append(x)
    return all_req_files
