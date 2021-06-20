from profanity_police.checker import Checker
from profanity_police.youtube import YoutubeTranscript
from profanity_police.exceptions import TranscriptNotFoundError, InvalidArgumentError

from profanity_police.srt_extractor import SrtExtractor

class TranscriptChecker():

    def _pre_check(self, source, file_type, file_path, url, video_id, language_code):
        """
            Helper function to check the arguments for 'check_transcript' function
        """
        if not source:
            raise InvalidArgumentError("'source' needs to be passed")
        if source == "file":
            if not file_type:
                raise InvalidArgumentError("'file_type' needs to be passed")

            if not file_path:
                raise InvalidArgumentError("'file_path' needs to be passed")

            if file_type not in ["txt", "srt"]:
                raise InvalidArgumentError("'file_type' needs to be from the following values. ['txt', 'srt']")

            if language_code not in ["hi", "en"]:
                raise InvalidArgumentError("'language_code' needs to be from the following values ['en', 'hi'] for 'file' as source")
        elif source == "youtube":
            if not url and not video_id:
                raise InvalidArgumentError("For `source` as 'youtube', either `url` or `video_id` needs to be passed")
        else:
            raise InvalidArgumentError("'source' needs to be from the following values ['file', 'youtube']")

    def check_transcript(self, source = "file", file_type = "srt", file_path = None, url = None, video_id = None, language_code = "en"):
        """
            Checks if transcript has swear words. 
            Transcript can come from multiple sources, i.e. file, youtube

            If a transcript comes from a file there are two possible cases handled, SRT file and txt file

            :param source: Source of transcript. There are two possible values "file" and "youtube"
                            Default: "file"
            :param file_type: If source is "file" then file_type must contain the type of file. Currently there are two options, "txt" and "srt"
                            Default: "srt 
            :param file_path: If source is "file" then file_path must contain the path of the transcript file
                            Default: None
            :param url: If source is "youtube" then either url or video_id must be specified
                            Default: None
            :param video_id: If source is "youtube" then either url or video_id must be specified
                            Default: None
            :param langauge_code: Language of the transcript
                            Default: en

            :return: List of dictionaries with texts which contain swear words

        """
        self._pre_check(source, file_type, file_path, url, video_id, language_code)

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

        return None