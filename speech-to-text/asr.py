from faster_whisper import WhisperModel
import os
import argparse

parser = argparse.ArgumentParser(description='Run Transcription on audio file using latest whisper model.')
parser.add_argument('file_path', help='Filename to process.')
args = vars(parser.parse_args())

file_path = args['file_path']

if not os.path.isfile(file_path):
  print(f"Unable to locate a file at {file_path}")
  exit(1)

model = WhisperModel("large-v3")

segments, info = model.transcribe(file_path)
for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
