import math
import os


def iptobin(ip):
        new = ip.split(".")
        binip = []
        str1=""
        for i in range(len(new)):
            binip.append( bin(int(float(new[i]))))
            strtmp = '%s' % binip[i]
            strtmp = strtmp[2:]

            if strtmp.isdigit():
                strtmp2='{:0>8}'.format(strtmp)
            else:
                print('Error string:\n %s\n consist non-digit chars' % strtmp)
                return 0
            str1=str1+strtmp2
            str1=str1+'.'
        str2=str1[:len(str1)-1]
        str1=""
        print('%s' % str2)
def errorcheck(ip):

    new = ip.split(".")
    if not len(new)==4:
        print("INPUT ERROR: ip must consit of 32 bits or 4 octets ")
        return True
    for i in range(len(new)):
        if not new[i].isdigit():
            print('INPUT ERROR: you must enter only digits')
            return True 
        if int(float(new[i]))>255:
            print('INPUT ERROR: ip octet must be < 255')
            return True
def printbanner():
    print("██╗██████╗ ██╗   ██╗██╗  ██╗ ")
    print("██║██╔══██╗██║   ██║██║  ██║ ")
    print("██║██████╔╝██║   ██║███████║ ")
    print("██║██╔═══╝ ╚██╗ ██╔╝╚════██║ ")
    print("██║██║      ╚████╔╝      ██║ ")
    print("╚═╝╚═╝       ╚═══╝       ╚═╝ \n")
    print("██████╗ ██╗███╗   ██╗        ")
    print("██╔══██╗██║████╗  ██║        ")
    print("██████╔╝██║██╔██╗ ██║        ")
    print("██╔══██╗██║██║╚██╗██║        ")
    print("██████╔╝██║██║ ╚████║        ")
    print("╚═════╝ ╚═╝╚═╝  ╚═══╝        \n\n")
    return 0


while True:
    
    rows, columns = os.popen('stty size', 'r').read().split()
    if float(rows)>=12 and float(columns)>=28:
        printbanner()
    

    ip1 = input("Please enter IP1: ")
    inperr1=errorcheck(ip1)
    if inperr1:
        continue
    ip2 = input("Please enter IP2: ")
    inperr2=errorcheck(ip2)
    if inperr2:
        continue
    if not inperr1 and not inperr2:
        iptobin(ip1)
        iptobin(ip2)
        break


