from pickle import *
import time
import random
import os
from tickets import *
from rail import *

class rail:
    def __init__(self):
        self.trainno = 0
        self.no_ofac1stclass = 0
        self.no_ofac2ndclass = 0
        self.no_ofac3rdclass = 0
        self.no_ofsleeper = 0
        self.trainname = ""
        self.startingpt = ""
        self.destination = ""
 # _______________________GETS INPUT__________________
    def getinput(self):
        print("\t\t\t  ENTER THE TRAIN DETAILS\n\n\n\n")
        self.trainname = input("ENTER THE TRAIN NAME : ")
        self.trainno = int(input("ENTER THE TRAIN NUMBER: "))
        self.no_ofac1stclass = int(input("ENTER NO_OF AC FIRST CLASS SEATS TO BE RESERVED : "))
        self.no_ofac2ndclass = int(input("ENTER NO_OF AC SECOND CLASS SEATS TO BE RESERVED : "))
        self.no_ofac3rdclass = int(input("ENTER NO_OF AC THIRD CLASS SEATS TO BE RESERVED : "))
        self.no_ofsleeper = int(input("ENTER NO_OF SLEEPER CLASS SEATS TO BE RESERVED : "))
        self.startingpt = input("ENTER THE STARTING POINT : ")
        self.destination = input("ENTER THE DESTINATION POINT : ")
        os.system('clear')
# ___________________DISPALYS  DATA_________________
    def output(self):
        print("\nTHE ENTERED TRAIN NAME IS : ", self.trainname)
        print("THE TRAIN  NUMBER IS : ", self.trainno)
        print("STARTING POINT ENTERED IS : ", self.startingpt)
        print("DESTINATION POINT ENTERED IS : ", self.destination)
        print("NO_OF AC FIRST CLASS SEATS RESERVED ARE :", self.no_ofac1stclass)
        print("NO_OF AC SECOND CLASS SEATS RESERVED ARE :", self.no_ofac2ndclass)
        print("NO_OF AC THIRD CLASS SEATS RESERVED ARE :", self.no_ofac3rdclass)
        print("NO_OF SLEEPER CLASS SEATS RESERVED ARE :", self.no_ofsleeper)
 # _______RETURNS TRAIN NAME,NUMBER,CLASS,STARTING PT.,DESTINATION____________
    def gettrainname(self):
        return (self.trainname)
    def gettrainno(self):
        return (self.trainno)
    def getno_ofac1stclass(self):
        return (self.no_ofac1stclass)
    def getno_ofac2ndclass(self):
        return (self.no_ofac2ndclass)
    def getno_ofac3rdclass(self):
        return (self.no_ofac3rdclass)
    def getno_ofsleeper(self):
        return (self.no_ofsleeper)
    def getstartingpt(self):
        return (self.startingpt)
    def getdestination(self):
        return (self.destination)