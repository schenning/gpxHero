import sys
import fileinput

for i, line in enumerate(fileinput.input('Laffing_i_ghettoen.gpx', inplace=1)):
    sys.stdout.write(line.replace('X','1'))
#gpx_file = open('Laffing_i_ghettoen.gpx','r')
#for line in gpx_file.readlines():
#    if '<time>' in line:
#        print line
