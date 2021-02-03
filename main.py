StationID = 0   # the name of the server is a number 0-35. >10 are ABCDEF...Z
NetID = 0    #net ID is a number assigned to this station during INIT phase.
anscestorID = 0     #on first INIT get the serial number of the anscestor station.
MyNetworkAddress = 0
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


# accept commands and dispatch
def on_received_string(receivedString):
    global anscestorID, NetID
    rs = receivedString[0:3]
    nid = receivedString[4:]    #netID of ascendant station
    if rs == "INIT" and anscestorID == 0:
        ascestorID = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
        NetID = int(nid) + 1

radio.on_received_string(on_received_string)

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
