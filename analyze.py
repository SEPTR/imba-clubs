#!/usr/bin/env python

import json
import nltk
import os
import re


# Replace all non-whitespace, non-alphanumeric characters in club names.
SUB_RE = re.compile(r"[^\sa-zA-Z0-9]+")


if __name__ == "__main__":
    with open(os.path.join("clubs", "clubs.json")) as f:
        clubs_string = re.sub(SUB_RE, "", " ".join([d["name"].lower() for d in json.load(f)]))
        tokens = nltk.WhitespaceTokenizer().tokenize(clubs_string)
        freq_dist = nltk.FreqDist(tokens)
        for k, v in freq_dist.items():
            if v > 1:
                print k, v
