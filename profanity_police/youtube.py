from youtube_transcript_api import YouTubeTranscriptApi

from urllib import parse

class YoutubeTranscript:
    def __init__(self, url = None, video_id = None):
        """ 
            Constructor

            :param video_id: Video ID of URL
        """
        if not video_id and not url:
            # raise exception
            pass

        if video_id:
            self.video_id = video_id

        if url:
            self.video_id = self.extract_video_id(url)

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
        return None

    def extract_video_id(self, value):
        """
        Credits: https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python

        Examples:
        - http://youtu.be/SA2iWivDJiE
        - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
        - http://www.youtube.com/embed/SA2iWivDJiE
        - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        """
        query = parse.urlparse(value)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = parse.parse_qs(query.query)
                return p['v'][0]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]
        # fail?
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