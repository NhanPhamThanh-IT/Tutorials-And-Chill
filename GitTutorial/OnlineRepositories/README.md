<div align="justify">

# <div align="center">Online Repositories</div>

__GitHub__ is a web-based hosting service for software development projects that uses the Git revision control system. It also has their standard GUI application available for download (Windows, Mac, GNU/ Linux) directly from the service's website. But in this session, we will see only CLI part.

## Create GitHub Repository

Go to github.com. If you already have the __GitHub__ account, then login using that account or create a new one. Follow the steps from github.com website to create a new repository.

## Push Operation

Tom decides to use the __GitHub__ server. To start a new project, he creates a new directory and one file inside that.

```bash
[tom@CentOS]$ mkdir github_repo

[tom@CentOS]$ cd github_repo/

[tom@CentOS]$ vi hello.c

[tom@CentOS]$ make hello
cc hello.c -o hello

[tom@CentOS]$ ./hello
```

The above command will produce the following result:

```
Hello, World !!!
```

After verifying his code, he initializes the directory with the git init command and commits his changes locally.

```bash
[tom@CentOS]$ git init
Initialized empty Git repository in /home/tom/github_repo/.git/

[tom@CentOS]$ git status -s
?? hello
?? hello.c

[tom@CentOS]$ git add hello.c

[tom@CentOS]$ git status -s
A hello.c
?? hello

[tom@CentOS]$ git commit -m 'Initial commit'
```

After that, he adds the __GitHub__ repository URL as a remote origin and pushes his changes to the remote repository.

```bash
[tom@CentOS]$ git remote add origin https://github.com/kangralkar/testing_repo.git

[tom@CentOS]$ git push -u origin master
```

Push operation will ask for __GitHub__ user name and password. After successful authentication, the operation will succeed.

The above command will produce the following result:

```bash
Username for 'https://github.com': kangralkar
Password for 'https://kangralkar@github.com': 
Counting objects: 3, done.
Writing objects: 100% (3/3), 214 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/kangralkar/test_repo.git
 * [new branch]      master −> master
 Branch master set up to track remote branch master from origin.
```

From now, Tom can push any changes to the __GitHub__ repository. He can use all the commands discussed in this chapter with the __GitHub__ repository.

## Pull Operation

Tom successfully pushed all his changes to the __GitHub__ repository. Now, other developers can view these changes by performing clone operation or updating their local repository.

Jerry creates a new directory in his home directory and clones the __GitHub__ repository by using the git clone command.

```bash
[jerry@CentOS]$ pwd
/home/jerry

[jerry@CentOS]$ mkdir jerry_repo

[jerry@CentOS]$ git clone https://github.com/kangralkar/test_repo.git
```

The above command produces the following result:

```
Cloning into 'test_repo'...
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 3 (delta 0)
Unpacking objects: 100% (3/3), done.
```

He verifies the directory contents by executing the ls command.

```bash
[jerry@CentOS]$ ls
test_repo

[jerry@CentOS]$ ls test_repo/
hello.c
```

</div>
