from services.tte_wrapper import TTEWrapper 

tteWrapper = TTEWrapper()

def getEffects():
    print(f"Calling getEffects tool")
    return tteWrapper.getEffects()

def addEffect(effectName : str):
    print(f"Calling addEffect tool {effectName}")
    return tteWrapper.addEffect(effectName=effectName)

def playAnimation():
    print(f"Calling playAnimation tool call")
    return tteWrapper.playAnimation()