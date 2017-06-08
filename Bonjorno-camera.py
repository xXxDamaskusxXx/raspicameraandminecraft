import picamera
from time import sleep
camera= picamera.PiCamera()
input = raw_input("escribi algo\n")
if input=='a':
    for x in range(0,10):
        camera.capture('timelapse' + str(x) + '.jpg')
        sleep(1)
        print "Te saque un escracho" 
else:
    if input=='b':
        camera.awb_mode= 'incandescent'
        camera.capture('efecto.jpg')
        print "Alto efecto loko"
    else:
        print "input no reconocido, pero igual intentaste"
            
