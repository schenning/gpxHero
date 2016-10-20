import gpxpy.parser as parser
import numpy as np




def noise(n):
    nois = np.random.normal(0,1,n)
    return nois


  
def myround(a, decimals=0):
     return np.around(a-10**(-(decimals+5)), decimals=decimals) 




def conv(sec):
    pass








gpx_file = open( 'Laffing_i_ghettoen.gpx', 'r' )

gpx_parser = parser.GPXParser( gpx_file )
gpx_parser.parse()

gpx_file.close()

gpx = gpx_parser.parse()

x = []

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            #print 'Point at ({0},{1}) -> {2}, {3}'.format( point.latitude, point.longitude, point.elevation, point.time )
            
            x.append(point.time)

for elem in x:
    print str(elem)

print len(x)

print myround(noise (100))
