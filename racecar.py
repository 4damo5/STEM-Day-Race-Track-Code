from picamera import PiCamera
import time 
from gpiozero import DistanceSensor, DigitalInputDevice
import imageio.v2 as imageio
import os

#intiializes camera
camera = PiCamera()

#continuously read the state of blocker done
#when starting block is lifted (aka the digital pin reads 0 for the blocker) done
#start checking the Ultrasonic Sensor done
#if the sensor detects car done
#start camera, take 5 pictures done 
#stop camera, compile pictures 1-5 into gif done

#Sources:
#https://randomnerdtutorials.com/raspberry-pi-digital-inputs-python/
#https://projects.raspberrypi.org/en/projects/physical-computing/12
#https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/6
#https://raspberrypi.stackexchange.com/questions/91784/gpiozero-button-when-pressed
#https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python

foil = DigitalInputDevice(4)
ultrasonic = DistanceSensor(echo=17, trigger=5)

car_threshold = .5

cam_state = False


if os.path.exists('/home/raspu/Desktop/video.h264'):
    os.remove('/home/raspu/Desktop/video.h264')

#start = time.monotonic()

#runs infinitely
while True:
    #print foil data and us sensor data
    print(foil.value, ultrasonic.distance)

    #when the breaker circuit is broken from the foil
    if foil.value == 0:
        
        #start camera
        camera.start_preview()

        #if the camera isn't already recording
        if cam_state == False:
            #start the timer
            start = time.monotonic()
            
            #start the camera
            camera.start_recording('/home/raspu/Desktop/video.h264')
            
            #camera is on
            cam_state = True

        #if there is a car in the range of the sensor
        if ultrasonic.distance <= car_threshold:
            #sensor var to end timer
            end = time.monotonic()

            #print the race time and velocity
            print(f'Race Time: {end-start}')
            print(f'Velocity: {3/(end-start)} ft/s')

            #delay a bit before ending the recording in order to catch the end
            time.sleep(5)

            #stop recording
            camera.stop_recording()
            camera.stop_preview()
            
            #end code
            break
    

