
import requests
import datetime

# Twitter Bearer Token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJnC0AEAAAAADcmD5womCa5edQVO2qTdCzFbWq8%3Dx2hJcfOeRmaji8mRhcWxT7J5boLrptmKQKi6TUzMiFCKiDL42x"

# Telegram Bot Token and Chat ID
BOT_TOKEN = "7928766798:AAHJpbX1WJ5rET5Sk4QlkCnl4zWYkxVrFZE"
CHAT_ID = "5142973821"

# Step 1: Get recent trending tweets
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

query = "web3 OR nft OR crypto lang:en -is:retweet"
url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=5&tweet.fields=public_metrics,created_at"

response = requests.get(url, headers=headers)

# Step 2: Build Telegram message
if response.status_code == 200:
    tweets = response.json().get("data", [])
    if not tweets:
        message = "No trending tweets found at the moment."
    else:
        message = "🔥 *Top Web3 Tweets Today:*

"
        for tweet in tweets:
            tweet_url = f"https://twitter.com/i/web/status/{tweet['id']}"
            content = tweet['text'].replace("\n", " ").strip()
            message += f"• {content[:100]}...
🔗 {tweet_url}

"
else:
    message = f"Error fetching tweets: {response.status_code}\n{response.text}"

# Step 3: Send message to Telegram
tg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": message,
    "parse_mode": "Markdown"
}
tg_response = requests.post(tg_url, data=data)
print("Telegram response:", tg_response.status_code, tg_response.text)
