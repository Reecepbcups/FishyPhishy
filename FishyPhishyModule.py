# Reecepbcups - December 27th, 2018.
# Discord Contact: Reecepbcups#3370

import pyautogui as p
import time, random, string
from faker import Faker 
fake = Faker()
#pyautogui.displayMousePosition() in CMD/Terminal to see location at all times 

class Phishy():
    
    def website(self, link, x=265, y=65):
        time.sleep(1)
        p.click(x,y) # address bar on chrome 1080p. Yours may differ
        p.typewrite(link)
        p.press('enter')
        # No tab due to being the webstie restart
        
    def email(self):
        p.typewrite(fake.simple_profile(sex=None)['mail'] + '\t')


    @classmethod 
    def password(self):
        p.typewrite(''.join(random.choice(string.ascii_letters) for x in range(int(random.randint(8,20)))))
        p.press('tab')
    pw = password
    
    def name(self, words='b'):
        if words is 'f': # First Name
            p.typewrite(fake.name().split()[0])
        elif words == 'l': # last name
            p.typewrite(fake.name().split()[1])
        elif words == 'b': # both
            p.typewrite(fake.name())
        p.press('tab')

    @classmethod
    def home(self):
        try:
            p.typewrite(fake.address().split('\n')[0])
        except:
            p.typewrite(fake.address().split('\n')[0])
        p.press('tab')
    address = home

    def city(self):
        try:
            p.typewrite(fake.address().split('\n')[1].split(',')[0])
        except:
            p.typewrite(fake.address().split('\n')[1].split(',')[0])
        p.press('tab')
        
    def state(self):
        try:
            p.typewrite(fake.address().split('\n')[1].split(',')[1].split()[0])
        except:
            p.typewrite(fake.address().split('\n')[1].split(',')[1].split()[0])
        p.press('tab')
        
    @classmethod
    def zip_code(self):
        try:
            p.typewrite(fake.address().split('\n')[1].split(',')[1].split()[1])
        except:
            p.typewrite(fake.address().split('\n')[1].split(',')[1].split()[1])
        p.press('tab')
    zip = zip_code
    
    @classmethod     
    def ssn(self):
        p.typewrite(fake.ssn(taxpayer_identification_number_type="SSN"))
        p.press('tab')
    social = ssn

    @classmethod      
    def phone(self):
        p.typewrite(fake.phone_number())
        p.press('tab')
    phone_number = phone

    @classmethod   
    def card(self, info='number'):
        if info == 'number' or info == 'n':
            p.typewrite(fake.credit_card_number(card_type=None)) 
        elif info=='exp' or info== 'experation':
            p.typewrite(str(random.randint(2021,2030)))
        p.press('tab')
    credit = card
    credit_card = card

    @classmethod
    def cvv(self):
        p.typewrite(fake.credit_card_security_code(card_type=None))
    csc = cvv
    cvs = cvv
    security = cvv

        
    @classmethod     
    def dropDown(self, kind='month'):
        actions = ['enter', 'down', 'enter', 'tab']
        for action in actions:
            p.press(action)
            time.sleep(0.3)
    buttons = dropDown
    selectBox = dropDown
    

    @classmethod
    def location(self, number=25):
        print('Press enter to print the mouses postion on your screen.\n(q to quit)\n')
        for i in range(number):
            user = input()
            if user == 'q' or user == 'Q':
                break
            print(str(i + 1) +". "+ str(p.position()))
    loc = location 

    @classmethod
    def click(self,x=None,y=None):
        if x == None and y == None:
           print('You did not pass a X, or Y value to the .click() function.')
           print('Mouse Cordnates Are: ' + str(p.position()))
        else:
            p.click(x,y)

    submit = click

    @classmethod
    def tab(self):
        p.press('tab')
    t = tab

    def enter(self):
        p.press('enter')
        
    @classmethod
    def numbers(self, t='d'):
        if t == 'd':
            p.typewrite(str(random.randint(0,31)).zfill(2))
        elif t == 'm':
            p.typewrite(str(random.randint(1,12)).zfill(2))
        elif t == 'y':
            p.typewrite(str(random.randint(1943,1994)))
    date = numbers

    @classmethod
    def text(self, string):
        p.typewrite(str(string))
        p.press('tab')
    type = text
    
    def repeat_click(self, x,y ,NumberOfTimes, delay=0):
        for i in range(NumberOfTimes):
            p.click(x,y)
            time.sleep(delay)
        
    def rest(self, wait):
        time.sleep(int(wait))

        
