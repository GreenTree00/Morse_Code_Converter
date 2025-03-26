import morsecode

on = True

MorseCode = morsecode.MorseCode()

while on:
    print(MorseCode.greeting())
    data = input("Please enter the string you would like to convert to morse code: \n").upper()
    print(MorseCode.morse_code_converter(data))
  
