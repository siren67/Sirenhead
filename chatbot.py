import os
import textwrap
from typing import List

import requests


GOOGLE_API_URL = "https://www.googleapis.com/customsearch/v1"


def fetch_google_snippets(query: str, api_key: str, cse_id: str, max_results: int = 5) -> List[str]:
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": query,
        "num": max_results,
    }
    response = requests.get(GOOGLE_API_URL, params=params, timeout=20)
    response.raise_for_status()
    payload = response.json()
    items = payload.get("items", [])
    return [item.get("snippet", "") for item in items if item.get("snippet")]


def build_answer(snippets: List[str]) -> str:
    if not snippets:
        return "I couldn't find any results to answer that."
    combined = " ".join(snippets)
    return textwrap.shorten(combined, width=600, placeholder="...")


def main() -> None:
    api_key = os.getenv("GOOGLE_API_KEY")
    cse_id = os.getenv("GOOGLE_CSE_ID")
    if not api_key or not cse_id:
        raise SystemExit(
            "Missing GOOGLE_API_KEY or GOOGLE_CSE_ID environment variables. "
            "See README.md for setup instructions."
        )

    print("Google-backed chatbot. Type 'exit' to quit.")
    while True:
        query = input("You: ").strip()
        if query.lower() in {"exit", "quit"}:
            break
        if not query:
            continue
        snippets = fetch_google_snippets(query, api_key, cse_id)
        answer = build_answer(snippets)
        print(f"Bot: {answer}\n")


if __name__ == "__main__":
    main()
