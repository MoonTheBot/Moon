# Moon
Moon is a multipurpose Discord bot with more than general common features.

# Requirements
- Node [Version 8.0.0 or higher](https://node.js.org)
- Git command line ([Windows](https://git-scm.com/download/win) | [Linux](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) | [MacOS](https://git-scm.com/download/mac)) installed
- Windows build tools, this is required for the database being used but also for a lot of other dependencies the bot and framwork use.

# Downloading
In command prompt, in location of choice, run the following command:

`git clone https://github.com/Prylaris/Moon.git`

After that process has completed, run `cd Moon`

In order for the dependencies to install, run `npm install --save`

# Configuration
Please edit the `config.js` file and enter all of the required fields.

# Example Command
If you'd like to add your own commands to the bot, simply use the following template:

```js
const Discord = require("discord.js");

exports.run = async (client, message, args, level, error) => {

    // Bot Code Here

    if (error) {
        return message.channel.send("An unexpected error has occurred, try again later.");
    }
};

exports.conf = {
    enabled: true,
    guildOnly: false,
    aliases: [],
    permLevel: "User"
};

exports.help = {
    name: "test",
    category: "Information",
    description: "Super dope testing command.",
    usage: "test"
};
```

# Moon API
If you'd like to know how to use the API for Moon, here are some examples to get you started:

## Logging In and Out:
```py
from mapi import Client

session = Client(ratelimit=3, bot=None, hide_token=True) # Initialize a client session with:
# A 3 seconds global ratelimit
# No bot parameter
# Hide_token set to True to hide the token from out str representation

session.login("YourAPITokenHere")

# Here we can preform whatever actions we like

print(session) # This will return the str representation of the session which contains a lot of useful information

session.logout() # This is in no way necessary unless you wish to login with a different key later on
```

## Retrieving metrics
```py
from mapi import Client
import json # Not needed it just looks better with this

session = Client().login("APITokenGoesHere")

print(json.dumps(session.metrics(), indent=4, sort_keys=True))
session.logout()
```

## Showing str representation
```py
from mapi import Client

session = Client().login("APIKey")

print(session)
session.logout()
```

# License
This project is placed under the MIT license.
