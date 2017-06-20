#! /usr/local/bin/python
# -*- coding: utf-8 -*-
#
# estimate_jnt.py
#   First ver.: 2017-06-09
#
#   Copyright 2017
#       Kazuhiro KOBAYASHI <kobayashi.kazuhiro@g.sp.m.is.nagoya-u.ac.jp>
#
#   Distributed under terms of the MIT license.
#

"""
estimate joint feature vector of the speaker pair using GMM

"""

import argparse

from sprocket.util.yml import PairYML
from sprocket.util.jnt import JointFeatureExtractor


def main():
    # Options for python
    description = 'estimate joint feature of source and target speakers'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-m', '--multicore', type=int, default=1,
                        help='# of cores for multi-processing')
    parser.add_argument('org', type=str,
                        help='original speaker label')
    parser.add_argument('tar', type=str,
                        help='target speaker label')
    parser.add_argument('pair_ymlf', type=str,
                        help='yml file for the speaker pair')
    args = parser.parse_args()

    # read pair-dependent yml file
    conf = PairYML(args.pair_ymlf)

    # joint feature extraction
    jnt = JointFeatureExtractor(conf, mnum=args.multicore)
    jnt.estimate()

    return

if __name__ == '__main__':
    main()