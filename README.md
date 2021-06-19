# swear-word-checker
Python library to check for swear words in a youtube video

Install package using pip

```
 pip install git+ssh://git@github.com/vivekkumar2696/swear-word-checker.git
```

Sample python code
```
from profanity_police.checker import Checker
from profanity_police.youtube import YoutubeTranscript

y_transcript = YoutubeTranscript("MLdXYEWTC1k")

checker = Checker()
transcript = y_transcript.get_transcript(language_code = "hi")
if not transcript:
    print("Transcript not found")
else:
    swear_words_in_transcript = checker.swear_word_check(transcript["transcript"], "hi")
    print(swear_words_in_transcript)
```

