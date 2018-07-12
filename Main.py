import math
import time

print("RUN")
#Gets valid input for waveform
waveform = input("Waveform(Sin or Square): ").lower()
while waveform != "sin" and waveform != "square":
    waveform = input("\nPlease enter a valid option.\nWaveform(Sin or Square): ").lower()
#Gets valid input for frequency
isFloat = False
while isFloat == False:
    frequency = input("Frequency(Hz): ")
    try:
        frequency = abs(float(frequency))
        isFloat = True
    except ValueError:
        print("\nPlease enter a valid option.")
#Shows the user what they have chosen as their waveform
print(str(frequency) + "Hz " + waveform + " wave")

period = 1/frequency
print("Period: " + str(period) + " sec\n")

values = {0:0}

def generateSin():
    for x in range(1,int(6283*period)):
        value = math.sin(x*frequency*0.001)
        values.update({x:value})
        if value<0.001:
            if value>-0.001:
                print(x)

def generateSqr():
    cycleTime = 1.0/frequency/2
    for x in range(1,1000):
        return cycleTime

if waveform == "sin":
    generateSin()
else:
    print(generateSqr())

print(values)

trash = input("Press enter to start.")

while True:
    for x in range(0, int(6283*period)):
        if x%10 == 0:
            print(str(x) + ": " + str(values[x]))
            time.sleep(0.01)