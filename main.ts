let StationID = 0
let NetworkLeaderID = 0
// on first INIT get the serial number of the network leader
radio.setGroup(7)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
function showStationID() {
    
    let ids = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    basic.showString(ids[StationID], 200)
}

function emptyKeyBuffer() {
    while (input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B) || input.buttonIsPressed(Button.AB)) {
        
    }
}

function SetupStationID() {
    
    console.log("Entering setup:")
    emptyKeyBuffer()
    showStationID()
    while (true) {
        if (input.buttonIsPressed(Button.A) && !input.buttonIsPressed(Button.B)) {
            StationID = Math.max(0, StationID - 1)
            showStationID()
        } else if (input.buttonIsPressed(Button.B) && !input.buttonIsPressed(Button.A)) {
            StationID = Math.min(35, StationID + 1)
            showStationID()
        } else if (input.buttonIsPressed(Button.AB)) {
            emptyKeyBuffer()
            return
        }
        
    }
}

// ## NetworkInit: initialize the network. The 0-station sends INIT signal and every station autoconfigured.
function NetworkInit() {
    
    if (StationID == 0) {
        
    }
    
}

// ################# MAIN LOOP ########################
showStationID()
basic.clearScreen()
while (true) {
    basic.pause(100)
    if (input.buttonIsPressed(Button.AB)) {
        SetupStationID()
        basic.clearScreen()
    }
    
    //  only stations with ID=0 are allowed to init the network
    if (input.buttonIsPressed(Button.A)) {
        NetworkInit()
    }
    
}
