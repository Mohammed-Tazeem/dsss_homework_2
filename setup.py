from setuptools import setup, find_packages

setup(
    name='math-quiz-game',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz:math_quiz',
        ],
    },
    author='Mohammed Tazeem Khan',
    author_email='mohammed.t.khan@fau.de',
    description='A simple math quiz game in Python',
    url='https://github.com/Mohammed-Tazeem/dsss_homework_2.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
