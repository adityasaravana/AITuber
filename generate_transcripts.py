# This file generates transcripts and saves them to a folder as .txt files, given a list of YouTube video IDs.

from youtube_transcript_api import YouTubeTranscriptApi
from main import *
import os

transcripts = YouTubeTranscriptApi.get_transcripts(video_ids)

# Save strings to text files.
def save_string_to_file(data_string, filename):
    with open(filename, "w") as text_file:
        print(data_string, file=text_file)

# Compile each video's subtitles into transcripts.
def compile_transcripts(transcripts_data):
    compiled_transcripts = {}
    for video_id, subtitles in transcripts_data[0].items():  # Only process the first item of the tuple
        # Join all subtitle texts into one single string with a space in between each part
        transcript = ' '.join([item['text'] for item in subtitles])
        compiled_transcripts[video_id] = transcript
    return compiled_transcripts

compiled_transcripts = compile_transcripts(transcripts)

# Create a new folder for the transcripts
folder_name = f'{channel_id} Transcripts'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# For each video, create a text file named the video id and write the transcript to it
for video_id, transcript in compiled_transcripts.items():
    file_path = os.path.join(folder_name, f"{video_id}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(transcript)

print(f"Transcripts have been saved in the '{folder_name}' folder.")


