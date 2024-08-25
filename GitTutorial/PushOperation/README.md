<div align="justify">

# <div align="center">Push Operation</div>

Jerry modified his last commit by using the amend operation and he is ready to push the changes. The Push operation stores data permanently to the Git repository. After a successful push operation, other developers can see Jerry’s changes.

He executes the git log command to view the commit details.

```bash
[jerry@CentOS project]$ git log
```

The above command will produce the following result:

```bash
commit d1e19d316224cddc437e3ed34ec3c931ad803958
Author: Jerry Mouse <jerry@tutorialspoint.com>
Date: Wed Sep 11 08:05:26 2013 +0530

Changed return type of my_strlen to size_t
```

Before push operation, he wants to review his changes, so he uses the __git show__ command to review his changes.

```bash
[jerry@CentOS project]$ git show d1e19d316224cddc437e3ed34ec3c931ad803958
```

The above command will produce the following result:

```bash
commit d1e19d316224cddc437e3ed34ec3c931ad803958
Author: Jerry Mouse <jerry@tutorialspoint.com>
Date: Wed Sep 11 08:05:26 2013 +0530

Changed return type of my_strlen to size_t

diff --git a/string.c b/string.c
new file mode 100644
index 0000000..7da2992
--- /dev/null
+++ b/string.c
@@ -0,0 +1,24 @@
+#include <stdio.h>
+
+size_t my_strlen(char *s)
+
{
   +
   char *p = s;
   +
   +
   while (*p)
   + ++p;
   + return (p -s );
   +
}
+
+int main(void)
+
{
   + int i;
   + char *s[] = 
   {
      + "Git tutorials",
      + "Tutorials Point"
      +
   };
   +
   +
   +
   for (i = 0; i < 2; ++i)
   printf("string lenght of %s = %lu\n", s[i], my_strlen(s[i]));
   +
   +
   return 0;
   +
}
```

Jerry is happy with his changes and he is ready to push his changes.

```bash
[jerry@CentOS project]$ git push origin master
```

The above command will produce the following result:

```bash
Counting objects: 4, done.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 517 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To gituser@git.server.com:project.git
19ae206..d1e19d3 master −> master
```

Jerry’s changes have been successfully pushed to the repository; now other developers can view his changes by performing clone or update operation.

</div>
