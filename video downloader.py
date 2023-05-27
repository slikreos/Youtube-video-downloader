from pytube import YouTube

query = input("Enter what you would like to download ")
video = YouTube.search(query)

# Print out the search results
for i in range(len(video)):
    print(f"{i+1}. {video[i].title}")

# Ask the user which video they want to download
choice = int(input("Enter the number of the video you want to download: "))
url = video[choice-1].watch_url

# Create a YouTube object
yt = YouTube(url)

# Get the first stream
stream = yt.streams.first()

# Downloads the video
stream.download()
