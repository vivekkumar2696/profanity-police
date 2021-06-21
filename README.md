# Profanity Police
This is a python API which allows you to check for swear words in a youtube video, srt file, text file, custom source with multi language support. There are additional features like getting youtube transcript of a video, srt parser etc.

[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](http://opensource.org/licenses/MIT)  [![image](https://img.shields.io/pypi/v/profanity-police.svg)](https://pypi.org/project/profanity-police/) [![image](https://img.shields.io/pypi/pyversions/profanity-police.svg)](https://pypi.org/project/profanity-police/)



# Install

Install package using pip
```
pip install profanity-police
```
If you want to use it from source, you'll have to install the dependencies manually:
```
pip install -r requirements.txt
```

# API

## Youtube
Basic implementation to check for swear words in a youtube video in a particular language

```python
from profanity_police.transcript_checker import TranscriptChecker

checker = TranscriptChecker()
print(checker.check_transcript(source = "youtube", url = "https://www.youtube.com/watch?v=Vev2ybF2Z6g", language_code = "en"))
# video id can be passed directly instead of url if needed
# print(checker.check_transcript(source = "youtube", video_id = "Vev2ybF2Z6g", language_code = "hi"))
```
This would print something like this:-
```
[
   {
      "text":"The whole fucking bruhaha was happening..",
      "start":298.91,
      "duration":2.06,
      "found":[
         "fucking"
      ]
   },
   {
      "text":"What the fuck is happening?",
      "start":330.99,
      "duration":0.91,
      "found":[
         "fuck"
      ]
   },
   {
      "text":"Shit scripts how do you say it's shit?",
      "start":1218.77,
      "duration":1.63,
      "found":[
         "shit"
      ]
   }
]
```
The duration is depicted in seconds.

Get youtube transcript for a video
```python
from profanity_police.youtube import YoutubeTranscript

y_transcript = YoutubeTranscript(url = "https://www.youtube.com/watch?v=Vev2ybF2Z6g")
# Get the original transcripts available for a video
y_transcript.get_original_languages()

# Get the languages to which the video can be translated to
y_transcript.get_translation_languages()

transcript_en = y_transcript.get_transcript(language_code = "en-GB")
transcript_fr = y_transcript.get_transcript(language_code = "fr")
transcript_hi = y_transcript.get_transcript(language_code = "hi")
```

## Custom File

### SRT file
```python
from profanity_police.transcript_checker import TranscriptChecker

checker = TranscriptChecker()
swear_phrases = checker.check_transcript(source = "file", file_path = "sample_srt_files/panchayat_episode_6.srt", file_type = "srt", language_code = "en")
print(swear_phrases)
```

### Text file

```python
from profanity_police.transcript_checker import TranscriptChecker

checker = TranscriptChecker()

swear_phrases = checker.check_transcript(source = "file", file_path = "y", file_type = "txt", language_code = "en")
print(swear_phrases)
```

# Additional APIs

### Custom checker
```python
from profanity_police.checker import Checker
checker = Checker()
transcript = [{"text": "What is your name?"}, {"text": "shut the fuck up"}]
language_code = "en"
# `transcript` needs to be a list of dictionaries with one mandatory key - `text` 
swear_words_in_transcript = checker.check_swear_word(transcript, language_code)
```             
### SRT text Extractor
```python
from profanity_police.srt_extractor import SrtExtractor
file_path = "sample_srt_files/panchayat_episode_3.srt"
transcript = SrtExtractor().extract_text(file_path)
"""
transcript is a list of dictionary with the below format
[
    {"text": "what is your name?", "start": 10, "end": 12}
]
start and end are in seconds
"""
```

## Languages

For swear word checker

| Name             | Code |
| ---------------- | ---- |
| [English](en)    | en   |
| [French](fr)     | fr   |
| [Hindi](hi)      | hi   |
| [Italian](it)    | it   |
| [Korean](ko)     | ko   |
| [Portuguese](pt) | pt   |
| [Russian](ru)    | ru   |
| [Spanish](es)    | es   |

For youtube translation:-
All languages supported by youtube.

If you liked it and it was helpful, then
<a href="https://www.buymeacoffee.com/vivekkumar2696" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

# License
MIT
