import os
import time
from fastapi import FastAPI
from twitter_client import poll_twitter_mentions
from gpt_drafter import draft_reply
from state_manager import save_message, get_messages, flag_priority
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/messages")
def list_messages():
    return get_messages()

@app.post("/process")
def process():
    mentions = poll_twitter_mentions()
    results = []
    for mention in mentions:
        if not mention.get("responded"):
            draft = draft_reply(mention["text"])
            is_priority = flag_priority(mention["text"])
            save_message(
                mention_id=mention["id_str"],
                text=mention["text"],
                draft=draft,
                priority=is_priority
            )
            results.append({"id": mention["id_str"], "draft": draft, "priority": is_priority})
    return results

if __name__ == "__main__":
    # For local dev: poll every N seconds
    while True:
        process()
        time.sleep(60)  # Poll every 60s
