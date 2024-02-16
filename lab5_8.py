#Imports Square Root function
from math import sqrt
#defines file reading the data and the output file for writing
file_written = open(r'C:/Users/PGCC Loaner/Documents/MAGSAT Data Lab/lab5_8.txt', 'r+')
file1 = open(r'C:/Users/PGCC Loaner/Documents/MAGSAT Data Lab/80_01_01.dat', 'r')  # open file ('r' for read)
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
      absolute_b= sqrt(pow(Bx,2)+pow(By,2)+pow(Bz,2))
      #selects only three elements
      lan_abso=Time, Lambda, absolute_b
      #writes to text file and seperates the data into seperate lines
      file_written.write(str(lan_abso)+"\n")


file1.close()                    # close files
file_written.close()
print('Done.')
