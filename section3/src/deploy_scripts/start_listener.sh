#!/bin/bash

curl -X POST http://localhost:8042/tools/execute-script --data-binary @/home/workspace/src/deploy_scripts/route_dicoms.lua -v
sudo storescp 106 -v -aet HIPPOAI -od /home/workspace/out/study_root/ --sort-on-study-uid st