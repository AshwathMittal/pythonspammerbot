import pyautogui, time
time.sleep(2)
o = open("beemovie.txt","r")
for line in o:
     pyautogui.typewrite(line)
     pyautogui.press('enter')