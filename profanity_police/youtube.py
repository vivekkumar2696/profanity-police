from youtube_transcript_api import YouTubeTranscriptApi

class YoutubeTranscript:
    def __init__(self, video_id):
        self.video_id = video_id

    def get_original_transcript(self, language_code = 'en'):
        """
            Returns the transcript in the required language if the video owner has added
            None if not found

            :param language_code: Language code for which the transcript needs to be generated

            :return: List of dictionaries
                     The dictionary consists of 3 keys, i.e. text, start, duration
        """
        transcript_list = YouTubeTranscriptApi.list_transcripts(self.video_id)
        for transcript in transcript_list:
            if transcript.language_code == language_code:
                return transcript.fetch()
        # transcript = transcript_list.find_generated_transcript(['en'])
        return None

    def get_transcript(self, language_code = 'en'):
        """
            Returns the transcript in the required lanugage either original or translated
            None if not found

            :param language_code: Language code for which the transcript needs to be generated

            :return: List of dictionaries
                     The dictionary consists of 3 keys, i.e. text, start, duration
        """
        output = {"transcript": None, "translated": False, "original": False}

        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(self.video_id)
            for transcript in transcript_list:
                print(transcript.language_code)
                if transcript.language_code == language_code:
                    output["transcript"] = transcript.fetch()
                    output["translated"] = False
                    output["original"] = True
                    return output

            for transcript in transcript_list:
                if transcript.is_translatable:
                    translated_transcript = transcript.translate(language_code)
                    output["transcript"] = translated_transcript.fetch()
                    output["translated"] = True
                    output["original"] = False
                    return output

        except Exception as e:
            return None

        return None