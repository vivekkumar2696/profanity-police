class TextExtractor:
    """
        Extract text from a txt file
    """
    def extract_text(self, file, encoding = None):
        """
            Extract text from an text

            :param file: file_path of text file

            :return: List of dictionary in following keys
                    "text": Transcript text
                    e.g. 
                    [
                        {
                            "text": "Hello",
                        }
                    ] 
        """
        output = []
        with open(file, "r") as f:
            for line in f:
                d = {}
                d["text"] = line.rstrip('\n')
                output.append(d)

        return output