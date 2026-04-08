import json
import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import praw
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)


def get_reddit_client() -> praw.Reddit:
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "CSS-Project/1.0"),
    )


def fetch_top_posts(subreddit_name: str, limit: int = 5, time_filter: str = "week") -> pd.DataFrame:
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)

    posts = []
    for post in subreddit.top(time_filter=time_filter, limit=limit):
        posts.append(
            {
                "id": post.id,
                "title": post.title,
                "author": str(post.author) if post.author else "deleted",
                "score": post.score,
                "num_comments": post.num_comments,
                "created_utc": datetime.fromtimestamp(post.created_utc, tz=timezone.utc).isoformat(),
                "url": post.url,
                "selftext": post.selftext,
                "permalink": f"https://reddit.com{post.permalink}",
            }
        )

    return pd.DataFrame(posts)


def save_posts(df: pd.DataFrame, subreddit_name: str) -> None:
    csv_path = DATA_DIR / f"{subreddit_name}_top_posts.csv"
    json_path = DATA_DIR / f"{subreddit_name}_top_posts.json"

    df.to_csv(csv_path, index=False)
    df.to_json(json_path, orient="records", indent=2)

    print(f"Saved {len(df)} posts to:")
    print(f"  CSV:  {csv_path}")
    print(f"  JSON: {json_path}")


if __name__ == "__main__":
    import sys

    subreddit_name = sys.argv[1] if len(sys.argv) > 1 else "entrepreneur"
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    df = fetch_top_posts(subreddit_name, limit=limit)
    save_posts(df, subreddit_name)
    print(f"\nTop {limit} posts from r/{subreddit_name}:")
    print(df[["title", "score", "num_comments"]].to_string(index=False))
