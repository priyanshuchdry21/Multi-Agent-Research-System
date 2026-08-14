from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

def run_research_pipeline(topic : str) -> dict:

    state = {}

    #step 1 - search agent working
    print("\n"+" ="*50)
    print("step 1 - search agent working...")
    print("="*50)

    try:
        search_agent = build_search_agent()
        search_result = search_agent.invoke({
            "messages" : [("user", f"find recent, reliable and detailed infromation about: {topic}")]
        })
        state["search_results"] = search_result["messages"][-1].content

        print("\n search results ", state["search_results"])
    except Exception as e:
        import traceback

        print("\n" + "=" * 80)
        print("❌ SEARCH AGENT FAILED")
        print(f"Error: {e}")
        print("-" * 80)
        traceback.print_exc()
        print("=" * 80)

        state["search_results"] = "No search results available."
        state["scraped_content"] = state["search_results"]

        print("\n search results fallback used.")


    # step 2 - reader agent working
        # step 2 - reader agent working
    print("\n" + " =" * 50)
    print("step 2 - reader agent is scraping top resources...")
    print("=" * 50)

    try:
        reader_agent = build_reader_agent()

        reader_result = reader_agent.invoke({
            "messages": [(
                "user",
                f"""
You are a web reader.

Extract the first valid URL from the search results below.
Use the scrape_url tool to read it.
If no URL exists, simply reply "No URL found".

Search Results:
{state['search_results'][:250]}
"""
            )]
        })

        state["scraped_content"] = reader_result["messages"][-1].content

    except Exception as e:
        import traceback

        print("\n" + "=" * 80)
        print("❌ READER AGENT FAILED")
        print(f"Error: {e}")
        print("-" * 80)
        traceback.print_exc()
        print("=" * 80)

        # Continue the pipeline even if reader fails
        state["scraped_content"] = state["search_results"]

    print("\nscraped content:\n", state["scraped_content"])
    #step 3 - writer chain

    print("\n"+" ="*50)
    print("step 3 - Writer is drafting the report...")
    print("="*50)

    research_combined = (
    f"Search Results:\n{state['search_results'][:250]}\n\n"
    f"DETAILED CONTENT:\n{state['scraped_content'][:500]}"
)
    
    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\n Final Report\n",state['report'])

    #step 4 - critic report

    print("\n"+" ="*50)
    print("step 4 - critic is reviewing the report...")
    print("="*50)

    state["feedback"] = critic_chain.invoke({
        "report": state['report']
    })

    print("\n Critic report \n", state['feedback'])

    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic: ")
    run_research_pipeline(topic)