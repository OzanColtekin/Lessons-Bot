from selenium import webdriver
from tkinter import *
from selenium.webdriver.common.keys import Keys
import time
import os
import schedule
from tkinter import messagebox
import keyboard
import pyautogui

class JoinZoom():

    def first(self):
        self.driver = webdriver.Chrome()
        self.url = "http://online.yildiz.edu.tr/"
        self.driver.get(self.url)
        time.sleep(3)

    def logininfo(self):
        self.information = []
        try:
            if os.path.exists("bilgiler.txt"):
                with open("bilgiler.txt", "r") as bilgi:
                    read = bilgi.read().split("\n")
                    for row in read:
                        self.information.append(row)
            else:
                with open("bilgiler.txt", "w") as bilgi:
                    bilgi.close()
                messagebox.showerror(title="Hata", message="'bilgiler.txt' dosyası bulunamadı!!!\nDosya yerinize oluşturuldu! Lütfen içerisine bilgilerinizi giriniz.")
                exit()
        except FileNotFoundError:
            with open("bilgiler.txt", "w") as bilgi:
                bilgi.close()
            exit()

    def lisansinfo(self):
        if self.information[0] != "usiskullaniciadi":
            messagebox.showerror(title="HATA!", message="Bu program kişiye özel lisanslanmaktadır başkası tarafından kullanılamaz!")
            exit()

    def dersInfo(self):
        self.lessons = []
        try:
            if os.path.exists("lessons.txt"):
                with open("lessons.txt", "r") as lesso:
                    lesson = lesso.read().split("\n")
                    for less in lesson:
                        self.lessons.append(less)
            else:
                with open("lessons.txt", "w") as lessons:
                    lessons.close()
                messagebox.showerror(title="Hata", message="'lessons.txt' belgesi bulunamadı!!!\nDosya oluşturuldu! Lütfen içerisini düzenleyip tekrar çalıştırın.")
                exit()
        except FileNotFoundError:
            with open("lessons.txt", "w") as lessons:
                lessons.close()
            exit()

    def clockInfo(self):
        self.clocks = []
        try:
            if os.path.exists("clock.txt"):
                with open("clock.txt", "r") as c:
                    clock = c.read().split("\n")
                    for cl in clock:
                        self.clocks.append(cl)
            else:
                with open("clock.txt", "w") as c:
                    c.close()
                messagebox.showerror(title="Hata", message="'clock.txt' belgesi bulunamadı!!!\nDosya oluşturuldu! Lütfen içerisini düzenleyip tekrar çalıştırın.")
                exit()
        except FileNotFoundError:
            with open("clock.txt", "w") as c:
                c.close()
                exit()

    def findlogin(self):
        self.isStudent = self.driver.find_element_by_id("Data_AccountType")
        self.username = self.driver.find_element_by_id("Data_Mail")
        self.password = self.driver.find_element_by_id("Data_Password")
        self.button = self.driver.find_element_by_xpath('//*[@id="Information"]/div[4]/div[2]/button')

    def logged(self):
        self.isStudent.send_keys(Keys.ENTER, Keys.ARROW_DOWN, Keys.ARROW_DOWN, Keys.ENTER)
        self.username.send_keys(self.information[0])
        self.password.send_keys(self.information[1])
        self.button.click()

    def clickjoin(self):
        time.sleep(35)
        keyboard.press_and_release("enter")

    def pressEnter(self):
        time.sleep(3)
        keyboard.press_and_release("LEFT")
        time.sleep(2)
        keyboard.press_and_release("enter")

    def changewindow(self):
        time.sleep(2)
        pyautogui.keyDown('alt')
        time.sleep(.2)
        pyautogui.press('tab')
        time.sleep(.2)
        pyautogui.keyUp('alt')

    def joinbrw(self):
        self.first()
        self.findlogin()
        self.logged()
        time.sleep(8)

    def joinlesson(self,number):
        self.joinbrw()
        self.driver.get(self.lessons[number])
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="details"]/div/div/table/tbody/tr[1]/td[5]/a').click()
        self.pressEnter()
        self.clickjoin()
        self.driver.close()

    def loginlessonMondayOne(self):
        self.joinlesson(0)

    def loginlessonMondayTwo(self):
        self.joinlesson(1)

    def loginlessonTuesdayOne(self):
        self.joinlesson(2)

    def loginlessonTuesdayTwo(self):
        self.joinlesson(3)

    def loginlessonTuesdayThree(self):
        self.joinlesson(4)

    def loginlessonWedOne(self):
        self.joinlesson(5)

    def loginlessonWedTwo(self):
        self.joinlesson(6)

    def loginlessonWedThree(self):
        self.joinlesson(7)

    def loginlessonThuOne(self):
        self.joinlesson(8)

    def loginlessonFriOne(self):
        self.joinlesson(9)

    def loginlessonFriTwo(self):
        self.joinlesson(10)

    def start_schedules(self):
        schedule.every().monday.at("09:02").do(self.loginlessonMondayOne)
        schedule.every().monday.at("11:02").do(self.loginlessonMondayTwo)
        schedule.every().tuesday.at("09:02").do(self.loginlessonTuesdayOne)
        schedule.every().tuesday.at("13:02").do(self.loginlessonTuesdayTwo)
        schedule.every().tuesday.at("13:02").do(self.loginlessonTuesdayThree)
        schedule.every().wednesday.at("08:02").do(self.loginlessonWedOne)
        schedule.every().wednesday.at("11:02").do(self.loginlessonWedTwo)
        schedule.every().wednesday.at("13:02").do(self.loginlessonWedThree)
        schedule.every().thursday.at("13:02").do(self.loginlessonThuOne)
        schedule.every().friday.at("08:02").do(self.loginlessonFriOne)
        schedule.every().friday.at("08:02").do(self.loginlessonFriTwo)
        schedule.every().saturday.at("16:45").do(self.loginlessonFriTwo)


connect = JoinZoom()

def button():
    connect.logininfo()
    connect.lisansinfo()
    connect.dersInfo()
    whichclieckedone = clicked.get()
    whichclicked = clickedtwo.get()
    if whichclieckedone == "İstatistik":
        if whichclicked == "2. Sınıf":
            connect.start_schedules()
            time.sleep(5)
            while True:
                schedule.run_pending()
                time.sleep(5)


path = os.getcwd()
ico = path + "\\bot.ico"


root = Tk()
root.title("Auto Join Lesson BOT v0.1")
root.geometry("400x250")
root.iconbitmap(ico)
root.tk_setPalette("#c0c0c0")

# Drop Down Boxes
clicked = StringVar()
clickedtwo = StringVar()
drop = OptionMenu(root, clicked, "İstatistik")
drop.pack(pady=12)
drop = OptionMenu(root, clickedtwo, "2. Sınıf")
drop.pack(pady=12)

myButton = Button(root, command=button, text="RUN!", bg="yellow", fg="black")
myButton.pack(pady=20)
yazi = Label(root, text="Copyrigt Ozan", fg="black", padx=5, pady=100)
yazi.pack(side=RIGHT)

root.mainloop()
