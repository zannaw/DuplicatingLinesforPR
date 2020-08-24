import sys
import pyperclip
def duplicate(s):
  mystr = ""
  print("---DUPLICATION-----------------")
  for line in s.splitlines():
    if (len(line) >= 1):
      mystr += (line + "\n")
      mystr += (line + "\n")
      print(line)
      print(line)
    else:
      print(line)
      mystr += (line + "\n")
  print("---END OF DUPLICATION------------")
  pyperclip.copy(mystr)

while(True):
  print("Enter the lines you wish to duplicate. Type Ctrl+d on a new line when finished: ")
  s = sys.stdin.read()
  duplicate(s)
