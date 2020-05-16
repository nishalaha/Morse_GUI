from tkinter import *
import tkinter as tk
import time
import tkinter.font
import RPi.GPIO as GPIO
import RPi.GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

win = Tk()
win.title("Morse Code Blinker")
fontType = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

morseCode = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}


def mcode():
    value = textBox.get(1.0, tk.END+"-1c")
    value = value.upper()
    morse_code = ''
    for character in value:
        if character != ' ':
            morse_code += morseCode[character] + ' '
      
    for strg in morse_code:
        if strg == '-':
            dash()
        elif strg == '.':
            dot()
        else:
            time.sleep(0.5)
    time.sleep(0.5)
        
def dot():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(8,GPIO.LOW)
    time.sleep(0.3)

def dash():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(0.7)
    GPIO.output(8,GPIO.LOW)
    time.sleep(0.3)
    
                 
def x():
    RPi.GPIO.cleanup()
    win.destroy()
 
textBox = Text(win,height=1, width=40)
textBox.grid(row=1 , column=1)

enterB = Button(win,height=1, width=6, text='CIPHER!', font=fontType, fg = 'green', command = mcode)
enterB.grid(row=1, column=3)

close = Button(win, height=1, width=2, text='X', font=fontType, command = x, bg='red' )
close.grid(row=1, column=4)

win.protocol("WM_DELETE_WINDOW", x) 


mainloop() 
