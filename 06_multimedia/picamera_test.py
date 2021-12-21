import picamera
import time

path = '/home/pi/src4/06_multimedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3) #카메라 준비시간
    camera.capture('%s/photo.jpg' % path)
finally:
    camera.stop_preview()