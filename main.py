import sys
import fileinput
#import man
import re


def get_number_of_samples(lines):
    return len(lines)


def get_start_timestamp(lines):
    for line in lines:
        if '<time>' in line:
            return line.replace('<time>', '').replace('</time>', '').replace(' ','')

def get_end_timestamp(lines):
    return lines[-1].replace('<time>', '').replace('</time>', '').replace(' ','')

    

def get_duration(lines):
    s = convert_to_seconds(str(get_end_timestamp(lines))) - convert_to_seconds(str(get_start_timestamp(lines)))
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
    

def get_distance():
    x = raw_input('Write in the length of the run in kilometers\n\n')
    return x    

def distance_and_time_to_pace(distance, time_in_seconds):
    rem = time_in_seconds % 60
    m = time_in_seconds/60
    pace = str(m).zfill(2) + str(rem).zfill(2)
    return pace

    

def convert_to_seconds(timestamp):
    # convert the timestamp to seconds
    ts = timestamp.split('T')
    print ts
    ts = ts[1]
    ts = re.sub('[^0-9:]','',ts).split(':')
    sec = int(ts[0])*3600 + int(ts[1])*60+int(ts[2])
    return sec

def set_date():
    print 'Write in todays date\n'
    ts = raw_input('On the form yy-mm-dd\n')
    return ts +'T'

def set_start_time():
    print 'Write the start time'
    st = raw_input('On the form hh:mm:ss')
    return st + 'Z'


def parse_coordinates():
    pass    



timestamps = []
coordinates = []
lines = [line.rstrip('\n') for line in open('Laffing_i_ghettoen.gpx')]
for l in lines:
    if '<time>' in l:
         timestamps.append(l)

    if '<trkpt' in l:
        coordinates.append(l.replace('<trkpt','').replace('>',''))


for elem in timestamps:
    print convert_to_seconds(elem)

for elem in coordinates:
    print elem

#print get_start_timestamp(timestamps)
#print get_end_timestamp(timestamps)
#print get_duration(timestamps)
#print get_distance()
"""
for i, line in enumerate(fileinput.input('Laffing_i_ghettoen.gpx', inplace=1)):
    if '<time>' in line:
        print line
    else:
        print line 
""" 
#     sys.stdout.write(line.replace('1','DD'))
#gpx_file = open('Laffing_i_ghettoen.gpx','r')
#for line in gpx_file.readlines():
#    if '<time>' in line:
#        print line
