from setuptools import setup, find_packages

setup(
    name='math-quiz-game',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your project requires
        'random',
    ],
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz:math_quiz',  # Adjust this based on your project structure
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple math quiz game in Python',
    url='https://github.com/yourusername/math-quiz-game',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
