#opens text file for data output
file_written = open(r"C:\Users\PGCC Loaner\Documents\MAGSAT Data Lab\Written_data.txt", "r+")
#Input identity
file1 = open("C:\\Users\\PGCC Loaner\\Documents\\MAGSAT Data Lab\\80_01_01.dat")

#Read the first line of the data
line_num = 0
line= file1.readline()

#Loop through data file, to read every 600th line
while line:
    line_num+= 1
    if line_num == 1 or line_num % 600 == 0:
        #write the line to the output file
        file_written.write(line)

    #Read the next line from the input file
    line = file1.readline()

#close input and output files
file1.close()
file_written.close()
    
