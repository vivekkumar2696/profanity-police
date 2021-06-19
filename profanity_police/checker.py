class Checker:
    def __init__(self):
        pass

    def get_swear_words(self, language_code = 'en'):
        """
            Helper function to get the swear words for a particular lanugage code from the static data folder

            :param language_code: Language code for which the transcript needs to be generated

            :return: List of all the swear words
        """
        words = []
        print(language_code)
        if language_code:
            language_code = language_code.split(r"[^a-zA-Z0-9\s]")[0]
            print(language_code)
        else:
            language_code = "en"

        try:
            with open('./profanity_police/data/{0}'.format(language_code),'r') as f:
                for line in f:
                    words.append(line)
            return words
        except Exception as e:
            return None

    def check_swear_word(self, transcript, language_code = 'en', encode = False):
        """
            Check for swear words in a particular transcript or custom text

            :param transcript: List of dictionaries
                            Each dictionary contains the details of the text that needs to be searched along with other meta data
                            Note: Text needs to be passed with the key 'text'
                            This is required as the return type contains the exact dictionary with extra information

            :return: List of dictionaries
                    Contains the same dictionary which was passed along with the following keys
                    swear_words
        """
        swear_words = self.get_swear_words(language_code)

        swear_words_in_transcript = []

        # TODO: O(n3) Awful, improve this
        # Convert the source data in a dictionary to make searching O(1)
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
