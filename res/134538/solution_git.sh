#!/bin/bash

#init
cd ~/opi2
rm -rf repo_git
mkdir repo_git
cd repo_git
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
git add .
git commit -m "r1"

#r2
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout -b br_1
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit2/* .
git add .
git commit -m "r2"

#r3
git checkout -b br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit3/* .
git add .
git commit --allow-empty -m "r3"

#r4
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit4/* .
git add .
git commit -m "r4"

#r5
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_1
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit5/* .
git add .
git commit -m "r5"

#r6
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit6/* .
git add .
git commit --allow-empty -m "r6"

#r7
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit7/* .
git add .
git commit -m "r7"

#r8
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit8/* .
git add .
git commit -m "r8"

#r9
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit9/* .
git add .
git commit -m "r9"

#r10
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_1
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit10/* .
git add .
git commit -m "r10"

#r11
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
git merge br_1 --no-commit
git checkout --ours .
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit11/* .
git add .
git commit -m "r11"

#r12
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit12/* .
git add .
git commit -m "r12"

#r13
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
git merge br_2 --no-commit
git checkout --ours .
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit13/* .
git add .
git commit -m "r13"

#r14
ls | grep -v .git | xargs rm -rf
cp -r ../commits/commit14/* .
git add .
git commit -m "r14"

