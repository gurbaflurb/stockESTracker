# stockESTracker
I'm super lazy and just want to build one dashboard in an ELK stack that can track the value of a stock, and how much I've lost.

## Setup
You need the following:
`pip3 install elasticsearch elasticsearch-async python-dotenv`
A working ELK (Or just the EK)
Make an account with Alpha Vantage(https://www.alphavantage.co/). They let you make up to 5 API requests per minute and 500 per day for free(https://www.alphavantage.co/support/#api-key) as of writting. If you want better data consider paying for premium.
I've added an `example.env` file, if you want to use it, rename it to `.env` and fill it out with your own stuff.

## Running
Run this script when the NYSE is open(https://www.nyse.com/markets/hours-calendars). Keep in mind this script does not de-duplication and it grabs the last hours worth of content.Up to you on how you run it. 

## Legal
I am not liable for anything you use this for.