import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

from subprocess import call
call(["ls", "-l"])

# import the XBMC libraries so we can use the controls and functions of XBMC
import xbmc, xbmcgui
 
# name and create our window 
class BlahMainWindow(xbmcgui.Window): 
    # and define it as self
    def __init__(self):
    # add picture control to our window (self) with a hardcoded path name to picture
# you can use a url in control image
    self.addControl(xbmcgui.ControlImage(0,0,720,480, 'Q:\\scripts\\background.jpg'))
 
# store our window as a short variable for easy of use
W = BlahMainWindow()
# run our window we created with our background jpeg image
W.doModal()
# after the window is closed, Destroy it.
del W
 
line1 = "Hello World!"
line2 = "We can write anything we want here"
line3 = "Using Python"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
