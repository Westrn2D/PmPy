## Welcome to PmPy aka. Password manger python... (still working on a better name)

### What's new?:
- Added a PIN.
- And safe storage of said PIN.






### What can it do
It's simple really. It's a python password manager using the Cryptography library and the json library to store passwords and python.

### Syntax

| Syntax | Description |
| ----------- | ----------- |
| SHOW | Shows all stored passwords |
| GET | Shows a specific login |
|SAVE | Saves the temporary directory|
|NEW | Initializes prompt for new login |
|DELETE | Deletes specfied "profile" (Username password combo)|
|EXIT | Quits the program without saving any not saved profiles|

### Goals

- [x] Save passwords in a file (.txt, .json, .sql , etc.)
- [x] Be able to run this as a binary (.exe)
- [ ] MacOS support (for .app) has not been finished yet. 
- [x] More security features. [^1]
- [x] And make the syntax applicable, as it doesn't work nor have an interface
  for it  yet

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

Copyright © 2026 Constantinos Philiastides

### Footnotes
[^1]: If you run the program and don't set a PIN or for whatever reason the Setup file doesn't exist please download it from the
latest release.
