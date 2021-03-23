#!/bin/bash

#init
cd ~/opi2
rm -rf svnRepo
mkdir svnRepo
cd svnRepo

#init remote
svnadmin create origin
REMOTE_URL="file://$(pwd -P)/origin"
COMMITS=~/opi2/commits
svn mkdir -m "project structure" $REMOTE_URL/trunk $REMOTE_URL/branches

#init local
svn checkout $REMOTE_URL/trunk working_copy
cd working_copy

#r0
svn switch $REMOTE_URL/trunk
svn rm ./*
cp $COMMITS/commit0/* .
svn add ./*
svn commit -m "commit0" --username "red"

#r1
svn copy $REMOTE_URL/trunk $REMOTE_URL/branches/br_2 -m "Add br_2" --username "red"
svn switch $REMOTE_URL/branches/br_2
svn rm ./*
cp $COMMITS/commit1/* .
svn add ./*
svn commit -m "commit1" --username "red"

#r2
svn switch $REMOTE_URL/trunk
svn rm ./*
cp $COMMITS/commit2/* .
svn add ./*
svn commit -m "commit2" --username "red"

#r3
svn copy $REMOTE_URL/trunk $REMOTE_URL/branches/br_1 -m "Add br_1" --username "blue"
svn switch $REMOTE_URL/branches/br_1
svn rm ./*
cp -r $COMMITS/commit3/* .
svn add ./*
svn commit -m "commit3" --username "blue"

#r4
svn switch $REMOTE_URL/branches/br_2
svn rm ./*
cp -r $COMMITS/commit4/* .
svn add ./*
svn commit -m "commit4" --username "red"

#r5
svn switch $REMOTE_URL/trunk
svn rm ./*
cp -r $COMMITS/commit5/* .
svn add ./*
svn commit -m "commit5" --username "red"

#r6
svn rm ./*
cp -r $COMMITS/commit6/* .
svn add ./*
svn commit -m "commit6" --username "red"

#r7
svn switch $REMOTE_URL/branches/br_2
svn rm ./*
cp -r $COMMITS/commit7/* .
svn add ./*
svn commit -m "commit7" --username "red"

#r8
svn switch $REMOTE_URL/branches/br_1
svn rm ./*
cp -r $COMMITS/commit8/* .
svn add ./*
svn commit -m "commit8" --username "blue"

#r9
svn switch $REMOTE_URL/trunk
svn merge $REMOTE_URL/branches/br_1
svn rm ./* --force
cp -r $COMMITS/commit9/* .
svn add ./*
svn commit -m "commit9" --username "red"

#r10
cp -r $COMMITS/commit10/* .
svn commit -m "commit10" --username "red"

#r11
cp -r $COMMITS/commit11/* .
svn add ngQwbZDrTr.Ewt
svn commit -m "commit11" --username "red"

#r12
svn switch $REMOTE_URL/branches/br_2
svn rm *
cp -r $COMMITS/commit12/* .
svn add *
svn commit -m "commit12" --username "red"

#r13
svn switch $REMOTE_URL/trunk
svn merge --ignore-ancestry -r 3:16 $REMOTE_URL/branches/br_2
svn rm ngQwbZDrTr.Ewt
cp $COMMITS/commit13/mEEwtngQwb.Upj .
svn add mEEwtngQwb.Upj
svn commit -m "commit13" --username "red"

#r14
cp -r $COMMITS/commit14/* .
svn add 3AbUpjmEEw.9wN
svn rm mEEwtngQwb.Upj
svn rm \*
svn commit -m "commit14" --username "red"
