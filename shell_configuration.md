# Shell configuration

### Command history configuration

#### Store Configuration for more than the current session

For that, we need to store all the settings in the bash configuration file

` gedit ~/.bash_profle `

<img
  src="/images/linus_toolkit_images/shell_configuration/1.png"
  alt="Alt text"
  title="Optional title"
  style="margin: 0 auto;" width="693" height="452">

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