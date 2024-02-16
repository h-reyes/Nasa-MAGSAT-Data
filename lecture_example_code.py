with open(r"C:/Users/PGCC Loaner/Documents/MAGSAT Data Lab/Reading_and_writing code.py", "r") as f:
    for line in f:
        Time = int(line[0:8])
        print (time)

        Lambda = float(line[8:16])

        Phi = float(line[16:24])

        #R=
        
        flag= int(line[57:62])
        print (Time, Lambda, Phi, Flag)

    file1.close()

    print("Done")
