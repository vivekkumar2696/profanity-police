from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name = 'profanity_police',
    version = '1.0.0',
    description = 'A python library to check for swear words in a youtube video',
    url = 'git@github.com:vivekkumar2696/swear-word-checker.git',
    author = 'Vivek Kumar',
    author_email = 'kumar.vivek2696@gmail.com',
    license = 'unlicense',
    packages = ['profanity_police'],
    zip_safe = False,
    install_requires = required
)