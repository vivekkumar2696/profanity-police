from youtube_transcript_api import YouTubeTranscriptApi

class Checker:
    def __init__(self):
        pass

    def get_transcript(self, video_id, language_code = 'en'):
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        for transcript in transcript_list:
            if transcript.language_code == language_code:
                return transcript.fetch()
        # transcript = transcript_list.find_generated_transcript(['en'])
        return None

    def get_swear_words(self, language_code = 'en'):
        words = []
        with open('./src/data/en','r') as f:
            for line in f:
                words.append(line)
        return words

    def swear_word_check(self, video_id, langauge_code = 'en'):
        swear_words = self.get_swear_words()
        transcript = self.get_transcript("gIwgSpEg6ZY")
        # print([word for word in swear_words if word in [t['text'].lower() for t in transcript]])
        swear_words_in_transcript = []

        # TODO: O(n3) Awful, improve this
        for line in transcript:
            text = line['text']
            line_words = text.split()
            for swear_word in swear_words:
                for word in line_words:
                    if swear_word in word:
                        swear_words_in_transcript.append(line)
                        break

        return swear_words_in_transcript
