from profanity_police.checker import Checker
from profanity_police.youtube import YoutubeTranscript
from profanity_police.exceptions import TranscriptNotFoundError

from profanity_police.srt_extractor import SrtExtractor

class TranscriptChecker():
    def __init__(self):
        pass

    def _pre_check():
        pass

    def check_transcript(self, source = "file", file_path = None, file_type = "srt", url = None, video_id = None, language_code = "en"):
        if source == "file":
            if file_type == "srt":
                transcript = SrtExtractor().extract_text(file_path)
                checker = Checker()
                swear_words_in_transcript = checker.check_swear_word(transcript, language_code)
                return swear_words_in_transcript

        elif source == "youtube":
            y_transcript = YoutubeTranscript(url = url, video_id = video_id)

            transcript = y_transcript.get_transcript(language_code = language_code)
            if not transcript:
                # print("Transcript not found")
                raise TranscriptNotFoundError("Transcript not found for the video!")
            else:
                checker = Checker()
                swear_words_in_transcript = checker.check_swear_word(transcript["transcript"], language_code)
                return swear_words_in_transcript
        else:
            # Raise exception
            pass

        return None