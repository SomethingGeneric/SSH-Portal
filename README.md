# SSH-Portal
Small example of a way a user account could be restricted when logging in to SSH
## Demo
* Point your ssh client to `ssh://guest@mattcompton.me`
* Password is `account`
## Setup (assuming you're using OpenSSH server on some *nix-ish system)
* Create user to be used as portal account. (differs by OS), and switch to it
* `git clone https://github.com/SomethingGeneric/SSH-Portal`
* `cd SSH-Portal && python3 -m pip install -r requirements.txt`
* Optional:
    * Default commands include using `cowsay`, `lolcat`, and `fortune.` If you're on Debian/Ubuntu/Mint: `sudo apt-get install -y cowsay lolcat fortune` (might want to do on regular sudo account instead of making the portal account a sudoer.)
* Edit `/etc/ssh/sshd_config` and add something like
    * ```
        Match User <username>
            ForceCommand python3 <path/to/repo/>portal.py
* Done!
## Adding/changing commands
* In the repo directory, add a line to `commands.txt`, with syntax:
    * ```<command_that_user_inputs>:<command_that_system_executes>```
* NOTE: If you're using a sh script or system command, you might want to consider using this command, as sometimes portal/ssh immediatley clears screen:
    * ```python3 wr.py <path_to_script>```
