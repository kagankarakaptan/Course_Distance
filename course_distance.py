# -*- coding: utf-8 -*-
import math
from operator import pos
from tkinter import *
from tkinter import ttk
import tkinter as tk

app = Tk()
app.title("Course and Distance Calculator")
app.geometry("650x300")
frame = ttk.Frame(app, padding=20)
frame.grid()


pos1latDeg = tk.StringVar()

pos1latMin = StringVar()
pos1latSec = StringVar()
pos1latDir = StringVar()

pos1lonDeg = StringVar()
pos1lonMin = StringVar()
pos1lonSec = StringVar()
pos1lonDir = StringVar()

pos2latDeg = StringVar()
pos2latMin = StringVar()
pos2latSec = StringVar()
pos2latDir = StringVar()

pos2lonDeg = StringVar()
pos2lonMin = StringVar()
pos2lonSec = StringVar()
pos2lonDir = StringVar()


def calculate():

    pos1latDeg = pos1latDeg_Entry.get()
    pos1latMin = pos1latMin_Entry.get()
    pos1latSec = pos1latSec_Entry.get()
    pos1latDir = pos1latDir_Entry.get()

    pos1lonDeg = pos1lonDeg_Entry.get()
    pos1lonMin = pos1lonMin_Entry.get()
    pos1lonSec = pos1lonSec_Entry.get()
    pos1lonDir = pos1lonDir_Entry.get()

    pos2latDeg = pos2latDeg_Entry.get()
    pos2latMin = pos2latMin_Entry.get()
    pos2latSec = pos2latSec_Entry.get()
    pos2latDir = pos2latDir_Entry.get()

    pos2lonDeg = pos2lonDeg_Entry.get()
    pos2lonMin = pos2lonMin_Entry.get()
    pos2lonSec = pos2lonSec_Entry.get()
    pos2lonDir = pos2lonDir_Entry.get()

    lat1 = float(pos1latDeg) + float(pos1latMin)/60 + float(pos1latSec)/3600
    long1 = float(pos1lonDeg) + float(pos1lonMin)/60 + float(pos1lonSec)/3600
    lat2 = float(pos2latDeg) + float(pos2latMin)/60 + float(pos2latSec)/3600
    long2 = float(pos2lonDeg) + float(pos2lonMin)/60 + float(pos2lonSec)/3600
    if(pos1latDir == "S" or pos1latDir == "W"):
        lat1 *= -1
    if(pos1lonDir == "S" or pos1lonDir == "W"):
        long1 *= -1
    if(pos2latDir == "S" or pos2latDir == "W"):
        lat2 *= -1
    if(pos2lonDir == "S" or pos2lonDir == "W"):
        long2 *= -1
    d_lat = float(lat2) - float(lat1)
    d_long = float(long2) - float(long1)
    d_to_r = float(math.pi / 180.0)
    d_lat_rad = d_lat * d_to_r
    d_long_rad = d_long * d_to_r
    a = math.sin(d_lat_rad/2) ** 2 + math.sin(d_long_rad/2) ** 2 * \
        math.cos(lat1 * d_to_r) * math.cos(lat2 * d_to_r)
    b = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    R = 3443.9308855292
    d = b * R
    c = math.atan2(d_long_rad, d_lat_rad) * 57.2957795

    cStr_Label.config(text=str(c))
    dStr_Label.config(text=str(d))


tk.Label(frame, text="POSITION 1", fg="blue").grid(column=0, row=0)
tk.Label(frame, text="DEGREE", fg="purple").grid(column=1, row=0)
tk.Label(frame, text="MINUTE", fg="purple").grid(column=2, row=0)
tk.Label(frame, text="SECOND", fg="purple").grid(column=3, row=0)
tk.Label(frame, text="DIRECTION", fg="purple").grid(column=4, row=0)

tk.Label(frame, text="LATITUDE: ", fg="orange").grid(column=0, row=1)

pos1latDeg_Entry = tk.Entry(frame, textvariable=pos1latDeg)
pos1latDeg_Entry.grid(column=1, row=1)
pos1latMin_Entry = tk.Entry(frame, textvariable=pos1latMin)
pos1latMin_Entry.grid(column=2, row=1)
pos1latSec_Entry = tk.Entry(frame, textvariable=pos1latSec)
pos1latSec_Entry.grid(column=3, row=1)
pos1latDir_Entry = tk.Entry(frame, textvariable=pos1latDir)
pos1latDir_Entry.grid(column=4, row=1)

tk.Label(frame, text="LONGITUDE: ", fg="orange").grid(column=0, row=2)

pos1lonDeg_Entry = tk.Entry(frame, textvariable=pos1lonDeg)
pos1lonDeg_Entry.grid(column=1, row=2)
pos1lonMin_Entry = tk.Entry(frame, textvariable=pos1lonMin)
pos1lonMin_Entry.grid(column=2, row=2)
pos1lonSec_Entry = tk.Entry(frame, textvariable=pos1lonSec)
pos1lonSec_Entry.grid(column=3, row=2)
pos1lonDir_Entry = tk.Entry(frame, textvariable=pos1lonDir)
pos1lonDir_Entry.grid(column=4, row=2)

tk.Label(frame, text="").grid(column=0, row=3)

tk.Label(frame, text="POSITION 2", fg="blue").grid(column=0, row=4)
tk.Label(frame, text="DEGREE", fg="purple").grid(column=1, row=4)
tk.Label(frame, text="MINUTE", fg="purple").grid(column=2, row=4)
tk.Label(frame, text="SECOND", fg="purple").grid(column=3, row=4)
tk.Label(frame, text="DIRECTION", fg="purple").grid(column=4, row=4)

tk.Label(frame, text="LATITUDE: ", fg="orange").grid(column=0, row=5)

pos2latDeg_Entry = tk.Entry(frame, textvariable=pos2latDeg)
pos2latDeg_Entry.grid(column=1, row=5)
pos2latMin_Entry = tk.Entry(frame, textvariable=pos2latMin)
pos2latMin_Entry.grid(column=2, row=5)
pos2latSec_Entry = tk.Entry(frame, textvariable=pos2latSec)
pos2latSec_Entry.grid(column=3, row=5)
pos2latDir_Entry = tk.Entry(frame, textvariable=pos2latDir)
pos2latDir_Entry.grid(column=4, row=5)

tk.Label(frame, text="LONGITUDE: ", fg="orange").grid(column=0, row=6)

pos2lonDeg_Entry = tk.Entry(frame, textvariable=pos2lonDeg)
pos2lonDeg_Entry.grid(column=1, row=6)
pos2lonMin_Entry = tk.Entry(frame, textvariable=pos2lonMin)
pos2lonMin_Entry.grid(column=2, row=6)
pos2lonSec_Entry = tk.Entry(frame, textvariable=pos2lonSec)
pos2lonSec_Entry.grid(column=3, row=6)
pos2lonDir_Entry = tk.Entry(frame, textvariable=pos2lonDir)
pos2lonDir_Entry.grid(column=4, row=6)

tk.Label(frame, text="").grid(column=0, row=7)

tk.Button(frame, text="CALCULATE", command=calculate,
          bg="#F27A1A").grid(column=0, row=8)

tk.Label(frame, text="").grid(column=0, row=9)

tk.Label(frame, text="COURSE: ", fg="green").grid(column=0, row=10)
cStr_Label = tk.Label(frame, text="CALCULATE TO SEE", bg="yellow", fg="red")
cStr_Label.grid(column=1, row=10)

tk.Label(frame, text="DISTANCE: ", fg="green").grid(column=0, row=11)
dStr_Label = tk.Label(frame, text="CALCULATE TO SEE", bg="yellow", fg="red")
dStr_Label.grid(column=1, row=11)

app.mainloop()
