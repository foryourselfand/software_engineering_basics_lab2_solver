#!/bin/bash

#init
cd ~opi2
rm -rf gitRepo
mkdir gitRepo
cd gitRepo
git init

#r0
git config --local user.name red
git config --local user.email red@gmail.com
git checkout -b br_0
cp ../commits/commit0/* .
git add .
git commit -m r0

#r1
git checkout -b br_2
ls | grep -v .git | xargs rm -rf
cp ../commits/commit1/* .
git add .
git commit -m r1

#r2
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp ../commits/commit2/* .
git add .
git commit -m r2

#r3
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout -b br_1
ls | grep -v .git | xargs rm -rf
cp ../commits/commit3/* .
git add .
git commit --allow-empty -m r3

#r4
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp ../commits/commit4/* .
git add .
git commit --allow-empty -m r4

#r5
git checkout br_0
ls | grep -v .git | xargs rm -rf
cp ../commits/commit5/* .
git add .
git commit --allow-empty -m r5

#r6
ls | grep -v .git | xargs rm -rf
cp ../commits/commit6/* .
git add .
git commit --allow-empty -m r6

#r7
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp ../commits/commit7/* .
git add .
git commit --allow-empty -m r7

#r8
git config --local user.name blue
git config --local user.email blue@gmail.com
git checkout br_1
ls | grep -v .git | xargs rm -rf
cp ../commits/commit8/* .
git add .
git commit --allow-empty -m r8

#r9
git config --local user.name red
git config --local user.email red@gmail.com
git checkout br_0
git merge br_1 --no-commit
ls | grep -v .git | xargs rm -rf
cp ../commits/commit9/* .
git add .
git rm '*'
git commit -m r9

#r10
ls | grep -v .git | xargs rm -rf
cp ../commits/commit10/* .
git add .
git commit -m r10

#r11
ls | grep -v .git | xargs rm -rf
cp ../commits/commit11/* .
git add .
git commit -m r11

#r12
git checkout br_2
ls | grep -v .git | xargs rm -rf
cp ../commits/commit12/* .
git add .
git commit --allow-empty -m r12

#r13
git checkout br_0
git merge br_2 --no-commit
ls | grep -v .git | xargs rm -rf
cp ../commits/commit13/* .
git rm 'ngQwbZDrTr.Ewt'
git add .
git commit -m r13

#r14
ls | grep -v .git | xargs rm -rf
cp ../commits/commit14/* .
git add -A
git rm '*'
git rm mEEwtngQwb.Upj
git commit -m r14
