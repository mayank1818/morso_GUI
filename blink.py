import time
import tkinter as tk
from gpiozero import LED

# Initialize GPIO
led = LED(17)  # GPIO 17

# Morse code dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
                   '-': '-....-', '(': '-.--.', ')': '-.--.-'}

# Create GUI
window = tk.Tk()
window.title("Morse Code Converter")
window.geometry("400x200")

# Function to convert text to Morse code
def convert_to_morse():
    text = entry.get().upper()
    morse_code = ""
    for char in text:
        if char == ' ':
            morse_code += ' '
        elif char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
    blink_led(morse_code)

# Function to blink LED based on Morse code
def blink_led(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            led.on()
            time.sleep(0.2)
            led.off()
            time.sleep(0.2)
        elif symbol == '-':
            led.on()
            time.sleep(0.6)
            led.off()
            time.sleep(0.2)
        elif symbol == ' ':
            time.sleep(0.6)

# GUI elements
label = tk.Label(window, text="Enter text to convert to Morse code:")
label.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack()

convert_button = tk.Button(window, text="Convert", command=convert_to_morse)
convert_button.pack(pady=10)

exit_button = tk.Button(window, text="Exit", command=window.destroy)
exit_button.pack(pady=10)

window.mainloop()