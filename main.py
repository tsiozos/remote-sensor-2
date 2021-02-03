StationID = 0
NetworkLeaderID = 0     #on first INIT get the serial number of the network leader
radio.set_group(7)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)


def showStationID():
    global StationID
    ids = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    basic.show_string(ids[StationID],200)

def emptyKeyBuffer():
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B) or input.button_is_pressed(Button.AB):
        pass

def SetupStationID():
    global StationID
    print("Entering setup:")
    emptyKeyBuffer()
    showStationID()
    while True:
        
        if input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
            StationID = max(0, StationID-1)
            showStationID()
        elif input.button_is_pressed(Button.B) and not input.button_is_pressed(Button.A):
            StationID = min(35,StationID+1)
            showStationID()
        elif input.button_is_pressed(Button.AB):
            emptyKeyBuffer()
            return


### NetworkInit: initialize the network. The 0-station sends INIT signal and every station autoconfigured.
def NetworkInit():
    global StationID
    if StationID==0:
        pass





################## MAIN LOOP ########################
showStationID()
basic.clear_screen()

while True:
    basic.pause(100)
    if input.button_is_pressed(Button.AB):
        SetupStationID()
        basic.clear_screen()
    
    # only stations with ID=0 are allowed to init the network
    if input.button_is_pressed(Button.A):
        NetworkInit()
