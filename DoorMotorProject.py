# import required libs
import time
import RPi.GPIO as GPIO

GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# be sure you are setting pins accordingly
# GPIO10,GPIO9,GPIO11,GPI25
StepPins = [10,9,11,25]
 
# Set all pins as output
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

#wait some time to start
time.sleep(0.5)
 
# Define some settings
StepCounter = 0
WaitTime = 0.0015
 
# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = range(0, StepCount1)
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]
 
StepCount1r = 4
Seq1r = []
Seq1 = range(0, StepCount1)
Seq1[0]r = [0,0,0,1]
Seq1[1]r = [0,0,1,0]
Seq1[2]r = [0,1,0,0]
Seq1[3]r = [1,0,0,0]
# Define advanced sequence
# as shown in manufacturers datasheet
StepCount2 = 8
Seq2 = []
Seq2 = range(0, StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

#Seq2 reverse
StepCount2r = 8
Seq2r = []
Seq2r = range(0, StepCount2)
Seq2[0]r = [0,0,0,1]
Seq2[1]r = [0,0,1,1]
Seq2[2]r = [0,0,1,0]
Seq2[3]r = [0,1,1,0]
Seq2[4]r = [0,1,0,0]
Seq2[5]r = [1,1,0,0]
Seq2[6]r = [1,0,0,0]
Seq2[7]r = [1,0,0,1]

#Fulltorque 
StepCount3 = 4
Seq3 = []
Seq3 = range(0, StepCount3)
Seq3[0] = [0,0,1,1]
Seq3[1] = [1,0,0,1]
Seq3[2] = [1,1,0,0]
Seq3[3] = [0,1,1,0]

`#Full torque reverse
StepCount3r = 4
Seq3r = []
Seq3r = range(0, StepCount3r)
Seq3r[0] = [0,1,1,0]
Seq3r[1] = [1,1,0,0]
Seq3r[2] = [1,0,0,1]
Seq3r[3] = [0,0,1,1]
# set

Seq = 3r

StepCount = StepCount3r
 
# Start main loop
try:
  while 1==1:
    for pin in range(0, 4):
      xpin = StepPins[pin]
      if Seq[StepCounter][pin]!=0:
        #print " Step %i Enable %i" %(StepCounter,xpin)
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)
    StepCounter += 1

  # If we reach the end of the sequence
  # start again
    if (StepCounter==StepCount):
      StepCounter = 0
    if (StepCounter<0):
      StepCounter = StepCount
 
  # Wait before moving on
    time.sleep(WaitTime)
except:
  GPIO.cleanup();
finally: #cleaning up and setting pins to low again (motors can get hot if you wont) 
  GPIO.cleanup();
  for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)