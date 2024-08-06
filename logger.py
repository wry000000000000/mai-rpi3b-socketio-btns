'''Just a logger，you needn't modify it 只是个日志记录器，不用修改'''
import datetime
import time,sys
def log(type_:str,msg):
    file=(sys.stdout if type_.lower()!="error" else sys.stderr)
    print(f"[{str(datetime.datetime.today()).split('.')[0]}][maisocket][{type_}] {msg}",
          file=file)
