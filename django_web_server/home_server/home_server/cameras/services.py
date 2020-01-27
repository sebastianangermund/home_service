from picamera import PiCamera
from time import sleep

def request_get(url, params):
    pass

def take_picture(camera_address, photo_name):
    path = f'/home/pi/Projects/home_service/django_web_server/home_server/assets/photos/{photo_name}'
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture(path)
    camera.stop_preview()
    return True
