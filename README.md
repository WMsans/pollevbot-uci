# pollevbot

pollevbot is a bot that automatically responds to polls on pollev.com. It continually checks if a specified host has opened any polls. Once a poll has been opened, it submits the first response.

**for UCI Account only**

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3.6 or higher
- Selenium WebDriver
- ChromeDriver (compatible with your Chrome version)

## Setup

To set up this project on your local machine, follow these steps:

1. **Clone the repository:**
2. **Install required Python packages:**

```pip install selenium```


## Usage

Set the desired poll host in `main.py`

```angular2html
    present_code = "code123"
```

And run the script. A Chrome window opens on the Pollev login page: log in there yourself
(UCI NetID + Duo), then press Enter in the terminal and the bot starts monitoring for polls.


