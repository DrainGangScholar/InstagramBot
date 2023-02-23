# Instagram Unfollower

This script logs into an Instagram account, navigates to the account's following list, and unfollows all the accounts in the list.

## Requirements
- Python 3
- Selenium 3.141.0
- Chrome WebDriver

## Installation
1. Clone this repository or download the script files to your local machine.
2. Install the required Python modules using pip: 
```
   pip install selenium
```
3. Download and install Chrome WebDriver from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).

## Usage
1. Open `main.py` and enter your Instagram username and password in the `username` and `password` variables.
2. Run the script using the following command:
```
python main.py
```
3. The script will open a Chrome browser window and navigate to Instagram. It will log in using the provided username and password.
4. The script will then navigate to the following list and unfollow all accounts in the list.
5. The script will close the browser window once it has finished unfollowing all accounts.

## Note
- The script will pause for a few seconds between each unfollow to ensure that Instagram does not flag the account for suspicious activity.
- Use this script at your own risk. Unfollowing a large number of accounts in a short period of time may result in your account being temporarily or permanently banned by Instagram.
