

# Card10-Personal-Massager
Testing the vibrate motor on Card10 badge from CCCamp2019

## Install:

cd /dev/[device_name]/apps
git clone https://github.com/frigginglorious/Card10-Personal-Massager personal_massager

## Issues

Right now it breaks when the bottom left/right buttons are pressed because "NameError: local variable referenced before assignment"... so I need to learn to python

Also it will only vibrate for a couple of minutes before the message "MXC_ASSERT ../lib/FreeRTOS/Source/timers.c #386: (xTimer)" is output and it stops working.

### Main Repos
https://git.card10.badge.events.ccc.de

### Main Info
https://card10.badge.events.ccc.de/

### API Doc
https://firmware.card10.badge.events.ccc.de/epicardium/api.html#vibration-motor

