# coding: utf-8
import time
import picamera

camera = picamera.PiCamera()

camera.resolution = (1920, 1080)
camera.start_preview()
time.sleep(5)
camera.capture('preview.jpg', resize=(1280, 720))
camera.stop_preview()
camera.close()
