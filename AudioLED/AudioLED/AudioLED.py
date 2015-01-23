import sys
import ptvsd
ptvsd.enable_attach()

import ptvsd.visualstudio_py_util
sys.modules['visualstudio_py_util'] = ptvsd.visualstudio_py_util


from time import sleep
import RPi.GPIO as GPIO
import pyaudio
import wave
import audioop
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN)
#GPIO.setup(22, GPIO.IN)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)

p = pyaudio.PyAudio()

try:
    rms_hist = np.zeros(RATE / CHUNK * RECORD_SECONDS)

    n = 0
    while True:
        if ( GPIO.input(17) == True ):
            stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                rms = audioop.rms(data, 2)
               
                rms_hist = np.roll(rms_hist, -1)
                rms_hist[-1] = rms

                print(rms)

                if (rms > 2000):
                    GPIO.output(18, GPIO.HIGH)
                else:
                    GPIO.output(18, GPIO.LOW)
                if (rms > 8000):
                    GPIO.output(23, GPIO.HIGH)
                else:
                    GPIO.output(23, GPIO.LOW)
                if (rms > 15000):
                    GPIO.output(24, GPIO.HIGH)
                else:
                    GPIO.output(24, GPIO.LOW)
                if (rms > 20000):
                    GPIO.output(25, GPIO.HIGH)
                else:
                    GPIO.output(25, GPIO.LOW)

            stream.stop_stream()
            stream.close()

        else:
            GPIO.output(18, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(25, GPIO.LOW)

        sleep(0.2);

except KeyboardInterrupt: 
    p.terminate() 
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  

GPIO.cleanup()           # clean up GPIO on normal exit  
