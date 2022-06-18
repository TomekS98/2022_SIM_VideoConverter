# 2022_SIM_VideoConverter

Creates one output stream from multiple RTSP input streams.

## Instalation

Make sure you are using Python 3.9.10 \
All required packaged are inside requirements.txt. 

```bash
pip install -r requirements.txt
```

## Usage

```bash
main.py url1 url2 url3 url4
```

Example

```bash
main.py rtsp://localhost:8554/1 rtsp://localhost:8554/2 rtsp://localhost:8554/3 rtsp://localhost:8554/4
```