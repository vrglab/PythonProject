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
        log.write(f"Die Temperatur im Serverraum beträgt am {time.strftime('%d.%m.%Y')} um {time.strftime('%H:%M:%S')} Uhr laut Sensor: {'%.1f' % temperature} °C\n")



def runEvery10Seconds():
    while True:
        try:
            readTempSensor()
            time.sleep(10)
        except KeyboardInterrupt:
            print("\n Temperaturmessung wird beendet.")
            print("\n Programm wird beendet.")
            sys.exit(0)

runEvery10Seconds()