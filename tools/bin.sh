#!bin/bash
read -p "Bin: " bin
curl -s https://lookup.binlist.net/$bin > data.json
cat data.json | tr ',' "\n" | tr '"' ' ' | sed 's/{//' | sed 's/}//'
rm data.json
