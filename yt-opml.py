# -*- coding: utf-8 -*-
#
# yt-opml.py v1.0
# written by Mattias Bergsten <fnord@fnord.nu>, licensed Apache 2.0
# Google API code from https://developers.google.com/youtube/v3/code_samples/code_snippets, licensed Apache 2.0
#
import os
import json
import html

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

OPML_HEADER = """<opml version="1.1">
<body><outline text="YouTube Subscriptions" title="YouTube Subscriptions">"""
OPML_FOOTER = """</outline></body></opml>"""
OPML_LINE = '<outline text="%(title)s" title="%(title)s" type="rss" xmlUrl="https://www.youtube.com/feeds/videos.xml?channel_id=%(channel_id)s" />'

def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "yt-opml-secret.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.subscriptions().list(
        part="snippet",
        maxResults=50,
        mine=True
    )

    with open('yt-opml.opml', 'w') as f:
    
        print(OPML_HEADER, file=f)
    
        while request is not None:
            response = request.execute()

            for sub in response['items']:
                channel_id = sub['snippet']['resourceId']['channelId']
                title = html.escape(sub['snippet']['title'])
                print(OPML_LINE % {'title': title, 'channel_id': channel_id}, file=f)

            request = youtube.subscriptions().list_next(request, response)

        print(OPML_FOOTER, file=f)

if __name__ == "__main__":
    main()
