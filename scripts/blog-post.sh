#!/bin/bash

#### Set Python
PYTHON="$(which python3)"
# 

#### Set Files
PYTHON_FILE='./scripts/parsing.py'
COMMIT_FILE='./scripts/commit.sh'
#

#### Execute Python
"${PYTHON}" "${PYTHON_FILE}" 1>/dev/null && echo -e "Parsing Done\n"
#

#### Output save  ./line
SAVE_F='./line'
exec 3>> "${SAVE_F}"

echo -e "\n\n<!-- Blog-Post -->\n" >&3

#while IFS=','

while IFS=',' read text dated
do 
    formattedDate="$(LANG=en_US date '+%b %-d, %Y' -d ${dated})"
    echo "- ${text} ${formattedDate}" >&3
done < csv/parsing.csv

echo -e "\n<!-- Blog-Post End -->" >&3
#

#### Modified Time badge
D="$(date '+%Y/%m/%d_%H:%M')"
TIME_BADGE_URL="<img src=\"https://img.shields.io/badge/Last%20Modified-${D}-%23121212?style=flat\">"
echo -e "\n\n${TIME_BADGE_URL}" >&3
#

#### ADD README.md
cat ./OLD-README.md > ./README.md
cat "${SAVE_F}" >> README.md
#

#### line 파일 삭제
rm -rf "${SAVE_F}"
#