import sys
import fileinput
#import man
import re
import six
from math import radians, cos, sin, asin, sqrt
import datetime

class gpxObject:



    def __init__(self, gpx_filename):


        if not isinstance(gpx_filename, six.string_types):
            print "Could not open GPX file"
            raise NameError('Try again.')


        self.gpx = 0
        self.lines = [line.rstrip('\n') for line in open(gpx_filename)]
        self.timestamps = []
        self.coordinates = []
        for l in self.lines:
            if '<time>' in l:
                self.timestamps.append(l)

            if '<trkpt' in l:
                self.coordinates.append(l.replace('<trkpt','').replace('>',''))


        self.samples = self.get_number_of_samples()
        print self.samples

        self.start_timestamp = self.get_start_timestamp()

        print self.start_timestamp
        x = self.end_timestamp = self.get_end_timestamp()
        print self.end_timestamp

        #### Convert to seconds


        # convert timestamp to seconds
        ts = self.end_timestamp.split('T')
        ts = ts[1]
        ts = re.sub('[^0-9:]','',ts).split(':')
        sec_end = int(ts[0])*3600 + int(ts[1])*60+int(ts[2])
        # convert timestamp to seconds
        ts = self.start_timestamp.split('T')
        ts = ts[1]
        ts = re.sub('[^0-9:]','',ts).split(':')
        sec_start = int(ts[0])*3600 + int(ts[1])*60+int(ts[2])
        self.duration = sec_end - sec_start
        print self.duration
        #x = self.get_distance()
        #print x
        print str(datetime.timedelta(seconds=self.duration))
    def get_pace(self):
        pass
        print 'Not in use'
        raise 'Value Error'


    def get_distance(self):

        print 'hei'
        dist = 0
        lon = []
        lat = []     
        d = 0
        for coord in self.coordinates:
            tmp = re.compile(r'[^\d.]+')
            tmp = tmp.sub('',coord)
            lon.append(tmp[:9])
            lat.append(tmp[10:])


        for i in range(0,len(lon)-1,2):
            lon0 = float(lon[i])
            lon1 = float(lon[i+1])
            lat0 = float(lat[i])
            lat1 = float(lat[i+1])
            d += 2*asin(sqrt(sin((lat1-lat0)/2)**2 + cos(lat0)*cos(lat1) * sin((lon1-lon0)/2)**2))
            lon0, lat0, lon1, lat1 = map(radians, [lon0, lat0, lon1, lat1])
            # haversine formula 
            dlon = lon1 - lon0 
            dlat = lat1 - lat0 
            a = sin(dlat/2.0)**2 + cos(lat0) * cos(lat1) * sin(dlon/2.0)**2
            c = 2 * asin(sqrt(a))
            dist+= 6500*c



            
        return dist, d*6399


       

    def get_number_of_samples(self):
        return len(self.timestamps)



    def convert_to_seconds(self):
        # convert the timestamp to seconds
        ts = string.split('T')
        print ts
        ts = ts[1]
        ts = re.sub('[^0-9:]','',ts).split(':')
        sec = int(ts[0])*3600 + int(ts[1])*60+int(ts[2])
        return sec


    def get_start_timestamp(self):
        for line in self.lines:
            if '<time>' in line:
                return line.replace('<time>', '').replace('</time>', '').replace(' ','')

    def get_end_timestamp(self):
        return self.timestamps[-1].replace('<time>', '').replace('</time>', '').replace(' ','')

    

    def get_duration(self):
        x = self.get_end_timestamp()
        y = self.get_start_timestamp()
        print self.convert_to_seconds().get_end_timestamp()        

        return 0


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
    
        ts += str(h).zfill(2) +':' + str(m).zfill(2) + ':'+ str(s).zfill(2) + 'Z'
        return ts 
    

    def distance_and_time_to_pace(distance, time_in_seconds):
        rem = time_in_seconds % 60
        m = time_in_seconds/60
        pace = str(m).zfill(2) + str(rem).zfill(2)
        return pace


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


x = gpxObject('Laffing_i_ghettoen.gpx')



#for elem in x.timestamps:
#    print elem

#print x.get_number_of_samples()
"""
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
"""
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
