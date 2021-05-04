from pickle import *
import time
import random
import os
from tickets import *
from rail import *

def menu():
    tr = rail()
    tk = tickets()
    print("\t\t\t\tWELCOME TO INDIAN RAILWAYS")
    time.sleep(0.5)
    print("\n\n\t\t\t\tWELCOME TO SIDDHU AGENCY".center(80))
    while True:
        print("=" * 80)
        print(" \t\t\t\t INDIAN RAILWAY")
        print("=" * 80)
        print("\t\t\t1. ADMIN")
        print("\t\t\t2. PASSENGERS ")
        print("=" * 80)
        c = int(input("\t\t\tENTER YOUR CHOICE : "))
        if c==1:
            while True:
                print("=" * 80)
                print(" \t\t\t\t INDIAN RAILWAY")
                print("=" * 80)
                print("\t\t\t1. UPDATE TRAIN DETAILS.")
                print("\t\t\t2. TRAIN DETAILS. ")
                print("\t\t\t3. RESERVATION OF TICKETS.")
                print("\t\t\t4. CANCELLATION OF TICKETS. ")
                print("\t\t\t5. DISPLAY PNR STATUS.")
                print("\t\t\t6. QUIT.")
                print("** - office use......")
                ch = int(input("\t\t\tENTER YOUR CHOICE : "))
                print("\n\n\n\n\n\t\t\t\t\t\t\tLOADING. .")
                if ch == 1:
                    j = "*****"
                    r = input("\n\t\t\t\tENTER THE PASSWORD: ")
                    if (j == r):
                        x='y'
                        while(x=='y') :
                            fout = open("trdetails.dat", "ab")
                            tr.getinput()
                            dump(tr, fout)
                            fout.close()
                            print("\n\t\tUPDATING TRAIN LIST PLEASE WAIT . .")
                            time.sleep(0.5)
                            print("SUCCESSFULLY UPDATED".center(80))
                            x='z'
                        continue
                    elif (j < r):
                        print("WRONG PASSWORD".center(80))
                elif ch == 2:
                    fin = open("trdetails.dat", 'rb')
                    if not fin:
                        print("ERROR")
                    else:
                        try:
                            while True:
                                print("\t\t\t\tTRAIN DETAILS")
                                tr = load(fin)
                                tr.output()

                                input("PRESS ENTER TO VIEW NEXT TRAIN DETAILS")
                                os.system('clear')
                        except EOFError:
                            pass
                elif ch == 3:
                    print("\t\t\t\tRESERVATION OF TICKETS")
                    print(tk.reservation())
                elif ch == 4:
                    print("\t\t\t\tCANCELLATION OF TICKETS")
                    print(tk.cancellation())
                elif ch == 5:
                    print("PNR STATUS".center(80))
                    print(tk.display())
                elif ch == 6:
                    end()
                input("PRESS ENTER TO GO TO BACK MENU".center(80))
                os.system('clear')

        else:
                while True:
                    print("=" * 80)
                    print(" \t\t\t\t INDIAN RAILWAY")
                    print("=" * 80)
                    print("\t\t\t1. TRAIN DETAILS. ")
                    print("\t\t\t2. RESERVATION OF TICKETS.")
                    print("\t\t\t3. CANCELLATION OF TICKETS. ")
                    print("\t\t\t4. DISPLAY PNR STATUS.")
                    print("\t\t\t5. QUIT.")
                    ch = int(input("\t\t\tENTER YOUR CHOICE : "))
                    print("\n\n\n\n\n\t\t\t\t\t\t\tLOADING. .")
                    if ch == 1:
                        fin = open("trdetails.dat", 'rb')
                        if not fin:
                            print("ERROR")
                        else:
                            try:
                                while True:
                                    print("\t\t\t\tTRAIN DETAILS")
                                    tr = load(fin)
                                    tr.output()

                                    input("PRESS ENTER TO VIEW NEXT TRAIN DETAILS")
                                    os.system('clear2')
                            except EOFError:
                                pass
                    elif ch == 2:
                        print("\t\t\t\tRESERVATION OF TICKETS")
                        print(tk.reservation())
                    elif ch == 3:
                        print("\t\t\t\tCANCELLATION OF TICKETS")
                        print(tk.cancellation())
                    elif ch == 4:
                        print("PNR STATUS".center(80))
                        print(tk.display())
                    elif ch == 5:
                        end()
                    input("PRESS ENTER TO GO TO BACK MENU".center(80))
                    os.system('clear')

def end():
        print("\t\t\t\t\n\n\n\n\n\t THANK YOU.....")
        print("\n\t\t\tDONE BY: -")
        print("\t\t\t\t  SIDDHU")
        print("\n\n\t\t\t\t\t\t\tLOADING. .")
        time.sleep(0.5)
        print(".")
        os.system('clear')
menu()