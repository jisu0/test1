#! /usr/bin/env python

mport readtxt
l = readtxt.read_tsv("read_sample.tsv")
readtxt.to_json(l)
