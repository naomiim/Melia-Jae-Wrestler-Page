"""
__filename__ = "webpage.py"
__course__ = "SDEV 300 6382"
__author__ = "Naomi Martinez"
__copyright__ = "None"
__credits__ = "Naomi Martinez"
__license__ = "Pyzo GPL"
__version__ = "1.0.0"
__maintainer__ = "Naomi Martinez"
__email__ = "nmartinezwilson@student.umgc.edu"
__status__ = "Project 6"
"""

from flask import Flask
import datetime


app = Flask(__name__)

@app.route('/webpage')

def build():
    myReply = popHead()
    myReply += popH1('Welcome to the future site of MELIA JAE!!')
    myReply += popH1("FUTURE PRO WRESTLER!!")
    myReply += popComment('In the furture site this will be an About Me section')
    myReply += popH2('About Melia Jae')
    myReply += popParagraph('Born in Oahu, Hawaii and moved to San Antonio, TX to persue her wrestling dreams')
    myReply += popH2('Check her out')
    myReply += popParagraph('Check out her awesome Facebook')
    myReply += popLink('https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2Fpages%2Fcategory%2FAthlete%2FMelia-Jae-105055857706710%2F&psig=AOvVaw24a8lIXrz6ZzLE9Qr-bPAi&ust=1582802856008000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCNDvla-cCFQAAAAAdAAAAABAD/', 'Facebook')
    myReply += popH2('Check out her FIRST interview in Mexico')
    myReply += popLink('https://www.youtube.com/watch?v=mYdbJ751bIE/', 'Mexico Interview')
    myReply += popH3('Check out her Future Events here')
    myReply += popOrderedList()
    myReply += popH2('A day in her life')
    myReply += popUnorderedList()
    myReply += popLink('https://www.youtube.com/watch?v=kekD_sDvYME', 'EPIC Wrestling Match')
    myReply += popH2('Future Blog... under construction')
    myReply += popParagraph('Check out Melia Jae current time at San Antonio, TX')
    myReply += popLink('https://www.time.gov/', 'Time.org')
    myReply += str(popTime())
    
    myReply += popEnd()
    return myReply
    
    
def popH1(myString):
    newString = '<H1>' + myString + '</H1>'
    return newString
    
    
def popHead():
    headData = "<!DOCTYPE html> "
    headData +="<head> "
    headData +="<title>Melia Jae Wrestler</title>"
    headData +="<style>" + getStyle() + "</style>"
    headData +="</head>"
    headData +="<body>"
    return headData
    
    
def getStyle():
    myStyle = "table,td {"
    myStyle += "border: 5px solid #117;"
    myStyle += "}"
    return myStyle
    
def popH2(myString):
    newString = '<h2 align=\"center\">' + myString + '</h2>'
    return newString

def popH3(myString):
    newString = '<h3 align=\"center\">' + myString + '</h3>'
    return newString
    
def popParagraph(myString):
    newString = '<p align=\"center\">' + myString + '</p>'
    return newString

def popComment(myString):
    newString = '<!-- ' + myString + ' -->'
    return newString

def popLink(site, text):
    newString = '<a style=\"text-align:center\" target=\"_blank\" align=\"center\" href=\'' + site + '\'>' + text + '</a>'
    return newString
    
def popUnorderedList():
    newString = '<ul style=\"text-align:left\" align=\"left\"><li>Wake Up</li><li>Go Train at Gym</li><li>Go back home</li><li>Get ready for work</li><li>Go to Work</li><li>Off work and to wrestling school</li>'
    return newString
    
def popOrderedList():
    newString = '<ol style=\"text-align:left\" align=\"left\"><li>Ladies Night Out, Feb 29th</li>'
    return newString
    
def popTime():
    newString = '<p style=\"text-align:center\">' + 'The Current time is: '+ str(datetime.datetime.now()) + '</p>'
    return newString
    
def popEnd():
    endData = "</body>"
    endData += "</html>"
    return endData
    
app.run(host='0.0.0.0', port= 8080)