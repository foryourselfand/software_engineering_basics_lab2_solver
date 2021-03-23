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
svn rm ./* --force
cp -r $COMMITS/commit0/* .
echo "r0" > temporary_file
svn add ./* --force
svn commit -m "commit0" --username "red"

#r1
svn copy $REMOTE_URL/trunk $REMOTE_URL/branches/br_1 -m "Add br_1" --username "blue"
svn switch $REMOTE_URL/br_1
svn rm ./* --force
cp -r $COMMITS/commit1/* .
echo "r1" > temporary_file
svn add ./* --force
svn commit -m "commit1" --username "blue"

#r2
svn rm ./* --force
cp -r $COMMITS/commit2/* .
echo "r2" > temporary_file
svn add ./* --force
svn commit -m "commit2" --username "blue"

#r3
svn rm ./* --force
cp -r $COMMITS/commit3/* .
echo "r3" > temporary_file
svn add ./* --force
svn commit -m "commit3" --username "blue"

#r4
svn rm ./* --force
cp -r $COMMITS/commit4/* .
echo "r4" > temporary_file
svn add ./* --force
svn commit -m "commit4" --username "blue"

#r5
svn copy $REMOTE_URL/trunk $REMOTE_URL/branches/br_2 -m "Add br_2" --username "red"
svn switch $REMOTE_URL/br_2
svn rm ./* --force
cp -r $COMMITS/commit5/* .
echo "r5" > temporary_file
svn add ./* --force
svn commit -m "commit5" --username "red"

#r6
svn rm ./* --force
cp -r $COMMITS/commit6/* .
echo "r6" > temporary_file
svn add ./* --force
svn commit -m "commit6" --username "red"

#r7
svn switch $REMOTE_URL/trunk
svn rm ./* --force
cp -r $COMMITS/commit7/* .
echo "r7" > temporary_file
svn add ./* --force
svn commit -m "commit7" --username "red"

#r8
svn rm ./* --force
cp -r $COMMITS/commit8/* .
echo "r8" > temporary_file
svn add ./* --force
svn commit -m "commit8" --username "red"

#r9
svn switch $REMOTE_URL/br_2
svn rm ./* --force
cp -r $COMMITS/commit9/* .
echo "r9" > temporary_file
svn add ./* --force
svn commit -m "commit9" --username "red"

#r10
svn switch $REMOTE_URL/trunk
svn rm ./* --force
cp -r $COMMITS/commit10/* .
echo "r10" > temporary_file
svn add ./* --force
svn commit -m "commit10" --username "red"

#r11
svn switch $REMOTE_URL/br_2
svn rm ./* --force
cp -r $COMMITS/commit11/* .
echo "r11" > temporary_file
svn add ./* --force
svn commit -m "commit11" --username "red"

#r12
svn switch $REMOTE_URL/br_1
svn merge $REMOTE_URL/branches/br_2
svn rm ./* --force
cp -r $COMMITS/commit12/* .
echo "r12" > temporary_file
svn resolve . -R --accept mine-full
svn add ./* --force
svn commit -m "commit12" --username "blue"

#r13
svn rm ./* --force
cp -r $COMMITS/commit13/* .
echo "r13" > temporary_file
svn add ./* --force
svn commit -m "commit13" --username "blue"

#r14
svn switch $REMOTE_URL/trunk
svn merge $REMOTE_URL/branches/br_1
svn rm ./* --force
cp -r $COMMITS/commit14/* .
echo "r14" > temporary_file
svn resolve . -R --accept mine-full
svn add ./* --force
svn commit -m "commit14" --username "red"

