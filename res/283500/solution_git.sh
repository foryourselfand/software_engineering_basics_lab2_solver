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
git commit --allow-empty -m "r0"

#r1
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout -b br_1
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit1/* .
git add .
git commit --allow-empty -m "r1"

#r2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit2/* .
git add .
git commit --allow-empty -m "r2"

#r3
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit3/* .
git add .
git commit --allow-empty -m "r3"

#r4
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit4/* .
git add .
git commit --allow-empty -m "r4"

#r5
git config --local user.name red
git config --local user.email red@gmail.com
git checkout -b br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit5/* .
git add .
git commit --allow-empty -m "r5"

#r6
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit6/* .
git add .
git commit --allow-empty -m "r6"

#r7
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit7/* .
git add .
git commit --allow-empty -m "r7"

#r8
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit8/* .
git add .
git commit --allow-empty -m "r8"

#r9
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit9/* .
git add .
git commit --allow-empty -m "r9"

#r10
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit10/* .
git add .
git commit --allow-empty -m "r10"

#r11
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit11/* .
git add .
git commit --allow-empty -m "r11"

#r12
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_1
git merge br_2 --no-commit
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit12/* .
git checkout --ours -- ./*
git add .
git commit --allow-empty -m "r12"

#r13
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit13/* .
git add .
git commit --allow-empty -m "r13"

#r14
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
git merge br_1 --no-commit
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit14/* .
git checkout --ours -- ./*
git add .
git commit --allow-empty -m "r14"

