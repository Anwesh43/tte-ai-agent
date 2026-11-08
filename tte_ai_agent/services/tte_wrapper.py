from terminaltexteffects.effects.effects_rain import Rain
from terminaltexteffects.effects.effects_burn import Burn
from terminaltexteffects.effects.effects_beam import Beam
from terminaltexteffects.effects.effects_bubbles import Bubbles
from terminaltexteffects.effects.effects_fireworks import Fireworks
from terminaltexteffects.effects.effects_spotlights import Spotlights 
from terminaltexteffects.effects.effects_bouncyballs import BouncyBalls 
from terminaltexteffects.effects.effects_laseretch import LaserEtch

import time 
import sys 

class TTEWrapper:
    def __init__(self):
        self.effects = []
        self.effectMap = {
            "rain": Rain, 
            "fireworks": Fireworks,
            "beam": Beam, 
            "bubble": Bubbles, 
            "burn": Burn, 
            "spotlights": Spotlights,
            "bouncyballs": BouncyBalls,
            "laseretch": LaserEtch
        }

    def getEffects(self):
        return [key for key, _ in self.effectMap.items()]

    def _sendError(self, effectName : str):
        return {
            "status": "Error",
            "message": f"Effect {effectName} is not supported"
        }
    def addEffect(self, effectName : str):
        if not(effectName in self.effectMap):
            return self._sendError(effectName=effectName)
        self.effects.append(self.effectMap[effectName])
        return self._sendSuccessResponse(effectName=effectName)
    
    def _playEffect(self, effect):
        with effect.terminal_output() as terminal:
            for frame in effect:
                terminal.print(frame)

    def _sendSuccessResponse(self, effectName : str):
        return {
            "status": "success",
            "message": f"added {effectName} effect"
        }
    def addRainEffect(self, text : str):
        self.effects.append(Rain(text))
        return self._sendSuccessResponse("rain")

    def addBurnEffect(self, text : str):
        self.effects.append(Burn(text))
        return self._sendSuccessResponse("burn")

    def addBeamEffect(self, text : str):
        self.effect.append(Beam(text))
        return self._sendSuccessResponse("rain")
        
    def addBubbleEffects(self, text : str):
        self.effects.append(Bubbles(text))
        return self._sendSuccesResponse("bubbles")

    def addFireworkEffects(self, text : str):
        self.effects.append(Bubbles(text))
        return self._sendSuccessResponse("fireworks")

    def playAnimation(self):
        for effect in self.effects:
            self._playEffect(effect)
            time.sleep(1)
            sys.stdout.flush()
