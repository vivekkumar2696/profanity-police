from profanity_police.checker import Checker
from profanity_police.youtube import YoutubeTranscript

y_transcript = YoutubeTranscript(url = "https://www.youtube.com/watch?v=Vev2ybF2Z6g&ab_channel=AllIndiaBakchod", video_id = "Vev2ybF2Z6g")

checker = Checker()
transcript = y_transcript.get_transcript(language_code = "en-GB")
if not transcript:
    print("Transcript not found")
else:
    swear_words_in_transcript = checker.check_swear_word(transcript["transcript"], "en-GB")
    print(swear_words_in_transcript)
