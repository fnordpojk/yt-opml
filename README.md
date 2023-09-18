# yt-opml
Fetch subscriptions from YouTube API, create OPML file for RSS readers

## Getting started
Use the guide at https://developers.google.com/youtube/v3/getting-started to set up your API project, enable the YouTube Data API v3, and create an OAuth 2.0 Client ID for a desktop app.

Then download the client secret JSON file, and replace the dummy yt-opml-secret.json with it.

## Usage
Run the yt-opml.py script. It will open a URL, which will lead you through granting the script permissions to access your YouTube account.

If everything goes well, you should now have a file called yt-opml.opml in the current directory, containing all your YouTube subscriptions' RSS feeds.

Note that the script has absolutely no error checking or other niceties - it's a quick hack, handle it as such.