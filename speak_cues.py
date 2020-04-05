#!/usr/bin/env python
"""Generate audio speech files for input text."""

import argparse
import platform
import re
import os
import subprocess


SPEAK_CMDS = {
    'Linux':  'espeak -v en-us -w "{}.wav" "{}"',
    'Darwin': 'say -v Susan -o "{}.wav" --data-format=LEF32@22050 "{}"'
}

def cue_to_filename(cue):
    """Given a cue as text, return a filename string. All characters other than
    alphanumerics are replaced by underscores."""
    return re.sub(r'[^A-Za-z0-9]', '_', cue)

def gen_cues(infile, outdir, speak_cmd):
    """Given an input file of text cues separated by newlines and an outdir,
    generate sound files for each cue and store in outdir."""
    os.makedirs(outdir, exist_ok=True)
    with open(infile) as inf:
        txt_cues = inf.read().split('\n')
        for cue in txt_cues:
            if len(cue) > 0:
                cmd = speak_cmd.format(os.path.join(outdir,
                                                    cue_to_filename(cue)), cue)
                print('Running: ', cmd)
                res = subprocess.check_output(cmd, shell=True)

def main():
    """Main function"""
    arg_parser = argparse.ArgumentParser(description='Generate audio speech'
                                         ' files for input text. Each cue should'
                                         ' be separated by a new line.')
    arg_parser.add_argument('--in', dest='infile', default='./cues.txt',
                            help='The input file (default: ./cues.txt)')
    arg_parser.add_argument('--out', dest='outdir', default='./out/',
                            help='The output directory (default: ./out/)')
    args = arg_parser.parse_args()
    print(args)
    print('infile = {}'.format(args.infile))
    print('outdir = {}'.format(args.outdir))
    print('OS     = {}'.format(platform.system()))
    speak_cmd = SPEAK_CMDS[platform.system()] if platform.system() in SPEAK_CMDS else 'echo "No matching operating system"'
    gen_cues(args.infile, args.outdir, speak_cmd)

if __name__ == "__main__":
    main()
