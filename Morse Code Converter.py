morse_dict = {"A": ".-",
              "B": "-...", 
              "C":"-.-.",
              "D":"-..", 
              "E":".", 
              "F": "..-.",
              "G": "--.", 
              "H":"....", 
              "I": "..", 
              "J":".---", 
              "K":"-.-",
              "L":".-..",
              "M": "--",
              "N": "-.",
              "O": "---",
              "P": ".--.",
              "Q": "--.-",
              "R": ".-.",
              "S": "...",
              "T": "-",
              "U": "..-",
              "V": "...-",
              "W": ".--",
              "X": "-..-",
              "Y": "-.--",
              "Z": "--.."}
string1 = input("Enter a sentence\n")
string1 = string1.upper()
string1 = string1.replace(" ", "")
l = [ char for char in string1]
morse_list = []
for each_letter in l:
    x = morse_dict[each_letter]
    morse_list.append(x)
for each_code in morse_list:
    print(each_code, end=" ")