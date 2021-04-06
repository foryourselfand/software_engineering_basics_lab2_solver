#!/bin/bash

#init
cd ~/opi2
rm -rf gitRepo
mkdir gitRepo
cd gitRepo
git init

#r0
git config --local user.name red
git config --local user.email red@gmail.com
git checkout -b br_0
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit0/* .
git add .
git commit -m "r0"

#r1
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit1/* .
git add "d8j9nIRA2h.GUO" "mTh3ufkcBf.X5H"
git commit -m "r1"

#r2
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout -b br_1
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit2/* .
git commit -m "r2"

#r3
git checkout -b br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit3/* .
git commit --allow-empty -m "r3"

#r4
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit4/* .
git commit -m "r4"

#r5
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_1
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit5/* .
git add "d8j9nIRA2h.GUO" "mTh3ufkcBf.X5H"
git commit -m "r5"

#r6
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit6/* .
git commit --allow-empty -m "r6"

#r7
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit7/* .
git commit -m "r7"

#r8
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit8/* .
git commit -m "r8"

#r9
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit9/* .
git add "*"
git commit -m "r9"

#r10
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_1
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit10/* .
git commit -m "r10"

#r11
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
git merge br_1 --no-commit
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit11/* .
git checkout --ours -- ./*
git commit -m "r11"

#r12
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit12/* .
git commit -m "r12"

#r13
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
git merge br_2 --no-commit
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit13/* .
git checkout --ours -- ./*
git commit -m "r13"

#r14
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit14/* .
git add "kNJYHJdeC0.OEV"
git commit -m "r14"

