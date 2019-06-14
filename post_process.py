#### py codes to postprocess flexpart data
import os,sys,glob
import calendar
import time
from datetime import date

#import pygrib
#from gribapi import *
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import numpy as np
import struct
from read_header import *

#####Info to user
startdate=date.toordinal(date(2018,1,1))
print('Startdate = ' + str(startdate))

### Current working directory
# ## move to output directory
os.chdir(os.getcwd()+"/../../FLEXPART/output/test_data/")
path =os.getcwd()
#
# ##loading trajectory and dates file
f_traj=np.genfromtxt(path+'/trajectories.txt', delimiter='\n', skip_header=12)
f_date=np.loadtxt(path+'/dates')

file_header=path+'/header'
read_header(file_header,path,0)

#
# for file in glob.glob("grid_time_*"):
#     #print(file)
#     read_header(file)
    #grb=f_grib.open.select()[0]
    #data=grb.values
