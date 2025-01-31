import glob
import time
import sys

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def readTempSensor():
    f = open(device_file, 'r')
    lines = f.read()
    f.close()
    temp_data = lines.split('t=')
    temperature = int(temp_data[1]) / 1000.0
    with open("temptxt.txt", "a") as log:
        log.write(f"Die Temperatur im Serverraum beträgt um {time.strftime('%H:%M:%S')} Uhr laut Sensor: {temperature} °C")



def runEvery10Seconds():
    while True:
        try:
            readTempSensor()
            time.sleep(10)
        except KeyboardInterrupt:
            print("\n Temperature messen beendet")
            sys.exit(0)

