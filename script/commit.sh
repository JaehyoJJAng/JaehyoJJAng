#!/bin/bash
git=$(which git)
if [[ $(git status --porcelain) ]]
then
	${git} config user.name ${GITUSER}
	${git} config user.email ${GITEMAIL} 
	${git} add -A
	${git} commit -m "Update README"
	${git} push -u origin main
fi
