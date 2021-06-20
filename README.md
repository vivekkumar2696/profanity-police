# swear-word-checker
Python library to check for swear words in a youtube video or text.

[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](http://opensource.org/licenses/MIT)


# Install

Install package using pip
```
 pip install git+ssh://git@github.com/vivekkumar2696/profanity-police.git
```
If you want to use it from source, you'll have to install the dependencies manually:
```
pip install -r requirements.txt
```

# API

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

Get youtube transcript for a video
```python
from profanity_police.youtube import YoutubeTranscript

y_transcript = YoutubeTranscript(url = "https://www.youtube.com/watch?v=Vev2ybF2Z6g&ab_channel=AllIndiaBakchod")
# Get the original transcripts available for a video
y_transcript.get_original_languages()

# Get the languages to which the video can be translated to
y_transcript.get_translation_languages()

transcript_en = y_transcript.get_transcript(language_code = "en-GB")
transcript_hi = y_transcript.get_transcript(language_code = "hi")
```
