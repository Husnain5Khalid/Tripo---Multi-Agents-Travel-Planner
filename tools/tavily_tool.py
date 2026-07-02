import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key = os.getenv("TAVILY_API_KEY")
)


def tavily_search(query):
    response = client.search(
        query= query,
        max_results= 5
    )

    results = []

    for i, r in enumerate(response["results"], 1): #here i stand for index(or item number) which start from 1: r stand for results, On each loop, r is one dictionary.
        title = r.get("title","unknown")
        url = r.get("url","")
        snippet = r.get("content","").strip()
        # keep only the first 300 characters to avoid the wall of text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ",1)[0] + "..."
        results.append(f"{i}. **{title}**\n   {url}\n  {snippet}")

    return "\n\n".join(results)

