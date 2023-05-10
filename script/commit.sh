#!/bin/bash
git=$(which git)
${git} pull origin main 1>/dev/null 2>&1
if [[ $(git status --porcelain) ]]
then
	${git} config user.name ${GITUSER}
	${git} config user.email ${GITEMAIL} 
	${git} add -A
	${git} commit -m "Update README"
	${git} push -u origin main
fi