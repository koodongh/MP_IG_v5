from pylogix import PLC
import time

#import _H2104_detect
def PLC_():
    with PLC() as comm:
        comm.IPAddress = '192.168.1.13'  # PLC의 IP 주소

        # bool 태그 정의
        tag_IG = 'M1907_IG_DETECTED'  
        is_IG = comm.Read(tag_IG).Value
        print(f'is_IG : {is_IG}')
        if is_IG == False :
            comm.Write(tag_IG, True)
            is_IG = comm.Read(tag_IG).Value
            print(f'is_IG : {is_IG}')
        # bool 태그에 데이터 쓰기

if __name__ == '__main__':
    PLC_()
    #print('----Wait----')
    time.sleep(0.5)