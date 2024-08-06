'''The server file (install on your ALLS or other mainunits running maimai)
服务器文件（装在你的ALLS或者其他能运行maimai的主机上）'''
import eventlet

import logger

eventlet.monkey_patch()

import socketio
import eventlet.wsgi

import pykeyboard

sio = socketio.Server(async_mode='eventlet')  # 指明在evenlet模式下
app = socketio.Middleware(sio)

KBD=pykeyboard.PyKeyboard()

keys=list("WEDCXZAQ")

def key_dn(*args):
    '''手台按键按下'''
    logger.log("INFO","手台按键按下")
    if len(args)<2:
        logger.log("ERROR","没有传递键号")
        return 0
    o=keys[int(args[1])-1]
    logger.log("INFO",f"模拟按下：{o}")
    KBD.press_key(o)
    print(args)
def key_up(*args):
    '''手台按键抬起'''
    logger.log("INFO","手台按键抬起")
    if len(args)<2:
        logger.log("ERROR","没有传递键号")
        return 0
    o=keys[int(args[1])-1]
    logger.log("INFO",f"模拟抬起：{o}")
    KBD.release_key(o)
    print(args)
sio.on("key_dn")(key_dn)
sio.on("key_up")(key_up)

eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 8000)), app)
