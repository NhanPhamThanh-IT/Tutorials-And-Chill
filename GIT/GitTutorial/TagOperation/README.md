<div align="justify">

# <div align="center">Tag Operation</div>

Tag operation allows giving meaningful names to a specific version in the repository. Suppose Tom and Jerry decide to tag their project code so that they can later access it easily.

## Create Tags

Let us tag the current HEAD by using the __git tag__ command. Tom provides a tag name with -a option and provides a tag message with –m option.

```bash
tom@CentOS project]$ pwd
/home/tom/top_repo/project

[tom@CentOS project]$ git tag -a 'Release_1_0' -m 'Tagged basic string operation code' HEAD
```

If you want to tag a particular commit, then use the appropriate COMMIT ID instead of the HEAD pointer. Tom uses the following command to push the tag into the remote repository.

```bash
[tom@CentOS project]$ git push origin tag Release_1_0
```

The above command will produce the following result:

```bash
Counting objects: 1, done.
Writing objects: 100% (1/1), 183 bytes, done.
Total 1 (delta 0), reused 0 (delta 0)
To gituser@git.server.com:project.git
* [new tag]
Release_1_0 −> Release_1_0
```

## View Tags

Tom created tags. Now, Jerry can view all the available tags by using the Git tag command with –l option.

```bash
[jerry@CentOS src]$ pwd
/home/jerry/jerry_repo/project/src

[jerry@CentOS src]$ git pull
remote: Counting objects: 1, done.
remote: Total 1 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (1/1), done.
From git.server.com:project
* [new tag]
Release_1_0 −> Release_1_0
Current branch master is up to date.

[jerry@CentOS src]$ git tag -l
Release_1_0
```

Jerry uses the Git show command followed by its tag name to view more details about tag.

```bash
[jerry@CentOS src]$ git show Release_1_0
```

The above command will produce the following result:

```bash
tag Release_1_0
Tagger: Tom Cat <tom@tutorialspoint.com>
Date: Wed Sep 11 13:45:54 2013 +0530

Tagged basic string operation code


commit 577647211ed44fe2ae479427a0668a4f12ed71a1
Author: Tom Cat <tom@tutorialspoint.com>
Date: Wed Sep 11 10:21:20 2013 +0530

Removed executable binary

diff --git a/src/string_operations b/src/string_operations
deleted file mode 100755
index 654004b..0000000
Binary files a/src/string_operations and /dev/null differ
```

## Delete Tags

Tom uses the following command to delete tags from the local as well as the remote repository.

```bash
[tom@CentOS project]$ git tag
Release_1_0

[tom@CentOS project]$ git tag -d Release_1_0
Deleted tag 'Release_1_0' (was 0f81ff4)
# Remove tag from remote repository.

[tom@CentOS project]$ git push origin :Release_1_0
To gituser@git.server.com:project.git
- [deleted]
Release_1_0
```

</div>
