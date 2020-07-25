#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 12:58:08 2020

@author: CalebBorwick
"""
#imports
import pyautogui
import webbrowser
import time


#variables 
#change the time variable for your time slot
WorkoutTime = "6:30 am"
loc = "Remington"
fname = "ENTER FIRST NAME HERE"
lname = "ENTER LAST NAME HERE"
dobD="ENTER DAY HERE"
dobY="ENTER YEAR HERE"
dobM = "Nov"
email="ENTER EMAIL HERE @gmail.com"
phone="4036810031"



#open website
def OpenWeb():
    webbrowser.open_new("https://www.ymcacalgary.org/appointments/")
    time.sleep(3)

#scrolls to bottom of page
def scroll():
    pyautogui.moveTo(200,400,0.5)
    pyautogui.click()
    pyautogui.hotkey('alt', 'down')
    time.sleep(.5)


#scrolls to proper location
def location():
    if loc == "Brookfield":
        pyautogui.moveTo(200,410,0.5)
    elif loc == "Gray":
        pyautogui.moveTo(200,435,0.5)
    elif loc == "Melcor":
        pyautogui.moveTo(200,460,0.5)
    elif loc == "Remington":
        pyautogui.moveTo(200,480,0.5)
    elif loc == "Saddletowne":
        pyautogui.moveTo(200,500,0.5)
    elif loc == "Shane":
        pyautogui.moveTo(200,525,0.5)
    elif loc == "Shawnessy":
        pyautogui.moveTo(200,550,0.5)
    elif loc == "South Health":
        pyautogui.moveTo(200,575,0.5)
    pyautogui.click()


    

#scrolls to proper month
def month():
    pyautogui.moveTo(190,535,0.5)
    pyautogui.click()
    pyautogui.moveTo(190,780,0.5)
    if dobM == "Jan":
        pyautogui.moveTo(190,530,0.5)
    elif dobM == "Feb":
        pyautogui.moveTo(190,560,0.5)
    elif dobM == "Mar":
        pyautogui.moveTo(190,580,0.5)
    elif dobM == "Apr":
        pyautogui.moveTo(190,600,0.5)
    elif dobM == "May":
        pyautogui.moveTo(190,630,0.5)
    elif dobM == "Jun":
        pyautogui.moveTo(190,650,0.5)
    elif dobM == "Jul":
        pyautogui.moveTo(190,670,0.5)
    elif dobM == "Aug":
        pyautogui.moveTo(190,700,0.5)
    elif dobM == "Sep":    
        pyautogui.moveTo(190,720,0.5)
    elif dobM == "Oct":
        pyautogui.moveTo(190,740,0.5)
    elif dobM == "Nov":
        pyautogui.moveTo(190,760,0.5)
    elif dobM == "Dec":
        pyautogui.moveTo(190,780,0.5)
    pyautogui.click()

#auto fill
def fill():
    pyautogui.press('tab')
    pyautogui.write(dobD,0.15)
    pyautogui.press('tab')
    pyautogui.write(dobY,0.15)
    pyautogui.press('tab')
    pyautogui.write(email,0.15)
    pyautogui.press('tab')
    pyautogui.write(phone,0.15)

#sets time slot
def timeSlot():
    time.sleep(0.5)
    if WorkoutTime == "6:30 am":
        pyautogui.moveTo(500,565,0.5)
    elif WorkoutTime =="7:30 am":
        pyautogui.moveTo(500,580,0.5)
    elif WorkoutTime =="8:30 am":
        pyautogui.moveTo(500,600,0.5)
    elif WorkoutTime =="9:30 am":
        pyautogui.moveTo(500,625,0.5)
    elif WorkoutTime =="10:30 am":
        pyautogui.moveTo(500,645,0.5)
    elif WorkoutTime =="11:30 am":
        pyautogui.moveTo(500,660,0.5)
    elif WorkoutTime =="12:30 pm":
        pyautogui.moveTo(500,675,0.5)
    elif WorkoutTime =="1:30 pm":
        pyautogui.moveTo(500,690,0.5)
    elif WorkoutTime =="2:30 pm":
        pyautogui.moveTo(500,705,0.5)
    elif WorkoutTime =="3:30 pm":
        pyautogui.moveTo(500,720,0.5)
    elif WorkoutTime =="4:30 pm":
        pyautogui.moveTo(500,740,0.5)
    elif WorkoutTime =="5:30 pm":
        pyautogui.moveTo(500,760,0.5)
    elif WorkoutTime =="6:30 pm":
        pyautogui.moveTo(500,780,0.5)
    pyautogui.click()

        
    

    

#time booker
def bookTime():
    # opens website and gets parameters
    OpenWeb()
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    # takes you to the webform
    scroll()
    scroll()  
    # fills information
    pyautogui.click()
    location()
    pyautogui.moveTo(200,460,0.5)
    pyautogui.click()
    pyautogui.write(fname,0.15)
    pyautogui.press('tab')
    pyautogui.write(lname,0.15)
    month()
    fill()
    pyautogui.press('enter')
    pyautogui.moveTo(200,460,0.5)
    pyautogui.click()
    
    #page 2 of website
    #selects the last day
    pyautogui.moveTo(200,500,0.5)
    pyautogui.click()
    pyautogui.moveTo(200,600,0.5)
    pyautogui.click()
    pyautogui.moveTo(200,550,0.5)
    pyautogui.click()
    pyautogui.moveTo(200,575,0.5)
    pyautogui.click()
    scroll()
    pyautogui.moveTo(500,700,0.5)
    pyautogui.click()
    pyautogui.moveTo(500,780,0.5)
    timeSlot()
    pyautogui.moveTo(500,730,0.5)
    #pyautogui.click()





bookTime()

