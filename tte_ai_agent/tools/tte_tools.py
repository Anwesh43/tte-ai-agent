from services.tte_wrapper import TTEWrapper 

tteWrapper = TTEWrapper()

def getEffects():
    print(f"Calling getEffects tool")
    return tteWrapper.getEffects()

def addEffect(effectName : str, text : str):
    print(f"Calling addEffect tool {effectName}")
    return tteWrapper.addEffect(effectName=effectName, text = text)

def playAnimation():
    print(f"Calling playAnimation tool call")
    return tteWrapper.playAnimation()

def clearScreen():
    print(f"Calling clearScreen tool")
    tteWrapper.clearScreen()
    return {
        "status": "success",
        "message": "cleared screen"
    }
