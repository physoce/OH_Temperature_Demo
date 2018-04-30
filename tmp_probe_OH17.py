#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Update a simple plot as rapidly as possible to measure speed.
"""

## Add path to library (just for examples; you do not need this


from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
import tmp_probe as tp
app = QtGui.QApplication([])

tmp_probe1 = tp.Tmp_Probe(0)
tmp_probe2 = tp.Tmp_Probe(1)
p = pg.plot()
p.setWindowTitle('pyqtgraph example: PlotSpeedTest')
p.setXRange(-10,0) 
p.setLabel('bottom', 'Time', units='s')
curves = []
curves2 = []
#curve.setFillBrush((0, 0, 100, 100))
#curve.setFillLevel(0)

#lr = pg.LinearRegionItem([100, 4900])
#p.addItem(lr)
chunkSize = 100

data = np.empty((chunkSize+1,2)) # Init empty chunk of data
data2 = np.empty((chunkSize+1,2))
#data = [tmp_probe1.get_temp()]
ptr = 0
lastTime = time()
fps = None
maxChunks = 10
startTime = pg.ptime.time()


def update():
    global curves,curves2, data,data2, ptr, p, lastTime, fps, tmp_probe1,tmp_probe2,chunkSize,maxChunks
    now = pg.ptime.time()
    for c in curves:
        c.setPos(-(now-startTime), 0)
    for c in curves2:
        c.setPos(-(now-startTime), 0)
    i = ptr % chunkSize
    if i == 0:
        curve= p.plot(pen=(255,0,0))
        curves.append(curve)
        curve2= p.plot(pen=(0,255,0))
        curves2.append(curve2)
        last = data[-1]        
        data = np.empty((chunkSize+1,2))        
        data[0] = last
        last = data2[-1]
        data2 = np.empty((chunkSize+1,2))
        data2[0] = last
        while len(curves) > maxChunks:
            c = curves.pop(0)
            p.removeItem(c)
        while len(curves2) > maxChunks:
            c = curves2.pop(0)
            p.removeItem(c)
    else:
        curve = curves[-1]
        curve2 = curves2[-1]
    data[i+1,0] = now - startTime
    data[i+1,1] = tmp_probe1.get_temp()
    data2[i+1,0] = now - startTime
    data2[i+1,1] = tmp_probe2.get_temp()
    curve.setData(x=data[:i+2, 0], y=data[:i+2, 1])
    curve2.setData(x=data2[:i+2, 0], y=data2[:i+2, 1])

    ptr += 1

    '''
    data.append(tmp_probe1.get_temp())
    curve.setData(data[-40:])
    #curve.setData(data[ptr%10])
    ptr += 1
    now = time()
    dt = now - lastTime
    lastTime = now

    if fps is None:
        fps = 1.0/dt
    else:
        s = np.clip(dt*3., 0, 1)
        fps = fps * (1-s) + (1.0/dt) * s
    p.setTitle('%0.2f fps' % fps)
    app.processEvents()  ## force complete redraw for every plot
    '''
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)
    


## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
