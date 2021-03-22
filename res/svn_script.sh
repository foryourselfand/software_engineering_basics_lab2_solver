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
svn import $COMMITS/commit0 $REMOTE_URL/trunk -m 'commit0' --username 'first' #добавление в удаленный репозиторий начального коммита

#init local
svn checkout $REMOTE_URL/trunk working_copy
cd working_copy

#branch1
svn mkdir $REMOTE_URL/branches -m 'Add branches' --username 'first'                         #создание ветки
svn copy $REMOTE_URL/trunk $REMOTE_URL/branches/branch1 -m 'Add branch1' --username 'first' #добавление в ветку начальной ревизии

#r1
svn switch $REMOTE_URL/branches/branch1
cp $COMMITS/commit1/\* .
svn add \*
svn commit -m 'commit1' --username 'first'

#r2
svn switch $REMOTE_URL/trunk
cp $COMMITS/commit2/\* .
svn add \*
svn commit -m 'commit2' --username 'first'

#branch2
svn copy $REMOTE_URL/trunk $REMOTE_URL/branches/branch2 -m 'Add branch2' --username 'first'

#r3
svn switch $REMOTE_URL/branches/branch2
svn rm *
cp -r $COMMITS/commit3/* .
svn add *
svn commit -m 'commit3' --username 'second'

#r4
svn switch $REMOTE_URL/branches/branch1
svn rm *
cp -r $COMMITS/commit4/* .
svn add *
svn commit -m 'commit4' --username 'first'

#r5
svn switch $REMOTE_URL/trunk
svn rm *
cp -r $COMMITS/commit5/* .
svn add *
svn commit -m 'commit5' --username 'first'

#r6
svn rm *
cp -r $COMMITS/commit6/* .
svn add *
svn commit -m 'commit6' --username 'first'

#r7
svn switch $REMOTE_URL/branches/branch1
svn rm *
cp -r $COMMITS/commit7/* .
svn add *
svn commit -m 'commit7' --username 'first'

#r8
svn switch $REMOTE_URL/branches/branch2
svn rm *
cp -r $COMMITS/commit8/* .
svn add *
svn commit -m 'commit8' --username 'second'

#r9
svn switch $REMOTE_URL/trunk
svn merge --ignore-ancestry -r 5:12 $REMOTE_URL/branches/branch2
cp -r $COMMITS/commit9/* .
svn rm \*
svn commit -m 'commit9' --username 'first'

#r10
cp -r $COMMITS/commit10/* .
svn commit -m 'commit10' --username 'first'

#r11
cp -r $COMMITS/commit11/* .
svn add ngQwbZDrTr.Ewt
svn commit -m 'commit11' --username 'first'

#r12
svn switch $REMOTE_URL/branches/branch1
svn rm *
cp -r $COMMITS/commit12/* .
svn add *
svn commit -m 'commit12' --username 'first'

#r13
svn switch $REMOTE_URL/trunk
svn merge --ignore-ancestry -r 3:16 $REMOTE_URL/branches/branch1
svn rm ngQwbZDrTr.Ewt
cp $COMMITS/commit13/mEEwtngQwb.Upj .
svn add mEEwtngQwb.Upj
svn commit -m 'commit13' --username 'first'

#r14
cp -r $COMMITS/commit14/* .
svn add 3AbUpjmEEw.9wN
svn rm mEEwtngQwb.Upj
svn rm \*
svn commit -m 'commit14' --username 'first'
