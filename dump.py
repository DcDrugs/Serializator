#!/usr/bin/env python3
from factory.factory import serializer
import argparse


def dump(in_file, out_file):
    ifile = open(in_file, "r")
    ofile = open(out_file, "w")
    obj = types[in_file.split(".")[-1].lower()].unpack(ifile)
    types[out_file.split(".")[-1].lower()].pack(obj, ofile)
    ifile.close()
    ofile.close()


types = {
    "yaml": serializer.get_parser("yaml"),
    "json": serializer.get_parser("json"),
}
parser = argparse.ArgumentParser(description="Parser")
parser.add_argument("in_file", type=str, help="Input file for pars")
parser.add_argument("out_file", type=str, help="Output file to load")
args = parser.parse_args()

dump(args.in_file, args.out_file)
