import sys
import fileinput
import man
for i, line in enumerate(fileinput.input('Laffing_i_ghettoen.gpx', inplace=1)):
    if '<time>' in line:
        l =  convert_to_seconds(line)
        print line
    else:
        print line 
 
#     sys.stdout.write(line.replace('1','DD'))
#gpx_file = open('Laffing_i_ghettoen.gpx','r')
#for line in gpx_file.readlines():
#    if '<time>' in line:
#        print line
