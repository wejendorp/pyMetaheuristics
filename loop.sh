#!/bin/bash
for I in 1 2 3 4 5 .. 100
    do
        python ./Metaheuristic.py -v -f tcp.points -s tcp -a ascent -d 0
    done
