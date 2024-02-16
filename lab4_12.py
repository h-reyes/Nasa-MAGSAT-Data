file1 = open('C:/Users/PGCC Loaner/Documents/MAGSAT Data Lab/80_01_01.dat', 'r')  # open file ('r' for read)
Lines = file1.readlines()        # read all lines from file to list of strings
#Column for each element of the data sheet
with open('80_01_01.dat', 'r') as f:
   for line in f:
      Time = int(line[0:8])
      Lambda = float(line[8:16])
      Phi = float(line[16:24])
      R = float(line[24:33])
      Bx = float(line[33:41])
      By = float(line[41:49])
      Bz = float(line[49:57])
      flag = int(line[57:62])
      print (Time, Lambda, Phi, R, Bx, By, Bz, flag)

file1.close()                    # close file

print('Done.')
