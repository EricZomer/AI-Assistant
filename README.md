# AI-Assistant

## Overview
A project to setup an AI assistant to chat with, which responds to you with audio. Using Open AI but eventually will integrate with locally installed AI programs as well.

The project will let you record an audio clip with your microphone and call OpenAI Whisper to generate text from it. That text is used to call Chat-GPT 3.5, and the returned text is then sent to OpenAI TTS which generates an audio clip from the response.

I have limited it to a single question/response per run right now, just to avoid generating too many requests to Open AI at once.

## Improvements
Speed is definitely an issue, it can take 5-20 seconds for a response which is too long if this is a conversation AI application. This is mostly due to the text-to-speech using OpenAI TTS, might be unavoidable for now but is a field that is improving each day. A local text-to-speech application might be able to respond faster depending on the hardware used.

## To Do
Integrate with local text generation (LM Studio), text-to-img (SD) and text-to-speech (TBD) AIs

Allow it to run constantly, only calling the APIs when prompted

Use GPT-4 Vision to access webcam footage or a screenshot of the desktop

Record other audio, allow it to be sent and analyzed
