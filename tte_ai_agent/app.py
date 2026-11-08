from agents.tte_agent import generateTerminalStory 
import sys
import asyncio 
from tools.tte_tools import clearScreen, playAnimation 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(generateTerminalStory(prompt))
    clearScreen()
    playAnimation()
    