import os
import pickle
import time
from api_key import api_dict
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from collections import defaultdict
from getpixeldude import spawn_batch

api_key = api_dict.get("KEY")
video_id = "FLl9gnSYAxQ"
thumbnail = "./thumbnail.jpg"

YOUTUBE_DATA_API_CREDENTIALS_LOCATION = "./creds/client_secret.json"
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
api_service_name = "youtube"
api_version = "v3"

credentials = None

max_results = 1000


class YoutubeClient(object):
    def __init__(self, credentials_location):
        if os.path.exists("token.pickle"):
            print("Loading credentials from file...")
            with open("token.pickle", "rb") as token:
                credentials = pickle.load(token)

        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                print("Refreshing access token...")
                credentials.refresh(Request())
            else:
                print("Fetching New Tokens...")
                flow = InstalledAppFlow.from_client_secrets_file(
                    YOUTUBE_DATA_API_CREDENTIALS_LOCATION, scopes
                )

                flow.run_local_server(
                    port=8080, prompt="consent", authorization_prompt_message=""
                )
                credentials = flow.credentials

                with open("token.pickle", "wb") as f:
                    print("Saving credentials for future use...")
                    pickle.dump(credentials, f)

        youtube_client = build(
            api_service_name, api_version, credentials=credentials
        )

        self.youtube_client = youtube_client

    def set_thumbnail(self, video_id, thumbnail):
        request = self.youtube_client.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(thumbnail)
        )
        response = request.execute()

        return response

    def get_comments(self, video_id):
        global max_results
        # create a request to get 20 comments on the video
        request = self.youtube_client.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            order="orderUnspecified")  # top comments.
        # execute the request
        response = request.execute()

        temp_items = response["items"]
        author_names = []
        for i in temp_items:
            item_info = i["snippet"]
            # the top level comment can have sub reply comments
            topLevelComment = item_info["topLevelComment"]
            comment_info = topLevelComment["snippet"]
            author_names.append(comment_info["authorDisplayName"])

        spawn_batch(author_names)
        new_client.set_thumbnail(video_id, thumbnail)
        return response


def get_comments(videoid):
    new_client.get_comments(videoid)


new_client = YoutubeClient(YOUTUBE_DATA_API_CREDENTIALS_LOCATION)

get_comments(video_id)
