def readData():
    file = open('../botPersonalInformation.dat', 'r')
    Lines = file.readlines()
    return Lines[3]