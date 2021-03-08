import pyautogui
from time import sleep


pyautogui.FAILSAFE = True

x, y = pyautogui.size()
# pyautogui.moveTo(x/2, y/2, duration=1.5)
# pyautogui.move(-200, 50, duration=1)
pyautogui.moveTo(113, 747, duration=1.5)
pyautogui.click()

# pyautogui.click(clicks=10, interval=0.05)
# pyautogui.doubleClick()
# pyautogui.rightClick()
# pyautogui.vscroll(200)
# pyautogui.typewrite('Add something', interval=0.2)
pyautogui.sleep(0.5)
pyautogui.moveTo(241, 457, duration=0.5)

pyautogui.click()
pyautogui.hotkey('shift', 'alt')
pyautogui.typewrite(['к', 'о', 'т', 'енок'], interval=0.4)

pyautogui.press('enter')

# click on icon on screen
# pyautogui.locateCenterOnScreen('path/to/icon')

# answer = pyautogui.confirm(text='Start?', title='Starting app confirm', buttons=['OK', 'No'])
# pyautogui.getWindowsWithTitle("Stack Overflow")[0].minimize()
# windows_list = pyautogui.getAllWindows()
# print(windows_list)

# if answer == 'OK':
#     print('yes')
# else:
#     print('nope')
