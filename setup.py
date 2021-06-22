from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = 'profanity_police',
    version = '1.0.0',
    description = 'This is a python API which allows you to check for swear words in a youtube video, srt file, text file, custom source with multi language support. There are additional features like getting youtube transcript of a video, srt parser etc.',
    url = 'https://github.com/vivekkumar2696/profanity-police',
    author = 'Vivek Kamal Kumar',
    author_email = 'kumar.vivek2696@gmail.com',
    license = 'MIT',
    packages = ['profanity_police'],
    zip_safe = False,
    include_package_data = True,
    install_requires = required,
    keywords = ["transcript", "profanity", "profanity-detection", "swearword", "srt-parser", "youtube-transcripts", "youtube-captions"],
    classifiers=[
        'Development Status :: 3 - Alpha',# Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)