import os, time, random, sys
import pyautogui
import win32gui, win32com.client
# from win10toast import ToastNotifier

# toaster = ToastNotifier()
abs = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/screenshots/"

def CheckAnki():
    if(win32gui.FindWindow(None, "User 1 - Anki") == 0):
        os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
        time.sleep(10)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.AppActivate("User 1 - Anki")
    else: os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")
    time.sleep(3)

def StudyNow(AllDone):
    StudyNow_location = pyautogui.locateOnScreen(abs + 'StudyNow.png', confidence=0.9)
    if StudyNow_location is not None:
        StudyNow_center = pyautogui.center(StudyNow_location)
        pyautogui.click(StudyNow_center.x, StudyNow_center.y)
    else:
        AllDone += 1
        Decks_location = pyautogui.locateOnScreen(abs + 'Decks.png', confidence=0.9)
        if Decks_location is not None:
            Decks_center = pyautogui.center(Decks_location)
            pyautogui.click(Decks_center.x, Decks_center.y)
    return AllDone

pyautogui.PAUSE = 0.5
os.system("cls")
os.system("start C:\\Users\\Public\\Desktop\\Anki.lnk")

while True:
    Decks_location = pyautogui.locateOnScreen(abs + 'Decks.png', confidence=0.9)
    if Decks_location is not None:
        OK_location = pyautogui.locateOnScreen(abs + 'OK.png', confidence=0.9)
        if OK_location is not None:
            OK_center = pyautogui.center(OK_location)
            pyautogui.click(OK_center.x, OK_center.y)
        Syncing_location = pyautogui.locateOnScreen(abs + 'Syncing.png', confidence=0.9)
        if Syncing_location is None:
            break
    time.sleep(1)
shell = win32com.client.Dispatch("WScript.Shell")
shell.AppActivate("User 1 - Anki")
Anki = win32gui.FindWindow(None, "User 1 - Anki")
x = 0
if Anki != 0:
    while True:
        AllDone = 0
        English_location = pyautogui.locateOnScreen(abs + 'English.png', confidence=0.9)
        if English_location is not None: #1
            English_center = pyautogui.center(English_location)
            pyautogui.click(English_center.x, English_center.y)
            AllDone = StudyNow(AllDone)
        A0_location = pyautogui.locateOnScreen(abs + 'A0.png', confidence=0.9)
        if A0_location is not None: #2
            A0_center = pyautogui.center(A0_location)
            pyautogui.click(A0_center.x, A0_center.y)
            AllDone = StudyNow(AllDone)
        A2_location = pyautogui.locateOnScreen(abs + 'A2.png', confidence=0.9)
        if A2_location is not None: #3
            A2_center = pyautogui.center(A2_location)
            pyautogui.click(A2_center.x, A2_center.y)
            AllDone = StudyNow(AllDone)
        B_location = pyautogui.locateOnScreen(abs + 'B.png', confidence=0.9)
        if B_location is not None: #4
            B_center = pyautogui.center(B_location)
            pyautogui.click(B_center.x, B_center.y)
            AllDone = StudyNow(AllDone)
        C_location = pyautogui.locateOnScreen(abs + 'C.png', confidence=0.9)
        if C_location is not None: #5
            C_center = pyautogui.center(C_location)
            pyautogui.click(C_center.x, C_center.y)
            AllDone = StudyNow(AllDone)
        D_location = pyautogui.locateOnScreen(abs + 'D.png', confidence=0.9)
        if D_location is not None: #6
            D_center = pyautogui.center(D_location)
            pyautogui.click(D_center.x, D_center.y)
            AllDone = StudyNow(AllDone)
        KK_location = pyautogui.locateOnScreen(abs + 'KK.png', confidence=0.9)
        if KK_location is not None: #7
            KK_center = pyautogui.center(KK_location)
            pyautogui.click(KK_center.x, KK_center.y)
            AllDone = StudyNow(AllDone)
        
        ShowAnswer_location = pyautogui.locateOnScreen(abs + 'ShowAnswer.png', confidence=1)
        pyautogui.press('space')
        CheckAnki()
        Good_location = pyautogui.locateOnScreen(abs + 'Good.png', confidence=0.9)
        if Good_location is not None:
            Good_center = pyautogui.center(Good_location)
            time.sleep(60)
            while Good_location or Easy_location is not None:
                x += 1
                Easy_location = pyautogui.locateOnScreen(abs + 'Easy.png', confidence=0.9)
                Easy_center = pyautogui.center(Easy_location)
                Lower10min_location = pyautogui.locateOnScreen(abs + '10min.png', confidence=0.9)
                aDay_location = pyautogui.locateOnScreen(abs + '1d.png', confidence=0.9)
                if x < 10: print("  ", end = '')
                elif x < 100: print(" ", end = '')
                if Lower10min_location is not None:
                    Lower10min_center = pyautogui.center(Lower10min_location)
                    if Lower10min_center.x >= 1600: 
                        pyautogui.click(Good_center.x, Good_center.y)
                        print(x, "Good 10m")
                    elif aDay_location is not None:
                        aDay_center = pyautogui.center(aDay_location)
                        if aDay_center.x >= 1600: 
                            pyautogui.click(Good_center.x, Good_center.y)
                            print(x, "Good 1d")
                        else: 
                            pyautogui.click(Easy_center.x, Easy_center.y)
                            print(x, "Easy Left1d")
                    else: 
                        if random.random() <= 0.7:
                            pyautogui.click(Easy_center.x, Easy_center.y)
                            print(x, "Easy rand") #Left10min&no1d
                        else:
                            pyautogui.click(Good_center.x, Good_center.y)
                            print(x, "Good rand")
                else: 
                    pyautogui.click(Easy_center.x, Easy_center.y)
                    print(x, "Easy no10min") #impossible
                pyautogui.press('space')
                time.sleep(random.randint(50,60))
                CheckAnki()
                Good_location = pyautogui.locateOnScreen(abs + 'Good.png', confidence=0.9)
                if Good_location is None:
                    Decks_location = pyautogui.locateOnScreen(abs + 'Decks.png', confidence=0.9)
                    if Decks_location is not None:
                        Decks_center = pyautogui.center(Decks_location)
                        pyautogui.click(Decks_center.x, Decks_center.y)
                    break
        elif AllDone == 7:
            print("Review has done")
            Sync_location = pyautogui.locateOnScreen(abs + 'Sync.png', confidence=0.9)
            Sync_center = pyautogui.center(Sync_location)
            pyautogui.click(Sync_center.x, Sync_center.y)
            time.sleep(15)
            break
        else:
            print("Wrong window or page")
            break
    os.popen('%s%s' % ("taskkill /F /IM ","Anki.exe"))
else: print("Anki open fail")

print(time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime()))
if x == 7: time.sleep(30)
else: time.sleep(1800)
sys.exit()