#!/bin/bash
if [[ $(git status --porcelain) ]]
then
    git config --global user.name "${USER_NAME}"
    git config --global user.email "${USER_EMAIL}"
    git remote set-url origin https://"${USER_NAME}":"${TOKEN}"@github.com/"${REPOSITORY}"
    git add -A
    git commit -m "${MESSAGE}"
    git push -u origin main
fi