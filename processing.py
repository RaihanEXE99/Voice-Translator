import os,glob
from os.path import join,isfile
from subprocess import check_output
import base64,json

# GSM = '''@£$¥èéùìòÇØøÅåΔ_ΦΓΛΩΠΨΣΘΞ^{}\[~]|€ÆæßÉ!\"#¤%&'()*+,-./0123456789:;<=>?¡ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÑÜ§¿abcdefghijklmnopqrstuvwxyzäöñüà'''

# def generateOutput(file_path,language,ext):
    # Clear Final Cache
    # try:
    #     files = glob.glob('final_cache/*')
    #     for f in files:
    #         os.remove(f)
    # except :
    #     print("Already Final Cache Is Clear")
    # out = check_output(["autosub","-i",file_path,"-S",language,"-F",ext,"-o","./final_cache"])

    # try:
    #     files = glob.glob('temp_files/*')
    #     for f in files:
    #         os.remove(f)
    # except :
    #     print("temp_files Clear")

    # # path="final_cache"
    # # first_file = next(join(path, f) for f in os.listdir(path) if isfile(join(path, f)))
    # # f = open(first_file, "r",encoding="ascii", errors="ignore")
    # # out = f.read()
    # # fsrt = ""
    # # for i in out:
    # #     if i not in GSM:
    # #         print("COT MAMAH",i)
    # #     else:
    # #         fsrt += i
    # # base64_bytes = base64.b64encode(fsrt.encode("ascii"))

    # # print(out)
    # # try:
    # #     files = glob.glob('final_cache/*')
    # #     for f in files:
    # #         os.remove(f)
    # # except :
    # #     print("Already Final Cache Is Clear")
    # # print(out)
    # # print("FINAL",fsrt)
    # return 

def generateOutput(file_path,language,ext):
    try:
        try:
            files = glob.glob('final_cache/*')
            for f in files:
                os.remove(f)
        except :
            print("Already Final Cache Is Clear")
        out = check_output(["autosub","-i",file_path,"-S",language,"-F",ext,"-o","./final_cache"])

        try:
            files = glob.glob('temp_files/*')
            for f in files:
                os.remove(f)
        except :
            print("temp_files Clear")
            
        path="final_cache"
        first_file = os.listdir("final_cache")[0]
        f = open(path+"/"+first_file, "r",encoding="UTF-8")
        out = f.read()

        try:
            files = glob.glob('final_cache/*')
            for f in files:
                os.remove(f)
        except :
            print("Already Final Cache Is Clear")
    
    except:
        out = "Error, Something Wrong!"
    return out