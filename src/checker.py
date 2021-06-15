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

    def get_transcript_test(self, video_id, language_code = 'hi'):
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        for x in transcript_list:
            # print(x)
            if x.language_code == 'en':
                translated_transcript = x.translate('hi')
                return translated_transcript.fetch()

        return None

    def get_swear_words(self, language_code = 'en'):
        words = []
        with open('./src/data/{0}'.format(language_code),'r') as f:
            for line in f:
                words.append(line)
        return words

    def swear_word_check(self, video_id, language_code = 'en', encode = False):
        swear_words = self.get_swear_words(language_code)
        transcript = self.get_transcript_test(video_id, language_code)

        swear_words_in_transcript = []

        # TODO: O(n3) Awful, improve this
        for line in transcript:
            text = line['text']
            line_words = text.split()
            for swear_word in swear_words:
                swear_word = swear_word.rstrip('\n')
                for word in line_words:
                    word = word.rstrip('\n')
                    if encode:
                        if swear_word.encode("utf-8") in word.encode("utf-8"):
                            swear_words_in_transcript.append(line)
                            break
                    else:
                        if swear_word in word:
                            swear_words_in_transcript.append(line)
                            break

        return swear_words_in_transcript
