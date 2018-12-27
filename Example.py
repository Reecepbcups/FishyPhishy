# Reecepbcups - December 27th, 2018.
# Discord Contact: Reecepbcups#3370

from FishyPhishyModule import Phishy # imports the module
from faker import Faker; fake = Faker()
import time 

# The class in the file FishyPhishyModule.py is called "Phishy" so we set this to "s" because it is faster to type.
s = Phishy() 


##
## LOGIN INFORMATION / BASIC INFORMATION WILL AUTO TAB
##


# Basic Movements
s.click(255, 1000)  # click mouse at a location (x,y)
s.location()        # Prints where your mouse is on screen. (Used in s.click() function)
s.text('Your text') # type what ever you want - Alias: s.type('Your text')
s.rest()            # Wait / sleep (in seconds)
s.tab()             # Preses the tab key - Alias: s.t()
s.enter()           # Presses Enter.

s.repeat_click(500,500,10,0) # Click X number of times. srepeat_click(X_Location, Y_Location, NumberOfTimesToClick, delayInSeconds)
s.dropDown()        # Drop down menu.
s.website('www.google.com', 265, 65) # website, search bar location (x,y)
s.numbers('d') # Random Day, month, or year. Arguments: 'd','m','y' # Alias: s.date()

# Login Information
s.email()    # Random Email
s.password() # Random Password

# Basic personal infomation / location
s.name('b') # Random name. Arguments 'f' = first, 'l' = last, 'b' = both.
s.home()    # Random address
s.city()    # Random city
s.state()   # Random state
s.zipcode() # Random zipcode - Alias s.zip()
s.phone() # Random Phone Number

# Sensitive info
s.card('n') # Random Credit Card. Arguments = 'number'/'n' or 'experation'/'exp'
s.cvv()     # Random CVV number (Back of card 3 digits - 066)
s.ssn()     # Random Social Security Number - Alias s.social()




















