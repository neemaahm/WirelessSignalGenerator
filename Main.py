import math
import time
import matplotlib.pyplot as plt

#import board
#import busio
#import Adafruit_MCP4725

print("RUN")


#Gets valid input for waveform
def inputWaveform():
    waveform = input("Waveform(Sin or Square): ").lower()
    while waveform != "sin" and waveform != "square":
        waveform = input("\nPlease enter a valid option.\nWaveform(Sin or Square): ").lower()
    return waveform

#Gets valid input for frequency
def inputFrequency():
    isValid = False
    while isValid == False:
        frequency = input("Frequency(Hz): ")
        try:
            frequency = abs(float(frequency))
            isValid = True
        except ValueError:
            print("\nPlease enter a valid option.")
    return frequency

#Gets valid input for resolution
#Resolution is the number of outputs per second, independent of frequency.
def inputRes():
    isValid = False
    while isValid == False:
        res = input("Waveform Resolution(10-1000): ")
        try:
            res = abs(int(res))
            if res >= 1 and res <= 1000:
                isValid = True
            else:
                print("\nPlease enter a number within the range.")
        except ValueError:
            print("\nPlease enter a valid input.")
    return res

#Sets the waveform, frequency, and resolution variables
waveform = inputWaveform()
frequency = inputFrequency()
res = inputRes()

#Shows the user what they have chosen as their waveform and its period
print(str(frequency) + "Hz " + waveform + " wave")
period = 1/frequency
print("Period: " + str(period) + " sec\n")

#Creating dictionaries used in the rest of the code
rawValues = {0:0}
outputValues = {0:0}

#Creates x and y lists used for graphing
graphX = []
graphY = []
for i in range(0, int(math.pi*2*res*period)):
    graphX.append(i)

#Fills the rawValues dictionary with sin wave values
def generateSin():
    for i in range(1,int(math.pi*2*res*period)):
        value = math.sin(i * frequency * (1.0/res))
        rawValues.update({i:value})
        if value < 0.001:
            if value > -0.001:
                print(i)

#Fills the rawValues dictionary with square wave values (not currently working)
def generateSqr():
    cycleTime = 1.0/frequency/2
    for x in range(1,1000):
        return cycleTime

#Processes the rawValues dictionary and fills the outputValues dictionary with final output values
def processValues():
    for i in rawValues:
        if rawValues[i] <= 0.0:
            val = int((rawValues[i]+1)*2.5*(4096/5))
        else:
            val = int(((rawValues[i]*5/6)+2.5)*819.2)

        #val = int((rawValues[i]+1)*2048)
        graphY.append(val)
        outputValues.update({i:val})

#Outputs values to the 12 bit DAC (prints values to console just for now)
def output():
    #while True:
    for x in outputValues:
            print(str(x) + ": " + str(outputValues[x]))
            time.sleep(0.01)

if waveform == "sin":
    generateSin()
else:
    print(generateSqr())

print(rawValues)

temporary = input("Press enter to start.")


processValues()

print(graphX)
print(graphY)

plt.plot(graphX, graphY)
plt.xlabel('Time')
plt.ylabel('Dac Output')
plt.title('Dac Output vs Time')
plt.show()

output()