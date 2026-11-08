from terminaltexteffects.effects import Rain, Burn,Beams,  Bubbles, Fireworks, Spotlights, BouncyBalls, LaserEtch
from terminaltexteffects.engine.terminal import TerminalConfig 
from terminaltexteffects.utils.graphics import Color, Gradient 
import time 
import sys 

class TTEWrapper:
    def __init__(self):
        self.effects = []
        self.effectMap = {
            "rain": Rain, 
            "fireworks": Fireworks,
            "beam": Beams, 
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
    def addEffect(self, effectName : str, text : str):
        if not(effectName in self.effectMap):
            return self._sendError(effectName=effectName)
        terminalConfig = TerminalConfig(canvas_width = -1, canvas_height = -1, frame_rate = 60, no_color = False, xterm_colors = False, existing_color_handling="ignore")
        effect = self.effectMap[effectName](text, terminal_config = terminalConfig)
        effect.effect_config.final_gradient_stops = (
            Color("FF4500"),
            Color("FF8C00"),
            Color("FFD700"),
        )
        effect.effect_config.final_gradient_steps = 12 
        effect.effect_config.final_gradient_direction = Gradient.Direction.HORIZONTAL
        self.effects.append(effect)
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

    def clearScreen(self):
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()

    def playAnimation(self):
        for effect in self.effects:
            self._playEffect(effect)
            time.sleep(1)
            self.clearScreen()
        return {
            "status": "success",
            "message": "played animation"
        }
