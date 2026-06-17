#!/usr/bin/env bash

count_wolf_sessions() {
    docker ps --format "{{.Names}}" | grep "Wolf.*_" 2>/dev/null | wc -l
}

num_wolf=$(count_wolf_sessions)

while [ "${num_wolf}" -gt 0 ]; do
    sleep 30
    num_wolf=$(count_wolf_sessions)
done
