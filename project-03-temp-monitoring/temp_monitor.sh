#!/bin/bash
for i in $(seq 1 60);do
 echo "$(date +%T), $(vcgencmd measure_temp)"
 sleep 1
done | tee temp_log.csv
