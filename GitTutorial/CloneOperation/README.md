<div align="justify">

# <div align="center">Clone Operation</div>

We have a bare repository on the Git server and Tom also pushed his first version. Now, Jerry can view his changes. The Clone operation creates an instance of the remote repository.

Jerry creates a new directory in his home directory and performs the clone operation.

```bash
[jerry@CentOS ~]$ mkdir jerry_repo

[jerry@CentOS ~]$ cd jerry_repo/

[jerry@CentOS jerry_repo]$ git clone gituser@git.server.com:project.git
```

The above command will produce the following result.

```bash
Initialized empty Git repository in /home/jerry/jerry_repo/project/.git/
remote: Counting objects: 3, done.
Receiving objects: 100% (3/3), 241 bytes, done.
remote: Total 3 (delta 0), reused 0 (delta 0)
```

Jerry changes the directory to new local repository and lists its directory contents.

```bash
[jerry@CentOS jerry_repo]$ cd project/

[jerry@CentOS jerry_repo]$ ls
README
```

</div>
