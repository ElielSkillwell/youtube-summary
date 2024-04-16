import os

from dotenv import load_dotenv
from pytube import YouTube
import assemblyai as aai

YT_URL = 'https://www.youtube.com/watch?v=VSxF0bb-JH4&ab_channel=jayzern'

def get_youtube_audio(url, file):
    yt = YouTube(url)
    print(f'Title: {yt.title}')

    streams = yt.streams.filter(only_audio=True)
    streams[0].download(filename=file)


def get_transcript(file_name):
    aai.settings.api_key = os.getenv('ASSEMBLY_AI')

    transcriber = aai.Transcriber()
    config = aai.TranscriptionConfig(
        # speaker_labels=True, 
        # dual_channel=True,
        # language_code='fi'
        summarization=True,
        summary_model=aai.SummarizationModel.informative,
        summary_type=aai.SummarizationType.bullets
        )
    transcript = transcriber.transcribe(f'./{file_name}', config)

    return transcript

def main(file_name):    
    load_dotenv()

    get_youtube_audio(YT_URL, file_name)

    transcript = get_transcript(file_name)
    print(transcript.summary)


if __name__ == '__main__':
    main('test.mp3')