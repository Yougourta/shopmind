import asyncio
from src.agent import ShopMindState, run_agent

initial_state = ShopMindState(
    messages=[],
    user_profile=None,
    search_results=[],
    recommendations=[],
    iterations=0,
    error=None,
)

if __name__ == "__main__":
    result = asyncio.run(run_agent(initial_state))
    print(result)
