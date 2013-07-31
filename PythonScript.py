#! /usr/bin/python

from sys import platform as opsys
import os
import time
def clearscreen():
    if opsys == "linux2":
        os.system("clear")
    elif opsys == "win32" or opsys == "cygwin":
        os.system("cls")
cor = "n"
re = 0
while (cor != "y") or (cor != "yes"):
    clearscreen()
    print " "
    print "===========Realm of the mad god Damage Calculator v0.1 ==========="
    print "                                                   by Ethan Robinson"
    print " "
    if re == 1:
        print "Please re-enter your stats..."
        print " "
        re = 0
    while True:
        try:
            att = input("Please enter your attack stats: ")
            break
        except (NameError, SyntaxError):
            print " "
            print "Quit trying to crash my program."
            print "No strings of text, letters, or negative numbers"
            print " "
    while True:
        try:
            minb = input("Please enter the minimum damage your weapon deals: ")
            break
        except (NameError, SyntaxError):
            print " "
            print "Quit trying to crash my program." 
            print "No strings of text, letters, or negative numbers"
            print " "
    while True:
        try:
            maxb = input("Please enter the maximum damage your weapon deals: ")
            break
        except (NameError, SyntaxError):
            print " "
            print "Quit trying to crash my program." 
            print "No strings of text, letters, or negative numbers"
            print " "
    while True:
        try:
            dext = input("Please enter your dexterity stat: ")
            break
        except (NameError, SyntaxError):
            print " "
            print "Quit trying to crash my program." 
            print "No strings of text, letters, or negative numbers"
            print " "
    while True:
        try:
            wiza = input("Please enter the your wisdom stat you have: ")
            break 
        except (NameError, SyntaxError):
            print " "
            print "Quit trying to crash my program."
            print "No strings of text, letters, or negative numbers"
            print " "
    while True:
        try:
            vita = input("Please enter the amount of vitality you have: ")
            break
        except (NameError, SyntaxError):
            print " "
            print "Quit trying to crash my program." 
            print "No strings of text, letters, or negative numbers"
            print " "
    clearscreen()
    print "===========Realm of the mad god Damage Calculator v0.1 ==========="
    print "                                                   by Ethan Robinson"
    print "Your attack stats are ", att
    print "The minimum amount of damage your weapon deals is ", minb
    print "The maximum amount of damage your weapon deals is ", maxb
    print "Your dexteritiy is ", dext
    print "Your wizdom is ", wiza
    print "Your vitality is ", vita
    print " "
    cor = raw_input("Is this correct?: ")
    cor = cor.lower()
    if cor == "n":
        re = 1
        clearscreen()
    elif cor != "n" and cor != "no" and cor != "dick" and cor != "yes" and cor != "y":
        re = 0
        clearscreen()
        print "Quit trying to crash my program you damn NIGTITSFUCK!!!"
        time.sleep(2)
        clearscreen()
    elif cor == "y" or cor == "yes":
        break
    else:
        re = 0
        clearscreen()
        print " "
        print " "
        print " "
        print " "
        print " "
        print "                  You did not enter yes or no..."
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        time.sleep(3)
        clearscreen()
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print "                       You little FUCK!"
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        time.sleep(3)
        clearscreen()
        print " "
        print " " 
        print " "
        print "Out of all the things you could enter..."
        print " "
        print " "
        print " "
        print " "
        print " "
        print " " 
        print "                              YOU GAVE ME DICK!!!"
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        time.sleep(3)
        clearscreen()
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print "                                  ."
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        time.sleep(1)
        clearscreen()
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print "                                  . ."
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        time.sleep(1)
        clearscreen()
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print "                                  . . ."
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        print " "
        time.sleep(2)
        clearscreen()
        print "Equals banana!!!"
        print " "
        print " "
        print """                              -    .|||||."""
        print """                                  |||||||||"""
        print """                          -      ||||||  ."""
        print """                              -  ||||||   >"""
        print """                                ||||||| -/"""
        print """                           --   ||||||'("""
        print """                        -       .'      \""""
        print """                             .-'    | | |"""
        print """                            /        \ \ \""""
        print """              --        -  |      `---:.`.\""""
        print """             ____________._>           \\_\\____ ,--.__"""
        print """  --    ,--""           /    `-   .     |)_)    '\     '\ """
        print """       /  "             |      .-'     /          \      '\""""
        print """     ,/                  \           .'            '\     |"""
        print """     | "   "   "          \         /                '\,  /"""
        print """     |           " , =_____`-.   .-'_________________,--"""""
        print """   - |  "    "    /"/'      /\>-' ( <"""
        print """     \  "      ",/ /    -  ( <    |\_)"""
        print """      \   ",",_/,-'        |\_)"""
        print """   -- -'-;.__:-'"""
        raw_input()
        clearscreen()
#########################Functions#################################

#Damage calculator
def dam(mindam, maxdam, atk):
    minba = mindam * ((0.5 + atk) / 50)
    maxba = maxdam * ((0.5 + atk) / 50)
    av = (minba + maxba) / 2
    print "Maximum Damage = %.1f" % (maxba)
    print "Minumum Damage = %.1f" % (minba)
    print "Average Damage = %.1f" % (av)
    
#Dexterity calculator
def dex(dexter):
    aps = 1.5 + (6.5 * dexter / 75)
    print "Shots/s = %.1f" % (aps)
    
#Wisdom calculator
def wiz(wizb):
    wix = wizb * .06
    print "Mana Regeneration = %.1f" % (wix)

#Health per second Calculator
def vit(vitb):
    vix = vitb * .12 + 1
    print "Health Regeneration = %.1f" % (vix)

#Damage per second calculator
def dps(minbb, maxbb, atka, dexa):
    minba = minbb * ((0.5 + atka) / 50)
    maxba = maxbb * ((0.5 + atka) / 50)
    av = (minbb + maxbb) / 2
    aps = 1.5 + (6.5 * dexa / 75)
    dpsa = av * aps
    print "DPS = %.1f." % (dpsa)

########################################################################

clearscreen()
print "Okay, please wait while we calculate."
time.sleep(1)
clearscreen()
print "Okay, please wait while we calculate.."
time.sleep(1)
clearscreen()
print "Okay, please wait while we calculate..."
time.sleep(1.3)
clearscreen()
print "=============Results========================================================="
print " "
dam(minb, maxb, att)
dex(dext)
dps(minb, maxb, att, dext)
wiz(wiza)
vit(vita)
print " "
raw_input("Press Return to exit: ")
exit()
