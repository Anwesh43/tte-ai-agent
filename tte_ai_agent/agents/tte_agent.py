from pydantic_ai import Agent 
from dotenv import load_dotenv 
from tools.tte_tools import getEffects, addEffect 
from prompts.tte_prompt import SYSTEM_PROMPT 

load_dotenv()

agent = Agent(
    system_prompt = SYSTEM_PROMPT, 
    model = 'openai:gpt-5.2',
    tools = [getEffects, addEffect]
)

async def generateTerminalStory(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')
        