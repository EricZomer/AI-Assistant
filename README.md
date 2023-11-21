# AI-Assistant

## Overview
A project to setup an AI assistant to chat with, which responds to you with audio. Using Open AI but eventually will integrate with locally installed AI programs as well

The project will create an audio clip from your microphone and call OpenAI Whisper to generate text from it. That text is used to call Chat-GPT 3.5, and the returned text is then sent to OpenAI TTS which generates an audio clip from it.

Right now you can converse with the AI using Chat-GPT, using a microphone to ask a question, and getting an audio response about 5-20 seconds later
Have limited it to a single question/response per run right now, just to avoid generating too many requests to Open AI

## Improvements:
Speed is definitely an issue, can take 5-20 seconds for a response which is a bit much if this was to be a conversation AI application. However this is mostly due to the text-to-speech OpenAI TTS, and that is a field that is improving day by day right now, so that might be solved. A local text-to-speech application might also be able to respond faster depending on the hardware.

## To Do:
Integrate with local text generation (LM Studio), text-to-img (SD) and text-to-speech (TBD) AIs
Allow it to run constantly, only calling the APIs when prompted
Use GPT-4 Vision to access webcam footage or a screenshot of my desktop
Record other audio, allow it to be sent and analyzed