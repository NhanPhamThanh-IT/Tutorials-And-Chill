<div align="justify">

# <div align="center">Review Changes</div>  

After viewing the commit details, Jerry realizes that the string length cannot be negative, that’s why he decides to change the return type of my_strlen function.

Jerry uses the __git log__ command to view log details.

```bash
[jerry@CentOS project]$ git log
```

The above command will produce the following result.

```bash
commit cbe1249b140dad24b2c35b15cc7e26a6f02d2277
Author: Jerry Mouse <jerry@tutorialspoint.com>
Date: Wed Sep 11 08:05:26 2013 +0530

Implemented my_strlen function
```

Jerry uses the __git show__ command to view the commit details. The git show command takes __SHA-1__ commit ID as a parameter.

```bash
[jerry@CentOS project]$ git show cbe1249b140dad24b2c35b15cc7e26a6f02d2277
```

The above command will produce the following result:

```bash
commit cbe1249b140dad24b2c35b15cc7e26a6f02d2277
Author: Jerry Mouse <jerry@tutorialspoint.com>
Date: Wed Sep 11 08:05:26 2013 +0530

Implemented my_strlen function


diff --git a/string.c b/string.c
new file mode 100644
index 0000000..187afb9
--- /dev/null
+++ b/string.c
@@ -0,0 +1,24 @@
+#include <stdio.h>
+
+int my_strlen(char *s)
+{
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
```

He changes the return type of the function from int to size_t. After testing the code, he reviews his changes by running the __git diff__ command.

```bash
[jerry@CentOS project]$ git diff
```

The above command will produce the following result:

```bash
diff --git a/string.c b/string.c
index 187afb9..7da2992 100644
--- a/string.c
+++ b/string.c
@@ -1,6 +1,6 @@
#include <stdio.h>

-int my_strlen(char *s)
+size_t my_strlen(char *s)
{
   char *p = s;
   @@ -18,7 +18,7 @@ int main(void)
};
for (i = 0; i < 2; ++i)
{
   - printf("string lenght of %s = %d\n", s[i], my_strlen(s[i]));
   + printf("string lenght of %s = %lu\n", s[i], my_strlen(s[i]));
   return 0;
}
```

Git diff shows __'+'__ sign before lines, which are newly added and __'−'__ for deleted lines.

</div>
