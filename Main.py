import math
import time

print("RUN")


#Gets valid input for waveform
def inputWaveform():
    waveform = input("Waveform(Sin or Square): ").lower()
    while waveform != "sin" and waveform != "square":
        waveform = input("\nPlease enter a valid option.\nWaveform(Sin or Square): ").lower()
    return waveform

#Gets valid input for frequency
def inputFrequency():
    isFloat = False
    while isFloat == False:
        frequency = input("Frequency(Hz): ")
        try:
            frequency = abs(float(frequency))
            isFloat = True
        except ValueError:
            print("\nPlease enter a valid option.")
    return frequency

#Sets the waveform and frequency variables
waveform = inputWaveform()
frequency = inputFrequency()

#Shows the user what they have chosen as their waveform and its period
print(str(frequency) + "Hz " + waveform + " wave")
period = 1/frequency
print("Period: " + str(period) + " sec\n")
#Generates variables

#Generates dictionaries used in the rest of the code
rawValues = {0:0}
outputValues = {0:0}

#Fills the rawValues dictionary with sin wave values
def generateSin():
    #for x in range(1,int(6283*period)):
    for x in range(1,int(62*period)):
        #value = math.sin(x*frequency*0.001)
        value = math.sin(x * frequency * 0.1)
        rawValues.update({x:value})
        if value<0.001:
            if value>-0.001:
                print(x)

#Fills the rawValues dictionary with square wave values
def generateSqr():
    cycleTime = 1.0/frequency/2
    for x in range(1,1000):
        return cycleTime

#Processes the rawValues dictionary and fills the outputValues dictionary with final output values
def processValues():
    for x in rawValues:
        #if x % 10 == 0:
        if x%1 == 0:
            val = int((rawValues[x]+1)*2048)
            outputValues.update({x:val})

#Outputs values to the 12 bit DAC (prints values to console just for now)
def output():
    while True:
        for x in outputValues:
                print(str(x) + ": " + str(outputValues[x]))
                if outputValues[x] == 4096:
                    break
                time.sleep(0.01)

if waveform == "sin":
    generateSin()
else:
    print(generateSqr())

print(rawValues)

trash = input("Press enter to start.")


processValues()
output()