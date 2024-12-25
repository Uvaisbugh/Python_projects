import praw
import os

# Initialize the Reddit instance
reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT"),
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD")      
)

subreddit = reddit.subreddit("all")

# Monitor comments
try:
    for comment in subreddit.stream.comments(skip_existing=True):
        if "readit" in comment.body.lower():
            # Avoid replying to itself
            if comment.author.name != reddit.user.me().name:
                try:
                    comment.reply("Read it!")
                    print(f"Replied to comment by {comment.author.name}")
                except praw.exceptions.APIException as e:
                    print(f"API error: {e}")
                except Exception as e:
                    print(f"Unexpected error: {e}")

except KeyboardInterrupt:
    print("Bot stopped manually.")
except Exception as e:
    print(f"An error occurred: {e}")
