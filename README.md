# Browser Automation for Kiosk Mode Testing

This repository contains a Python script to open four instances of Google Chrome, load specified URLs, display them in measured quadrants of your screen, and refresh every 90 seconds. The script is designed to test the behavior of our predefined kiosk mode scenarios in an environment similar to which they will be displayed at EIC. 

## Prerequisites

To run this script, you need to have the following installed on your system:

- Python 3 (preferably the latest version)
- Google Chrome

## Setup

1. Clone this repository to your local machine
2. CD into the repository folder
3. Create the virtual environment with the command: `python3 -m venv venv`
4. Activate the virtual environment with the command `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
5. Install the required Python packages using the following command in your terminal: `pip install -r requirements.txt`

## Usage

1. Open the `kiosk_testing.py` file and modify the variables in the url array to include the scenarios you would like to test. Only 4 scenarios can be tested at a single time. 
2. Run the script using the following command in your terminal: `python kiosk_testing.py`

The script will open four instances of Google Chrome, each displaying one of the specified URLs. The pages will refresh every 90 seconds.

The SIT urls will require for you to be on the VPN. Alternatively, you can clone the Worldview repository and run the development branch locally and use the local urls. 
