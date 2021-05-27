
from plyer import notification
from threading import Timer
print("Here we are, wait 10 secs")
while True: 
    def warning():
        notification.notify(title='Time to break!', message='Make sure you take a break every now and then!', app_name='Break45', app_icon='C:/Users/Lidia/Documents/GitHub/Python-101/mini-projects/assets/pc.ico', timeout=10, ticker='', toast=False)
    t = Timer(2700, warning)
    t.start() 


