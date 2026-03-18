import asyncio
from shopmind.agent import ShopMindState, run_agent

def main():
    initial_state = ShopMindState(
        messages=[
            {"role": "user", "content": "Je cherche une poussette pour mon bébé qui va naître"}
        ],
        user_profile=None,
        search_results=[],
        recommendations=[],
        iterations=0,
        error=None,
    )
    result = asyncio.run(run_agent(initial_state))
    print(result)
if __name__ == "__main__":
    main()