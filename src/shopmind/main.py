import asyncio
from shopmind.crew import ShopMindState, run_agent, ShopMindCrew

def main():
    # initial_state = ShopMindState(
    #     messages=[],
    #     user_profile=None,
    #     search_results=[],
    #     recommendations=[],
    #     iterations=0,
    #     error=None,
    # )
    # result = asyncio.run(run_agent(initial_state))
    # print(result)

    ShopMindCrew().shopmind_crew().kickoff()

if __name__ == "__main__":
    main()