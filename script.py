from profanity_police.checker import Checker
from profanity_police.youtube import YoutubeTranscript

y_transcript = YoutubeTranscript("MLdXYEWTC1k")

checker = Checker()
transcript = y_transcript.get_transcript(language_code = "hi")
if not transcript:
    print("Transcript not found")
else:
    print(transcript["transcript"][0])
    swear_words_in_transcript = checker.check_swear_word(transcript["transcript"], "hi")
    print(swear_words_in_transcript)
    # with open("z", "w+") as f:
    #     for line in swear_words_in_transcript:
    #         f.write(str(line["start"]))
    #         f.write(line["text"])


    # print(transcript["transcript"])
    # print(transcript["original"], transcript["translated"])

