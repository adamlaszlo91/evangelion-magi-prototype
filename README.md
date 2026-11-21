# evangelion-magi-prototype

[![Tests](https://github.com/adamlaszlo91/evangelion-magi-prototype/actions/workflows/tests.yml/badge.svg)](https://github.com/adamlaszlo91/evangelion-magi-prototype/actions/workflows/tests.yml)

An example of decision system using potentially* multiple LLM-s

## Features
- Make decisions based on 3 different* LLM responses

## Screenshots

General request

![screenshot 1](media/screenshot.png)

## Usage
### Prerequisites
- [Ollama](https://ollama.com/), running on local
- [llama3.1](https://ollama.com/library/llama3.1) model installed with Ollama

### Install dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Generate decision proposal
```
python3 main.py
```
