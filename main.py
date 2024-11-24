import praw
import time
from datetime import datetime

from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD")
)



reddit.read_only = True

# Current time in UNIX timestamp
current_time = time.time()

# Time one week ago in UNIX timestamp
one_week_ago = current_time - (7 * 24 * 60 * 60)  # 7 days in seconds


#-------------------------#
# url="https://www.reddit.com/r/IndianStockMarket/comments/1gyjaet/an_investment_in_knowledge_pays_the_best_interest/"

# post=reddit.submission(url=url)

# print(post.title)
# print(post.selftext)

# for comment in post.comments:
#     print(comment.body)

#-------------------------#

for submission in reddit.subreddit("IndianStockMarket").hot(limit=100):  # Fetch more posts to increase the chance of finding recent ones
    if submission.created_utc > one_week_ago:  # Check if the post is within the last 7 days
        print("Title:", submission.title)
        print("Score:", submission.score)
        print("ID:", submission.id)
        print("URL:", submission.url)
        print("Created at:", datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'))
        print("Content:",submission.selftext)
        # Iterate through the first few comments (if any)
        submission.comments.replace_more(limit=0)  # To ensure we get all comments, not more to load
        for comment in submission.comments.list()[:5]:  # Get top 5 comments
            print("Comment:", comment.body)
        print("\n\n")



