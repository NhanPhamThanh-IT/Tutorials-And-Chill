# Difference between Static and Dynamic SQL

**Static or Embedded** SQL are SQL statements in an application that do not change at runtime and, therefore, can be hard-coded into the application. 

**Dynamic SQL** is SQL statements that are constructed at runtime; for example, the application may allow users to enter their own queries. 

**Dynamic SQL** is a programming technique that enables you to build SQL statements dynamically at runtime. 

You can create more general purpose, flexible applications by using dynamic SQL because the full text of a SQL statement may be unknown at compilation. 

Static SQL are faster and more efficient while dynamic SQL is less efficient since access plans for dynamic statements are generated at run-time so they must be prepared in the application, and this is something you will never look at in the static SQL, but these are not the only differences between them, so we can say that dynamic SQL has only one advantage over static statements which can be clearly noticed once the application is edited or upgraded, so with Dynamic statements there’s no need for pre-compilation or re-building as long as the access plans are generated at run-time, whereas static statements require regeneration of access plans if they were modified, in addition to the fact that Dynamic SQL requires more permissions, it also might be a way to execute unauthorized code, we don’t know what kind of users we’ll have, so for security it can be dangerous if the programmer didn’t handle it. 

Below mentioned are the basic differences between Static or Embedded and Dynamic or Interactive SQL:

- **Limitation of Dynamic SQL**: We cannot use some of the SQL statements Dynamically. Performance of these statements is poor as compared to Static SQL. 

- **Limitations of Static SQL**: They do not change at runtime thus are hard-coded into applications.
