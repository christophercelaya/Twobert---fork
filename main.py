#!/usr/bin/env python3

# import the quote_plus function from the urllib.parse module
from urllib.parse import quote_plus

# import the praw module for interacting with the Reddit API
import praw

# Define a list of phrases to match against post titles
LIST = ["TCC", "The Cosmic Circus", "TheCosmicCircus", "Lizzie Hill", "Lizzy Hill", "Alex Perez", "Alex P"]

# Define the text of the reply message
REPLY_TEMPLATE = " We have detected this post to pertain to **Lizzie Hill / The Cosmic Circus**, which the community voted as a **Tier 1 - Approved and Trustworthy** source during the latest round of Source Accuracy Calibrations. As of March 9, 2023, they had a 87.78% accuracy rate in our [Source Accuracy Database](https://docs.google.com/spreadsheets/d/18Xrwgf-AzNmq3Bo46cNHUvoTLKD9Yre0vNr7pxz63WQ/edit#gid=381085160)"

# Define a function to handle Reddit submissions
def main():
    # Initialize a PRAW Reddit instance with API credentials
    reddit = praw.Reddit(
        client_id="jdcn5TE8vmq6-p-KDnZAGw",
        client_secret="q_aIhaBLyfRq10aM9MSHKrNGN69omg",
        password="B0mbadbomberin.!",
        user_agent="Twobert 1.0",
        username="HuebertTMann",
        check_for_async=False
    )

    # Select the subreddit to monitor
    subreddit = reddit.subreddit("MssCss")

    # Loop through new submissions in the subreddit
    for submission in subreddit.stream.submissions():
        # Process each submission
        process_submission(submission)

# Define a function to process each Reddit submission
def process_submission(submission):
    # Convert the submission title to lowercase for easier matching
    normalized_title = submission.title.lower()

    # Loop through the list of phrases to match against the title
    for list_phrase in LIST:
        # Check if the phrase appears in the normalized title
        if list_phrase in normalized_title:
            # If a matching phrase is found, URL-encode the title and format the reply message
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)

            # Log the post being replied to and the reply text
            print(f"Replying to: {submission.title}")
            print(f"Reply text: {reply_text}")

            # Post the reply message to the submission
            submission.reply(reply_text)

            # A reply has been made so do not attempt to match other phrases.
            break

# Run the main function if this script is executed as the main program
if __name__ == "__main__":
    main()
