import pandas as pd;
import re;
import csv;
import json


f = open('files.json')
data = json.load(f)
print(data)
# load dataframe with path from json file
df = pd.read_csv(data['filepaths']['RetainingWalls1'])
firstInstance = df['GEOGRAPHICAL COORDINATE'][0]
coordinates = df['GEOGRAPHICAL COORDINATE']
splitInstance = re.split('[°\'"]+', firstInstance)


# strip whitespace
#for i in range(len(coordinates)):
#    coordinates.values[i] = coordinates.values[i].replace(" ", "")
longitude = []
latitude = []

# add two new columns for long and lat
for i in range(len(coordinates)):
    coordinates.values[i] = coordinates.values[i].split(',')
    latitude.append(coordinates.values[i][0])
    longitude.append(coordinates.values[i][1])

#  print(splitInstance)
#print(df['GEOGRAPHICAL COORDINATE'])
#for i in range(len(df['GEOGRAPHICAL COORDINATE'])):
#    df['GEOGRAPHICAL COORDINATE'].values[i] = splitInstance = re.split('[°\'"]+', df['GEOGRAPHICAL COORDINATE'].values[i])

# add longitude and latitude to new df column
df['Longitude'] = longitude
df['Latitude'] = latitude

dfLongitude = df['Longitude']
dfLatitude = df['Latitude']

# strip whitespace
for i in range(len(dfLongitude)):
    dfLongitude.values[i] = dfLongitude.values[i].replace(" ", "")
    dfLatitude.values[i] = dfLatitude.values[i].replace(" ", "")


print(df['GEOGRAPHICAL COORDINATE'])
print(df)

# to convert to decimal degrees
def decimalDegree(degree, minute, second, hemisphere):
    if hemisphere.lower() in ["w", "s", "west", "south"]:
        factor = -1.0
    elif hemisphere.lower() in ["n", "e", "north", "east"]:
        factor = 1.0
    else:
        raise ValueError("invalid hemisphere")

    return factor * (degree + (minute / 60) + (second / 3600))

# split into lists so as to separate degree, minute, second values
for i in range(len(dfLongitude)):
    dfLongitude.values[i] = re.split('[°\'"]+', dfLongitude.values[i])
    dfLatitude.values[i] = re.split('[°\'"]+', dfLatitude.values[i])  

# check if values are correct 
pd.set_option('display.max_rows', 100)
print(df)

# use function to convert to decimal degrees in place
for i in range(len(dfLongitude)):
    longValue = dfLongitude.values[i]
    latValue = dfLatitude.values[i]

    longValue = decimalDegree(float(longValue[0]), float(longValue[1]), float(longValue[2]), longValue[3])
    latValue = decimalDegree(float(latValue[0]), float(latValue[1]), float(latValue[2]), latValue[3])

    dfLongitude.values[i] = longValue
    dfLatitude.values[i] = latValue


print(df)



