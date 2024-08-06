import time
import gpiozero
import socketio
gps=[]
gps+=[2,3,4,17,27,22,10,9]
btns=[]
for i in range(8):
    btns+=[gpiozero.Button(gps[i])]
s0=socketio.client.Client()
s0.connect("http://192.168.31.102:8000")
isos={}
for i in btns:
    isos[i]=False
print("started")
if __name__ == '__main__':
    while True:
        index=-1
        for i in btns:
            index+=1
            if i.is_pressed and not isos[i]:
                print(index,"down")
                s0.call("key_dn",(index,))
                isos[i]+=1
            elif isos[i] and not i.is_pressed:
                s0.call("key_up",(index,))
                print(index,"up")
                isos[i]-=1
