#!/bin/bash

# Move to WorkingDirectory
cd /home/ncloud/git/JaehyoJJAng/script/

########### File List
PYTHON3=$(which python3)
PYTHON_FILE='/home/ncloud/git/JaehyoJJAng/script/parsing.py'
COMMIT_FILE='/home/ncloud/git/JaehyoJJAng/script/commit.sh'
#

######## Execute Python 
${PYTHON3} ${PYTHON_FILE} 1>/dev/null && echo -e "Parsing Done\n" || exit 1
#

######## Output Save ./line
SAVE_F='./line'
exec 3>> ${SAVE_F}
echo -e "\n\n<!-- Blog-Post -->\n" >&3
while IFS=',' read text dated 
do
	formattedDate="$(LANG=en_US date '+%b %-d, %Y' -d "${dated}")"
	echo "-  ${text} ${formattedDate}" >&3
done < ../csv/parsing.csv

echo -e "\n<!-- Blog-Post -->" >&3
#

########## ModiFied 
#
D=$(date "+%Y/%m/%d_%H:%M")
URL="<img src=\"https://img.shields.io/badge/Last%20Modified-${D}-%23121212?style=flat\">"
echo -e "\n\n${URL}" >&3

######### Add README.md
/usr/bin/cat '../OLD-README.md' > ../README.md
/usr/bin/cat ${SAVE_F} >> ../README.md
#

######### line 파일 삭제
/usr/bin/rm -rf ${SAVE_F}
#

######### Git Commit
${COMMIT_FILE}
#
