import pysrt

class SrtExtractor():
    def __init__(self):
        pass

    def extract_text(self, file, encoding = None):
        """
            Extract text from an SRT file
        """
        if encoding:
            subs = pysrt.open(file, encoding = encoding)
        else:
            subs = pysrt.open(file)

        output = []
        for sub in subs:
            d = {}
            d["text"] = sub.text
            d["start"] = sub.start.hours*3600 + sub.start.minutes*60 + sub.start.seconds
            d["end"] = sub.end.hours*3600 + sub.end.minutes*60 + sub.end.seconds
            output.append(d)
        return output