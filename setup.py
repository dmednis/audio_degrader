from setuptools import setup, find_packages

setup(
    name = 'audio_degrader',
    version = '1.0.0',
    url = 'https://github.com/mypackage.git',
    author = 'Davis Mednis',
    author_email = 'davis@medn.is’,
    description = 'This tool allows to introduce controlled degradations to audio.',
    packages = find_packages(),    
    install_requires = ['numpy >= 1.11.1', 'librosa >= 0.6.0'],
)
