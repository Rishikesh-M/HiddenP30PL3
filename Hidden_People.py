import requests
from bs4 import BeautifulSoup

def search_username(username):
    social_media_websites = {
        "Facebook": "https://www.facebook.com/",
        "Twitter": "https://twitter.com/",
        "Instagram": "https://www.instagram.com/",
        "TikTok": "https://www.tiktok.com/",
        "YouTube": "https://www.youtube.com/",
        "Reddit": "https://www.reddit.com/",
        "Twitch": "https://www.twitch.tv/",
        "GitHub": "https://github.com/",
        "LinkedIn": "https://www.linkedin.com/"
    }

    results = {}

    for platform, url in social_media_websites.items():
        response = requests.get(url + username)
        soup = BeautifulSoup(response.content, "html.parser")

        if response.status_code == 200:
            if soup.find("title"):
                title = soup.find("title").text.strip()
                if username in title:
                    results[platform] = "Found"
                else:
                    results[platform] = "Not Found"
            else:
                results[platform] = "Not Found"
        else:
            results[platform] = "Not Found"

    return results

username = input("Enter a username to search: ")
results = search_username(username)

print("Results:")
for platform, result in results.items():
    print(f"{platform}: {result}")