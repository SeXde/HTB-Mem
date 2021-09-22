This challenge consisted in eval code injection however it wasn't that trivial because you have to bypass the addslashes() filter in order to get remote code execution.

First things first, if you click the text "Nah, that doesn't work for me. Try again!" you will see a weird "?format=r" in the URL.

Ok, cool now you will try to inject code but it doesn't work (the filter addslashes block regular code execution) it's ok tho, don't worry if you encode the code it actually works.

In the repository i will let you a simple script which encode php functions to byass the addslashes filter.

So now we have the function encoded and we could simply try the classic function "system("/bin/ls -l")" that's ok but we'll have to find the flag listing other directories.

If we introduce "system("/bin/ls -l ..")" it will show us the flag name ... We almost there! with "system("/bin/cat ../{flagName}")" we will fianlly get the flag! easy!