<div align="justify">

# <div align="center">Patch Operation</div>

Patch is a text file, whose contents are similar to Git diff, but along with code, it also has metadata about commits; e.g., commit ID, date, commit message, etc. We can create a patch from commits and other people can apply them to their repository.

Jerry implements the strcat function for his project. Jerry can create a path of his code and send it to Tom. Then, he can apply the received patch to his code.

Jerry uses the Git __format-patch__ command to create a patch for the latest commit. If you want to create a patch for a specific commit, then use __COMMIT_ID__ with the format-patch command.

```bash
[jerry@CentOS project]$ pwd
/home/jerry/jerry_repo/project/src

[jerry@CentOS src]$ git status -s
M string_operations.c
?? string_operations

[jerry@CentOS src]$ git add string_operations.c

[jerry@CentOS src]$ git commit -m "Added my_strcat function"

[master b4c7f09] Added my_strcat function
1 files changed, 13 insertions(+), 0 deletions(-)

[jerry@CentOS src]$ git format-patch -1
0001-Added-my_strcat-function.patch
```

The above command creates __.patch__ files inside the current working directory. Tom can use this patch to modify his files. Git provides two commands to apply patches __git am__ and __git apply__, respectively. __Git apply__ modifies the local files without creating commit, while __git am__ modifies the file and creates commit as well.

To apply patch and create commit, use the following command:

```bash
[tom@CentOS src]$ pwd
/home/tom/top_repo/project/src

[tom@CentOS src]$ git diff

[tom@CentOS src]$ git status –s

[tom@CentOS src]$ git apply 0001-Added-my_strcat-function.patch

[tom@CentOS src]$ git status -s
M string_operations.c
?? 0001-Added-my_strcat-function.patch
```

The patch gets applied successfully, now we can view the modifications by using the __git diff__ command.

```bash
[tom@CentOS src]$ git diff
```

The above command will produce the following result:

```bash
diff --git a/src/string_operations.c b/src/string_operations.c
index 8ab7f42..f282fcf 100644
--- a/src/string_operations.c
+++ b/src/string_operations.c
@@ -1,5 +1,16 @@
#include <stdio.h>
+char *my_strcat(char *t, char *s)
diff --git a/src/string_operations.c b/src/string_operations.c
index 8ab7f42..f282fcf 100644
--- a/src/string_operations.c
+++ b/src/string_operations.c
@@ -1,5 +1,16 @@
#include <stdio.h>
+char *my_strcat(char *t, char *s)
+
{
   +
   char *p = t;
   +
   +
   +
   while (*p)
   ++p;
   +
   while (*p++ = *s++)
   + ;
   + return t;
   +
}
+
size_t my_strlen(const char *s)
{
   const char *p = s;
   @@ -23,6 +34,7 @@ int main(void)
{
```

</div>
