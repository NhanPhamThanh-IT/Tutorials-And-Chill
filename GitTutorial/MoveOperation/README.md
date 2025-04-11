<div align="justify">

# <div align="center">Move Operation</div>

As the name suggests, the move operation moves a directory or a file from one location to another. Tom decides to move the source code into __src__ directory. The modified directory structure will appear as follows −

```bash
[tom@CentOS project]$ pwd
/home/tom/project

[tom@CentOS project]$ ls
README string string.c

[tom@CentOS project]$ mkdir src

[tom@CentOS project]$ git mv string.c src/

[tom@CentOS project]$ git status -s
R string.c −> src/string.c
?? string
```

To make these changes permanent, we have to push the modified directory structure to the remote repository so that other developers can see this.

```bash
[tom@CentOS project]$ git commit -m "Modified directory structure"

[master 7d9ea97] Modified directory structure
1 files changed, 0 insertions(+), 0 deletions(-)
rename string.c => src/string.c (100%)

[tom@CentOS project]$ git push origin master
Counting objects: 4, done.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 320 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To gituser@git.server.com:project.git
e86f062..7d9ea97 master −> master
```

In Jerry’s local repository, before the pull operation, it will show the old directory structure.

```bash
[jerry@CentOS project]$ pwd
/home/jerry/jerry_repo/project

[jerry@CentOS project]$ ls
README string string.c
```

But after the pull operation, the directory structure will get updated. Now, Jerry can see the __src__ directory and the file present inside that directory.

```bash
[jerry@CentOS project]$ git pull
remote: Counting objects: 4, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
From git.server.com:project
e86f062..7d9ea97 master −> origin/master
First, rewinding head to replay your work on top of it...
Fast-forwarded master to 7d9ea97683da90bcdb87c28ec9b4f64160673c8a.

[jerry@CentOS project]$ ls
README src string

[jerry@CentOS project]$ ls src/
string.c
```

</div>
