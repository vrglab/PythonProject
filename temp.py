import glob

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def readTempSensor():
    f = open(device_file, 'r')
    lines = f.read()
    f.close()
    temp_data = lines.split('t=')
    temperature = int(temp_data[1]) / 1000.0
    temperatureS = "%.1f" % temperature
    return temperatureS

readTempSensor()