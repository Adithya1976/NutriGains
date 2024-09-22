from conva_ai import AsyncConvaAI
import asyncio
import os

CONVA_AI_COPILOT_ID = os.environ.get("CONVA_AI_COPILOT_ID")
CONVA_AI_COPILOT_VERSION = os.environ.get("CONVA_AI_COPILOT_VERSION")
CONVA_AI_COPILOT_API_KEY = os.environ.get("CONVA_AI_COPILOT_API_KEY")

class ConvaAIHandler:
    client = AsyncConvaAI(
            copilot_id=CONVA_AI_COPILOT_ID, 
            copilot_version=CONVA_AI_COPILOT_VERSION, 
            api_key=CONVA_AI_COPILOT_API_KEY
    )
    async def getResponse(query: str, stream: bool):
        response = ConvaAIHandler.client.invoke_capability(query, stream=stream)
        out = ""
        async for res in response:
            out = res.model_dump_json(indent=4)
        return out
    def generate(query, stream):
        response = asyncio.run(ConvaAIHandler.getResponse(query, stream))
        return response
