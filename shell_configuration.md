# Shell configuration

There are two kinds of varaibles. Shell and enviroment variables.

#### Store Configuration for more than the current session

For that, we need to store all the settings in the bash configuration file

` gedit ~/.bash_profle `

<img
  src="/images/linus_toolkit_images/shell_configuration/1.png"
  alt="Alt text"
  title="Optional title"
  style="margin: 0 auto;" width="693" height="452">

## Command history configuration

History configuration is kind of 

#### Set command history such that it won't store duplicate commands:

` HISTCONTROL="ignoredups" `

####  Set command history such that it won't store any command start with space:

` HISTCONTROL="ignorespace" `

####  Both settings:

` HISTCONTROL="ignoredups:ignorespace" `

####  Never record specific commands:

` HISTIGNORE="history*" `

####  Make command history more informative: (More option can be seen here: "man strftime")

` HISTTIMEFORMAT="%h %d %H: %M: %S> `

####  Set number of command stored: (default 1000)

` HISTSIZE="10000" `

` HISTSIZE="-1" ` - unlimited size.

####  Set the number of command stored in the History file:

- All the command are stored in ~/.bash_history when exiting the shell.

` HISTFILESIZE="10000" `

#### Set the history file to append the new shell history instead of override the last one:

- The history file is overrried any time we exit a shell.

` shopt -s histappend `

## Shell variables

#### Show all shell variables and function

` set `

#### Show only shell variables

` (set -o posix; set) ` 

Which run the command 'set -o posix' in a subshell and show the results.

We do this because the set -o posix changes the set command to show only the vars and not the funcs.

#### Show specific shell variables

` echo $PS1 ` - prompt format - the prefix before each command.

` PS1="\u:\$ " ` - will set the prompt format, u is the username.

<img
  src="/images/linus_toolkit_images/shell_configuration/1.png"
  alt="Alt text"
  title="Optional title"
  style="margin: 0 auto;" width="397" height="117">

#### To unset a shell varaible

` unset <var-name> `

#### Show more set options

` set -o `

#### Activate set option

` set -o <set-option> `

#### Deactivate set option

` set +o <set-option> `

## Environment variables

#### Show all those environment variables:

` printenv `

Or specific var, like 'shell'

` printenv SHELL `

` echo #SHELL `

#### To make a shell variable to be an enviroment variable, we export it

` export <var-name> `

#### To unset an enviroment varaible

` export -n <var-name> `





