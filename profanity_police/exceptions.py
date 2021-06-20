class InvalidYoutubeURLError(Exception):
    def __init__(self, message, errors = None):
        super().__init__(message)
        self.errors = errors

class TranscriptNotFoundError(Exception):
    def __init__(self, message, errors = None):
        super().__init__(message)
        self.errors = errors