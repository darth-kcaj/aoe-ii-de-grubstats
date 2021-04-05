import os
from mgz.summary import Summary ##fyi - there is a change in python 3.9.2+ that breaks this module



###### muckaround ######

fp_to_test_replay = "MP Replay v101.101.46295.0 @2021.04.04 134216 (6).aoe2record"


#https://github.com/happyleavesaoc/aoc-mgz
with open(fp_to_test_replay, 'rb') as data:
       s = Summary(data)
    
    # eof = os.fstat(data.fileno()).st_size
    # header.parse_stream(data)
    # body.meta.parse_stream(data)
    # while data.tell() < eof:
    #     body.operation.parse_stream(data)




print("")