<div align="justify">

# <div align="center">Perform Changes</div>

Jerry clones the repository and decides to implement basic string operations. So he creates string.c file. After adding the contents, string.c will look like as follows:

```c
#include <stdio.h>

int my_strlen(char *s)
{
   char *p = s;

   while (*p)
      ++p;

   return (p - s);
}

int main(void)
{
   int i;
   char *s[] = 
   {
      "Git tutorials",
      "Tutorials Point"
   };

   for (i = 0; i < 2; ++i)
      
   printf("string lenght of %s = %d\n", s[i], my_strlen(s[i]));

   return 0;
}
```

He compiled and tested his code and everything is working fine. Now, he can safely add these changes to the repository.

Git add operation adds file to the staging area.

```bash
[jerry@CentOS project]$ git status -s
?? string
?? string.c

[jerry@CentOS project]$ git add string.c
```

Git is showing a question mark before file names. Obviously, these files are not a part of Git, and that is why Git does not know what to do with these files. That is why, Git is showing a question mark before file names.

Jerry has added the file to the stash area, git status command will show files present in the staging area.

```bash
[jerry@CentOS project]$ git status -s
A string.c
?? string
```

To commit the changes, he used the git commit command followed by –m option. If we omit –m option. Git will open a text editor where we can write multiline commit message.

```bash
[jerry@CentOS project]$ git commit -m 'Implemented my_strlen function'
```

The above command will produce the following result:

```bash
[master cbe1249] Implemented my_strlen function
1 files changed, 24 insertions(+), 0 deletions(-)
create mode 100644 string.c
```

After commit to view log details, he runs the git log command. It will display the information of all the commits with their commit ID, commit author, commit date and __SHA-1__ hash of commit.

```bash
[jerry@CentOS project]$ git log
```

The above command will produce the following result:

```bash
commit cbe1249b140dad24b2c35b15cc7e26a6f02d2277
Author: Jerry Mouse <jerry@tutorialspoint.com>
Date: Wed Sep 11 08:05:26 2013 +0530

Implemented my_strlen function


commit 19ae20683fc460db7d127cf201a1429523b0e319
Author: Tom Cat <tom@tutorialspoint.com>
Date: Wed Sep 11 07:32:56 2013 +0530

Initial commit
```

</div>
