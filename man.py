import gpxpy.parser as parser
import numpy as np
import sys
import fileinput
import re


# TODO list:
# Take in from argv
# Heart rate
# convert to seconds
# discontinue project 



def get_number_of_samples(gpx_file):
    samples = len(parse_gpx(gpx_file))
    return samples

def get_start_timestamp(gpx_file):
    samples = parse_gpx(gpx_file)
    return samples[0]

def get_end_timestamp(gpx_file):
    samples = parse_gpx(gpx_file)
    return samples[-1]
    

def get_duration(gpx_file):
    s = convert_to_seconds(str(get_end_timestamp(gpx_file))) - convert_to_seconds(str(get_start_timestamp(gpx_file)))
    return s


def get_date_from_timestamp(timestamp):
    date = timestamp.split('T')[0] + 'T'
    return date

def convert_to_timestamp(seconds,timestamp):
    ts = ''
    ts += get_date_from_timestamp(timestamp)
    rem_h = seconds%3600
    h = seconds/3600
    s = rem_h%60
    m = rem_h/60
    
    ts += str(h).zfill(2)+':' + str(m).zfill(2) +':'+ str(s).zfill(2) + 'Z'
    return ts 
    



def convert_to_seconds(timestamp):
    # convert the timestamp to seconds
    ts = timestamp.split('T')
    print ts
    ts = ts[1]
    ts = re.sub('[^0-9:]','',ts).split(':')
    sec = int(ts[0])*3600 + int(ts[1])*60+int(ts[2])
    return sec


    
    
    


def parse_gpx(gpx_file):

    gpx_file = open( 'Laffing_i_ghettoen.gpx', 'r' )
    gpx_parser = parser.GPXParser( gpx_file )
    gpx_parser.parse()
    gpx_file.close()
    gpx = gpx_parser.parse()
    x = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                x.append(point.time)

    return x

def noise(n):
    return np.random.normal(0,1,n)
    


  
def myround(a, decimals=0):
     return np.around(a-10**(-(decimals+5)), decimals=decimals) 




def conv(sec, sub):
    # --> string of timestamp
    # <-- modified string with sub seconds subtracted on each sample
    #  

    pass

gpx_file = parse_gpx('Laffing_i_ghettoen.gpx')
for elem in gpx_file:
    print elem.replace(' ','T')   
#print get_duration(gpx_file)
print get_end_timestamp(gpx_file)
#x =convert_to_seconds('2016-10-16T14:54:49Z')
#print convert_to_timestamp(x, '2016-10-16T14:54:49Z')



