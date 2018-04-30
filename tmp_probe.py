
import sys,os
import plotly as py

class Tmp_Probe(object):
    '''
    Return the temperature reading from a one-wire probe. Currently using the Pin 4
    '''
    def __init__(self,snsNum=0):
        if snsNum == 0:
            self.temp_sensor = '/sys/bus/w1/devices/28-00000605f68a/w1_slave'
        elif snsNum == 1:
            self.temp_sensor = '/sys/bus/w1/devices/28-000006064128/w1_slave'		
        self.__os_prep()

    def __os_prep(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

    def __temp_raw(self):
        f = open(self.temp_sensor, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def __read_temp(self):
        lines = self.__temp_raw()
        while lines[0].strip()[-3:] != 'YES':
#            time.sleep(0.1)
            lines = self.__temp_raw()
        temp_output = lines[1].find('t=')
        if temp_output != -1:
            temp_string = lines[1].strip()[temp_output + 2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c

    def get_temp(self):
        return self.__read_temp()

class WebReport(object):

    def __init__(self,token=1):
        self.stream_tokens = ["7c0ig164ac","64299hxjgr"]
        self.stream_id1 = dict(token=self.stream_tokesn[0])
        self.stream_id2 = dict(token=self.stream_tokesn[1])
        self.plot_url = py.plot(self.make_plots(),filename="Temp_Demo")

        self.s1 = py.Stream(stream_id=self.stream_tokens[0])
        self.s2 = py.Stream(stream_id=self.stream_tokens[1])

    def make_plots(self):
        pass
