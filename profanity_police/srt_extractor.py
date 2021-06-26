import pysrt

class SrtExtractor():
    def extract_text(self, file, encoding = None):
        """
            Extract text from an SRT file

            :param file: file_path of SRT file
            :param encoding: Encoding if present

            :return: List of dictionary in following keys
                    "text": Transcript text
                    "start": Start time in seconds
                    "end": End time in seconds
                    e.g. 
                    [
                        {
                            "text": "Hello",
                            "start": 2,
                            "end": 4
                        }
                    ] 
        """
        if encoding:
            subs = pysrt.open(file, encoding = encoding)
        else:
            subs = pysrt.open(file)

        output = []
        for sub in subs:
            d = {}
            d["text"] = sub.text
            d["start"] = sub.start.hours*3600 + sub.start.minutes*60 + sub.start.seconds + sub.start.milliseconds*0.001
            print(sub.start, d["start"])
            d["end"] = sub.end.hours*3600 + sub.end.minutes*60 + sub.end.seconds + sub.end.milliseconds*0.001
            output.append(d)
        return output