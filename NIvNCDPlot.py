"""
Created on Thu Jan 10 09:21:44 2019

@author: ecswift

This program will take the time series data from NCD
and NI vibration sensors and plot it on a line graph
for visual comparisons.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import plotly.offline as pyo

import numpy as np
import pandas as pd
import datetime

"""
I chose to only be concerned with the RMS values of each.
Eventually, the plot can be applied to the DELTA values as well.
"""

#JSC-3 MWATTS data
dataJSC3MWATTS = pd.read_excel('NIvNCD.xlsx', sheet_name='JSC-3 MWATTS')
print(dataJSC3MWATTS.head())

#NCD JSC-3A RMS data (includes x, y, and z values)
dataNCDJSC3ARMS = pd.read_excel('NIvNCD.xlsx', sheet_name='NCD JSC-3A RMS')
print(dataNCDJSC3ARMS.head())
#NCD JSC-3B RMS data (includes x, y, and z values)
dataNCDJSC3BRMS = pd.read_excel('NIvNCD.xlsx', sheet_name='NCD JSC-3B RMS')
print(dataNCDJSC3BRMS.head())


#NI JSC-3A RMS MOH data
dataNIJSC3ARMSMOH = pd.read_excel('NIvNCD.xlsx', sheet_name='NI JSC-3A RMS MOH')
print(dataNIJSC3ARMSMOH.head())
#NI JSC-3A RMS MOV data
dataNIJSC3ARMSMOV = pd.read_excel('NIvNCD.xlsx', sheet_name='NI JSC-3A RMS MOV')
print(dataNIJSC3ARMSMOV.head())
#NI JSC-3A RMS MOA data
dataNIJSC3ARMSMOA = pd.read_excel('NIvNCD.xlsx', sheet_name='NI JSC-3A RMS MOA')
print(dataNIJSC3ARMSMOA.head())


#NI JSC-3B RMS MOH data
dataNIJSC3BRMSMOH = pd.read_excel('NIvNCD.xlsx', sheet_name='NI JSC-3B RMS MOH')
print(dataNIJSC3BRMSMOH.head())
#NI JSC-3B RMS MOV data
dataNIJSC3BRMSMOV = pd.read_excel('NIvNCD.xlsx', sheet_name='NI JSC-3B RMS MOV')
print(dataNIJSC3BRMSMOV.head())
#NI JSC-3B RMS MOA data
dataNIJSC3BRMSMOA = pd.read_excel('NIvNCD.xlsx', sheet_name='NI JSC-3B RMS MOA')
print(dataNIJSC3BRMSMOA.head())


pyo.init_notebook_mode(connected=True)

dataJSC3MWATTS['MWATTS'] = dataJSC3MWATTS['MWATTS'].div(200)

#JSC 3 Overall MWATTS
lineJSCMWATTS = go.Scatter(x=dataJSC3MWATTS['TIME'], y=dataJSC3MWATTS['MWATTS'], name='JSC 3 MWATTS')

#X or Horizontal Axis of both 3A & 3B sensors
lineNCDJSC3BRMSX = go.Scatter(x=dataNCDJSC3BRMS['TIME'], y=dataNCDJSC3BRMS['X RMS'], name='NCD 3A X')
lineNIJSC3ARMSMOH = go.Scatter(x=dataNIJSC3ARMSMOH['TIME'], y=dataNIJSC3ARMSMOH['MOH RMS'], name='NI 3A MOH')
lineNCDJSC3ARMSX = go.Scatter(x=dataNCDJSC3ARMS['TIME'], y=dataNCDJSC3ARMS['X RMS'], name='NCD 3B X')
lineNIJSC3BRMSMOH = go.Scatter(x=dataNIJSC3BRMSMOH['TIME'], y=dataNIJSC3BRMSMOH['MOH RMS'], name='NI 3B MOH')

#Y or Vertical Axis of both 3A & 3B sensors
lineNCDJSC3BRMSY = go.Scatter(x=dataNCDJSC3BRMS['TIME'], y=dataNCDJSC3BRMS['Y RMS'], name='NCD 3A Y')
lineNIJSC3ARMSMOV = go.Scatter(x=dataNIJSC3ARMSMOV['TIME'], y=dataNIJSC3ARMSMOV['MOV RMS'], name='NI 3A MOV')
lineNCDJSC3ARMSY = go.Scatter(x=dataNCDJSC3ARMS['TIME'], y=dataNCDJSC3ARMS['Y RMS'], name='NCD 3B Y')
lineNIJSC3BRMSMOV = go.Scatter(x=dataNIJSC3BRMSMOV['TIME'], y=dataNIJSC3BRMSMOV['MOV RMS'], name='NI 3B MOV')

#Z or Axial Axis of both 3A & 3B sensors
lineNCDJSC3BRMSZ = go.Scatter(x=dataNCDJSC3BRMS['TIME'], y=dataNCDJSC3BRMS['Z RMS'], name='NCD 3A Z')
lineNIJSC3ARMSMOA = go.Scatter(x=dataNIJSC3ARMSMOA['TIME'], y=dataNIJSC3ARMSMOA['MOA RMS'], name='NI 3A MOA')
lineNCDJSC3ARMSZ = go.Scatter(x=dataNCDJSC3ARMS['TIME'], y=dataNCDJSC3ARMS['Z RMS'], name='NCD 3B Z')
lineNIJSC3BRMSMOA = go.Scatter(x=dataNIJSC3BRMSMOA['TIME'], y=dataNIJSC3BRMSMOA['MOA RMS'], name='NI 3B MOA')



#X or Horizontal Axis of both 3A & 3B sensors
datalinesX = [lineJSCMWATTS, lineNCDJSC3BRMSX, lineNIJSC3ARMSMOH, lineNCDJSC3ARMSX, lineNIJSC3BRMSMOH]

#Y or Vertical Axis of both 3A & 3B sensors
datalinesY = [lineJSCMWATTS, lineNCDJSC3BRMSY, lineNIJSC3ARMSMOH, lineNCDJSC3ARMSY, lineNIJSC3BRMSMOH]

#Z or Axial Axis of both 3A & 3B sensors
datalinesZ = [lineJSCMWATTS, lineNCDJSC3BRMSZ, lineNIJSC3ARMSMOA, lineNCDJSC3ARMSZ, lineNIJSC3BRMSMOA]


#X or Horizontal Axis of both 3A & 3B sensors
layoutLine= go.Layout(title='NCD v NI Ammonia Blowers 3A & 3B - RMS - X or Horizontal Axis')
fig = go.Figure(data=datalinesX, layout=layoutLine)
pyo.plot(fig)

#Y or Vertical Axis of both 3A & 3B sensors
layoutLine= go.Layout(title='NCD v NI Ammonia Blowers 3A & 3B - RMS - Y or Vertical Axis')
fig = go.Figure(data=datalinesY, layout=layoutLine)
pyo.plot(fig)

#Z or Axial Axis of both 3A & 3B sensors
layoutLine= go.Layout(title='NCD v NI Ammonia Blowers 3A & 3B - RMS - Z or Axial Axis')
fig = go.Figure(data=datalinesZ, layout=layoutLine)
pyo.plot(fig)



















