from conva_ai import AsyncConvaAI
import asyncio

class ConvaAIHandler:
    client = AsyncConvaAI(
            copilot_id="e88ad0006e9e4b329869ea56c7e3e813", 
            copilot_version="1.0.0", 
            api_key="3ab933d615644b238fa181a2e02b11f0"
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