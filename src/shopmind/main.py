import asyncio
from shopmind.agent import ShopMindState, run_agent
from shopmind.logger import logger

def main():
    # Get user input
    logger.info('ShopMind: Que recherchez-vous?')
    user_input = input('You: ')
    # Create initial state
    initial_state = ShopMindState(
        messages=[
            {"role": "user", "content": user_input}
        ],
        user_profile=None,
        search_results=[],
        recommendations=[],
        iterations=0,
        error=None,
    )
    # Run the agent
    result = asyncio.run(run_agent(initial_state))
    # Print the result
    logger.info(f"final result: {result}")
if __name__ == "__main__":
    main()