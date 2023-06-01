import praw
import pandas as pd

reddit = praw.Reddit(
    client_id='P04n_Z8BzmWgxpUom1qi9Q',
    client_secret='hpNyrrO1fH54EL-NJbUHU_qsY35kNQ',
    user_agent='bitcoin data scraper',
)

subreddit = reddit.subreddit("bitcoin")

rows = []

batch_size = 500
before_date = 1682636400  # Unix timestamp for January 1, 2013 (adjust as needed)

while True:
    new_posts = subreddit.new(limit=batch_size, params={"before": before_date})

    batch_rows = list(new_posts)  # Collect the praw Submission objects in a list

    for post in batch_rows:
        row = {
            "Title": post.title,
            "URL": post.url,
            "Score": post.score,
            "ID": post.id,
            "Author": post.author,
            "Created UTC": post.created_utc,
            "Number of Comments": post.num_comments,
            "Self Text": post.selftext,
            "Subreddit": post.subreddit,
            "Upvote Ratio": post.upvote_ratio,
            "Is Self Post": post.is_self,
            "Is Pinned": post.pinned,
            "Is Stickied": post.stickied,
            "Is Locked": post.locked,
            "Edited UTC": post.edited,
            "Gilded Count": post.gilded
        }

        rows.append(row)

    if len(batch_rows) < batch_size:
        break

    before_date = min(post.created_utc for post in batch_rows)

df = pd.DataFrame(rows)
print(df.head())
df.to_csv('reddit_bitcoin_datafinal1.csv', index=False)
