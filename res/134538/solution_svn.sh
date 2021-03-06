#!/bin/bash

#init
cd ~/opi2
rm -rf repo_svn
mkdir repo_svn
cd repo_svn

#init remote
svnadmin create origin
REMOTE_URL="file://$(pwd -P)/origin"
COMMITS=~/opi2/commits
svn mkdir -m "project structure" $REMOTE_URL/trunk $REMOTE_URL/branches --username "red"

#init local
svn checkout $REMOTE_URL/trunk working_copy
cd working_copy

#r0
cp -r $COMMITS/commit0/* .
svn add --force *
svn commit -m "commit0" --username "red"

#r1
svn rm --force *
cp -r $COMMITS/commit1/* .
svn add --force *
svn commit -m "commit1" --username "red"

#r2
svn copy $REMOTE_URL/trunk $REMOTE_URL/branches/br_1 -m "Add br_1" --username "blue"
svn switch $REMOTE_URL/branches/br_1
svn rm --force *
cp -r $COMMITS/commit2/* .
svn add --force *
svn commit -m "commit2" --username "blue"

#r3
svn copy $REMOTE_URL/branches/br_1 $REMOTE_URL/branches/br_2 -m "Add br_2" --username "blue"
svn switch $REMOTE_URL/branches/br_2
svn rm --force *
cp -r $COMMITS/commit3/* .
echo "r3" > temporary_file
svn add --force *
svn commit -m "commit3" --username "blue"

#r4
svn switch $REMOTE_URL/trunk
svn rm --force *
cp -r $COMMITS/commit4/* .
svn add --force *
svn commit -m "commit4" --username "red"

#r5
svn switch $REMOTE_URL/branches/br_1
svn rm --force *
cp -r $COMMITS/commit5/* .
svn add --force *
svn commit -m "commit5" --username "blue"

#r6
svn switch $REMOTE_URL/branches/br_2
svn rm --force *
cp -r $COMMITS/commit6/* .
echo "r6" > temporary_file
svn add --force *
svn commit -m "commit6" --username "blue"

#r7
svn switch $REMOTE_URL/trunk
svn rm --force *
cp -r $COMMITS/commit7/* .
svn add --force *
svn commit -m "commit7" --username "red"

#r8
svn switch $REMOTE_URL/branches/br_2
svn rm --force *
cp -r $COMMITS/commit8/* .
svn add --force *
svn commit -m "commit8" --username "blue"

#r9
svn switch $REMOTE_URL/trunk
svn rm --force *
cp -r $COMMITS/commit9/* .
svn add --force *
svn commit -m "commit9" --username "red"

#r10
svn switch $REMOTE_URL/branches/br_1
svn rm --force *
cp -r $COMMITS/commit10/* .
svn add --force *
svn commit -m "commit10" --username "blue"

#r11
svn switch $REMOTE_URL/trunk
svn merge $REMOTE_URL/branches/br_1
svn resolve . -R --accept=working
svn rm --force *
cp -r $COMMITS/commit11/* .
svn add --force *
svn commit -m "commit11" --username "red"

#r12
svn switch $REMOTE_URL/branches/br_2
svn rm --force *
cp -r $COMMITS/commit12/* .
svn add --force *
svn commit -m "commit12" --username "blue"

#r13
svn switch $REMOTE_URL/trunk
svn merge $REMOTE_URL/branches/br_2
svn resolve . -R --accept=working
svn rm --force *
cp -r $COMMITS/commit13/* .
svn add --force *
svn commit -m "commit13" --username "red"

#r14
svn rm --force *
cp -r $COMMITS/commit14/* .
svn add --force *
svn commit -m "commit14" --username "red"

