import gpxpy.parser as parser
import numpy as np
import sys
import fileinput
import re


# TODO list:
# Take in from argv
# Heart rate
# convert to seconds
 



def get_number_of_samples(gpx_file):
    samples = len(parse(gpx_file))
    return samples

def get_start_timestamp(gpx_file):
    samples = parse(gpx_file)
    return samples[0]

def get_end_timestamp(gpx_file):
    samples = parse(gpx_file)
    return samples[-1]

def get_date_from_timestamp(timestamp):
    date = timestamp.split('T')[0] + 'T'
    return date

def convert_to_timestamp(seconds,timestamp):
    ts = ''
    ts+=get_date(timestamp)
    
    



def convert_to_seconds(timestamp):
    # convert the timestamp to seconds
    ts = timestamp.split('T')
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



print convert_to_seconds('2016-10-16T14:54:49Z')




