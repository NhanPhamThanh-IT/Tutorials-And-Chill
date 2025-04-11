<div align="justify">

# <div align="center">Different Platforms</div>

GNU/Linux and Mac OS uses __line-feed (LF)__, or new line as line ending character, while Windows uses __line-feed and carriage-return (LFCR)__ combination to represent the line-ending character.

To avoid unnecessary commits because of these line-ending differences, we have to configure the Git client to write the same line ending to the Git repository.

For Windows system, we can configure the Git client to convert line endings to __CRLF__ format while checking out, and convert them back to __LF__ format during the commit operation. The following settings will do the needful.

```bash
[tom@CentOS project]$ git config --global core.autocrlf true
```

For GNU/Linux or Mac OS, we can configure the Git client to convert line endings from __CRLF__ to __LF__ while performing the checkout operation.

```bash
[tom@CentOS project]$ git config --global core.autocrlf input
```

</div>
