import numpy as np 
from scipy.io.netcdf import netcdf_file
import matplotlib.pyplot as plt
import json
with netcdf_file(r'D:\github\MSR-2.nc', mmap=False) as f:
    var = f.variables
print(var['longitude'].units)
print(var['latitude'].units)
latitude_index = np.searchsorted(var['latitude'].data,-41.28)
longitude_index = np.searchsorted(var['longitude'].data,174.77) 
print('longitude_index:',longitude_index)
print('latitude_index:',latitude_index)
data = var['Average_O3_column'][:, latitude_index, longitude_index][:]
Jan_zon = data[::12]
July_zon = data[6::12]
time = var['time'][:]
jan_time=time[::12]
july_time=time[6::12]
plt.plot(var['time'].data, data,label = 'Все время') 
plt.plot(jan_time, Jan_zon, label = 'Январь')
plt.plot(july_time, July_zon, label = 'Июль')
plt.legend()
plt.grid()
plt.savefig('ozon.png')


d = {
  "city": "Wellington",
  "coordinates": "-41.28,174.77",
  "jan": {
    "min": float(np.min(Jan_zon)),
    "max": float(np.max(Jan_zon)),
    "mean": float(np.mean(Jan_zon)),
  },
  "jul": {
    "min": float(np.min(July_zon)),
    "max": float(np.max(July_zon)),
    "mean": float(np.mean(July_zon)),
  },
  "all": {
    "min": float(np.min(data)),
    "max": float(np.max(data)),
    "mean":float(np.mean(data)),
  }
}
with open('ozon.json', 'w') as f:
    json.dump(d, f, indent=2)
with open('ozon.json', 'r') as f:
    print(f.read())
    f.seek(0)