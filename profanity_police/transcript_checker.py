from profanity_police.checker import Checker
from profanity_police.youtube import YoutubeTranscript
from profanity_police.exceptions import TranscriptNotFoundError

class TranscriptChecker():
    def __init__(self):
        pass

    def _pre_check():
        pass

    def check_transcript(self, source = "file", url = None, video_id = None, language_code = "en"):
        if source == "file":
            # WIP
            pass
        elif source == "youtube":
            if url or video_id:
                y_transcript = YoutubeTranscript(url = url, video_id = video_id)

                checker = Checker()
                transcript = y_transcript.get_transcript(language_code = language_code)
                if not transcript:
                    # print("Transcript not found")
                    raise TranscriptNotFoundError("Transcript not found for the video!")
                else:
                    swear_words_in_transcript = checker.check_swear_word(transcript["transcript"], language_code)
                    return swear_words_in_transcript
            else:
                pass
        else:
            # Raise exception
            pass

        return None