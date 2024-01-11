# Bash overview

#### $ sign

The Character $ in bash shell, make substitution with bash variable

` echo This is my username $USER `

#### double quotes ""

No change in the echo command:

` echo "This is my username $USER" `

#### single quotes ''

Return literaly the value inside:

` echo 'This is my username $USER' `

useful in grep command like this:

` grep '.*/udp' /etc/services `

#### back ticks ``

Execute command between them.

#### brace expansion

Run mulitple commands in one line:

` echo sp{i,a}ce `

` touch file{0..2}.txt `

` cat file{0..100..2}.log `

#### tree command

Check tree dir and files of a dir:

tree /path/

#### make local variables

define it:

` pdir='/tmp/file/today/' `

and use it:

` mkdir -p $pdir `

and inside a string use {}:

` mkdir -p "{$pdir}/hour `

#### count number of lines in a commad

` ls -l | wc -l `

#### Boolean logic

run sequentially:

` ; `

OR AND bollean condition:

` || && `

Line terminator:

` & ` 

#### 