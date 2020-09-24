import datetime
from win10toast import ToastNotifier
import sys

day = datetime.datetime.now().strftime("%d")
if day == '01':
    toaster = ToastNotifier()
    toaster.show_toast("Cache Cleaner",
                   "It's time to clean your PC!",
                   icon_path="logo_small.ico",
                   duration=7)

else:
    sys.exit()
