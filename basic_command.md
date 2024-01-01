# Basic commands

#### Print working directory:

` pwd `

#### Simple copy files to the current wd

` cp /some/path . `

#### List of items, including hidden ones

` ls -la `

#### Home directory

Navigating to the home directory is done by using ~

` cd ~ `

Changing to the home directory is done via changing the bash configuration.
~ is expands of the $HOME variable.

Many home directories can be used, in relation to usernames.

` cd ~root `

` cd ~username `

#### Stack of paths

Many paths can be stored, not only the last one.

Store another path to the stack:

` pushd <path> `

Show stack:

` dirs `

Use stack:

` echo ~0 ` - to print the first path in the stack. (most recent one)

` cd ~1 ` - to go to the second recent path.

Remove from stack:

` popd +1 ` - remove the second recent path.

` popd +2 ` - remove the third recent path.

#### List of last used commands

` history `

The number of restored commands are depends on the value in the $HISTSIZE var in shell vars.

#### Run command from the history list

` !14 ` - run the command on the line 14 in the history list.

` !-3 ` - run the fourth command from the bottom of the list.

` !! ` - run the last command line.

` sudo !! ` - can be added as part of command.

#### Search in previous commands

Use ctrl+R and type the requested query.

