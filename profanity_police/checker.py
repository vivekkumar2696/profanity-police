from profanity_police.data.data import *

import re

class Checker:
    def __init__(self):
        pass

    def get_swear_words(self, language_code = 'en'):
        """
            Helper function to get the swear words for a particular lanugage code from the static data folder

            :param language_code: Language code for which the transcript needs to be generated

            :return: dictionary of all the swear words with static value of 1 for all
        """
        words = []
        if language_code:
            language_code = re.split(r"[^a-zA-Z0-9\s]", language_code)[0]
        else:
            language_code = "en"

        try:
            return eval(language_code)
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

        for line in transcript:
            text = line['text'].lower()
            line_words = text.split()
            found = []
            for word in line_words:
                word = word.rstrip('\n')
                if swear_words.get(word):
                    found.append(word)
            if len(found):
                line["found"] = found
                swear_words_in_transcript.append(line)

        return swear_words_in_transcript
