#!/usr/bin/python

# This script monitors which app steals focus away from you on Macbook
# All credits and praise go to /u/fredfow3 ❤️, thank you again, you've saved me a headache trying to debug this issue
# You might need to: `pip install pyobjc`

try:
    from AppKit import NSWorkspace
except ImportError:
    print("Can't import AppKit -- maybe you're running python from brew?")
    print("Try running with Apple's /usr/bin/python instead.")
    exit(1)

from datetime import datetime
from time import sleep

last_active_name = None
while True:
    active_app = NSWorkspace.sharedWorkspace().activeApplication()
    if active_app["NSApplicationName"] != last_active_name:
        last_active_name = active_app["NSApplicationName"]
        print(
            "%s: %s [%s]"
            % (
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                active_app["NSApplicationName"],
                active_app["NSApplicationPath"],
            )
        )
sleep(1)
