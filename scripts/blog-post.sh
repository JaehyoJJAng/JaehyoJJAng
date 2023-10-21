#!/bin/bash

#### Set Python
PYTHON="$(which python3)"
#

#### Set files
PYTHON_FILE='./scripts/parsing.py'
COMMIT_FILE='./scripts/commit.sh'
#

#### Execution Python Script
"${PYTHON}" "${PYTHON_FILE}" 1>/dev/null && echo -e "Parsing Done\n"
#

#### Output save ./line
SAVE_F='./line'
exec 3>> "${SAVE_F}"

echo -e "\n\n<!-- Blog-Post -->\n" >&3

while IFS=',' read text dated
do
    dated=$(echo "${dated}" | sed 's/"//g')
    echo "- ${text} ${dated}" >&3
done < ./csv/parsing.csv

echo -e "\n<!-- Blog-Post End -->" >&3
# 

#### Modified Time badge
D="$(date '+%Y/%m/%d_%H:%M')"
TIME_BADGE_URL="<img src=\"https://img.shields.io/badge/Last%20Modified-${D}-%23121212?style=flat\">"
echo -e "\n\n${TIME_BADGE_URL}" >&3
#

#### Add README.md
cat ./OLD-README.md > ./README.md
cat "${SAVE_F}" >> ./README.md
#

#### Delete line
rm -rf "${SAVE_F}"
echo -e "Deleted ${SAVE_F}"
#
