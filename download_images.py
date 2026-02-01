import urllib.request
import os

images = {
    "premium_hardwood.jpg": "https://media.istockphoto.com/id/1172535025/photo/smoking-wood-chips-for-bbq-on-white-background.jpg?s=1024x1024&w=is&k=20&c=5y8wuyUJKGdkjoRHc6ByxYWlMESF0om6ZjxWCDAC9g0=",
    "fine_sawdust.jpg": "https://images.unsplash.com/photo-1595856417769-e763131e5057?q=80&w=2070&auto=format&fit=crop"
}

if not os.path.exists("images"):
    os.makedirs("images")

for filename, url in images.items():
    try:
        print(f"Downloading {filename}...")
        # Add headers to mimic a browser to avoid some basic blocks
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        )
        with urllib.request.urlopen(req) as response, open(f"images/{filename}", 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Saved {filename}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
