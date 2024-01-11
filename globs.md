# Globs

#### find all files with pattern names

* asteric - none or any number of any char.

? question mark - one of any char.

+ plus - one occurence.

[] - one of a list of chars.

[-] - match one of a range.

[!] [^] - negate the match. exclamation mark.

[[:punct:]] - one match of a punctuatuion. (!@#$)

[[:space:]] - one match of a space.

[![:space:]] - one match of not a space.

` ls file_name* `

` ls file_name*.txt `

` ls file_name?.txt `

` ls file_name[abc].txt `

` ls file_name[a-c].txt `

` ls file_name[a-zA-Z].txt `

#### differences between globs and regex

<img
  src="/images/linus_toolkit_images/globs/6.png"
  alt="Alt text"
  title="Optional title"
  style="margin: 0 auto;" width="750" height="383">

<img
  src="/images/linus_toolkit_images/globs/7.png"
  alt="Alt text"
  title="Optional title"
  style="margin: 0 auto;" width="750" height="383">

