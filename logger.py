import datetime
import time,sys
def log(type_:str,msg):
    file=(sys.stdout if type_.lower()!="error" else sys.stderr)
    print(f"[{str(datetime.datetime.today()).split('.')[0]}][maisocket][{type_}] {msg}",
          file=file)