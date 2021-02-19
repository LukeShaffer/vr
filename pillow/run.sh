#!/bin/sh

export RUN_FUZZER_MODE=interactive;export FUZZING_ENGINE=libfuzzer; export SANITIZER=address; export OUT=/shared/591/syntax/vr/pillow; run_fuzzer fuzz_pillow

echo "Sleeping"
echo "0" > $HOME/flag
while true
do
        val=$(cat $HOME/flag)
        if [ $val -eq 1 ]
        then
                exit
        fi
        sleep 5m
done
