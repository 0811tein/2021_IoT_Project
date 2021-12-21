import picamera
import time

path = '/home/pi/src4/06_multimedia'

camera = picamera.PiCamera()
try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3) #카메라 준비시간
    while True:
        a = input("photo:1, video:2, exit:9 > ")
        now_str = time.strftime("%Y%m%d_%H%M%S")
        if a == '1':
            camera.capture('%s/%sphoto.jpg' % (path, now_str))
        elif a == '2': 
            camera.start_recording('%s/%svideo.h264' % (path, now_str))
            time.sleep(10)
            camera.stop_recording()
        elif a == '9':
            break
        else:
            print('incorrect')
finally:
    camera.stop_preview()
