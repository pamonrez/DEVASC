import csv
samplefile = open ('cvsfile.cvs')
samplereader = csv.reader(samplefile)
sampledata = list(samplefile)
print(sampledata)
