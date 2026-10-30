# pollevbot

pollevbot is a bot that automatically responds to polls on pollev.com. It continually checks if a specified host has opened any polls. Once a poll has been opened, it submits the first response.

**for UCI Account only**

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3.6 or higher
- patchright (bundles its own Chromium)

## Setup

To set up this project on your local machine, follow these steps:

1. **Clone the repository:**
2. **Install required Python packages:**

```pip install patchright```
```patchright install chromium```


## Usage

Set the desired poll host in `main.py`

```angular2html
    present_code = "code123"
```

And run the script. A Chromium window opens on the Pollev page: log in there yourself
(UCI NetID + Duo), then press Enter in the terminal and the bot starts monitoring for polls.

Chromium runs on the persistent profile in `.browser-profile`, so the login (and Chrome's saved
password) survives between runs — same setup as perusallbot.


