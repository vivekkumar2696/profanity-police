# from youtube_transcript_api import YouTubeTranscriptApi
# # # print("".join([x['text'] for x in YouTubeTranscriptApi.get_transcript("gIwgSpEg6ZY")]))
# transcript_list = YouTubeTranscriptApi.list_transcripts("gIwgSpEg6ZY")
# for x in transcript_list:
#     # print(x)
#     if x.language_code == 'en':
#         translated_transcript = x.translate('hi')
#         with open('x', 'w+') as f:
#             f.write("".join([i['text'] for i in translated_transcript.fetch()]))
# # transcript = transcript_list.find_generated_transcript('hi')
# # print(transcript)
# # transcript = transcript_list.find_transcript(['hi'])
# # print(transcript.fetch())
# # translated_transcript = transcript.translate('de')
# # print(translated_transcript.fetch())
# # 

# try:
#     transcript = transcript_list.find_manually_created_transcript(['de'])
# except Exception as e:
#     print(e)
# # print(transcript)
# # if not transcript:
# #     transcript = transcript_list.find_generated_transcript(['en'])

import unicodedata
from src.checker import Checker

checker = Checker()
print(checker.swear_word_check("gIwgSpEg6ZY", "hi", True))