import sys
import json
import gzip

# Load the JSON file containing the Twitter data
with gzip.open(sys.argv[1], 'rt') as f:
    tweets = json.load(f)

# Define the word
word_to_search = sys.argv[2]

# Initialize the counter
count = 0

# Loop through each tweet in the data
for tweet in tweets:
    # Check if the tweet is a retweet (starts with 'RT')
   if not tweet['text'].startswith('RT'):
    # Check if the word is in the tweet text
    if word_to_search in tweet['text']:
        # If it is, increment the counter
        count += 1

# Print the total count of occurrences of the word
print(f'The word "{word_to_search}" appears {count} times in the dataset.')
