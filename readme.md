# Speak Cues

Generate audio speech files for input text specified in a file. Each cue should
be separated by a new line.

## Requirements

- Python 3
- Mac: [say command](https://ss64.com/osx/say.html) (built-in)
- Linux: [espeak](http://espeak.sourceforge.net/) (`sudo apt install espeak`)

## Usage

```bash
speak_cues.py [-h] [--in INFILE] [--out OUTDIR]

optional arguments:
  -h, --help    show this help message and exit
  --in INFILE   The input file (default: ./cues.txt)
  --out OUTDIR  The output directory (default: ./out/)
```

