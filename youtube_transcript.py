from youtube_transcript_api import YouTubeTranscriptApi

def extract_transcript(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[-1]

        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        transcript_text = ""
        for i in transcript:
            transcript_text += " " + i["text"]

        return transcript_text
    except Exception as e:
        print(f"Error extracting transcript: {e}")
        return None
