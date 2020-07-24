# Mask Detector 😷
> EN: Project created for COVID-19 challenge by the robotics team: Team ProdiXy
> PT-BR: Projeto utilizado no desafio COVID-19 pela equipe de robótica Team ProdiXy

Face mask detector for people. Created during quarantine caused by COVID19. That is my first Python and Machine Learning project and I did not develop all the source code, check the "How it was developed?" section of this README file. 

## Development setup ⚒️

First of all you should need Python3 installed (and pip), to install python3 check the official website of Python: https://www.python.org/downloads/

After that, you need install project dependencies using CLI (Command Line Interface) running this line of code on root folder:

```sh
pip install -r requirements.txt
```

after that you can just run `python detect_mask_video.py`

## Setup variables

Optionally you can setup a Slack URL for Slack Integration, set it up on variable "slack_url" on ./config.json on root folder that you will create

Example:

```json
    {
        "slack_url": "https://hooks.slack.com/services/your/slack/here"
    }
```

## How it was developed? 🤖

This project was developed by **Nelson Kenmochi** and his team and it is a modification of another similar project, I tried to improve it in certain aspects. Check the another Github project link below 👇

https://github.com/chandrikadeb7/Face-Mask-Detection