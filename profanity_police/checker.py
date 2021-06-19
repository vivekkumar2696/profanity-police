class Checker:
    def __init__(self):
        pass

    def get_swear_words(self, language_code = 'en'):
        words = []
        print(language_code)
        if language_code:
            language_code = language_code.split(r"[^a-zA-Z0-9\s]")[0]
            print(language_code)
        else:
            language_code = "en"

        with open('./profanity_police/data/{0}'.format(language_code),'r') as f:
            for line in f:
                words.append(line)
        return words

    def swear_word_check(self, transcript, language_code = 'en', encode = False):
        swear_words = self.get_swear_words(language_code)

        swear_words_in_transcript = []

        # TODO: O(n3) Awful, improve this
        for line in transcript:
            text = line['text'].lower()
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
                        if swear_word == word:
                            swear_words_in_transcript.append(line)
                            break

        return swear_words_in_transcript
