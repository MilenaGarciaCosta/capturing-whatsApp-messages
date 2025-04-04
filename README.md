
# Capturing WhatsApp Messages
This project aims to monitor a chat or group message feed and capture each sent message. The goal is to search for a specific pattern in the captured message, and if it meets the established criteria, the relevant information is stored and later displayed in the terminal in a clean and formatted manner.


## :wrench: Setting up
First, install Selenium.

```bash
  pip install selenium
  or
  pip3 install selenium
```

This code was developed to run on the Edge browser. This requires a driver that allows Selenium to control Microsoft Edge.
Go to [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and dowload the driver corresponding to the version of your Edge browser.

In your code, you will need to reference the location of this driver. It is recommended that you place it in the following path:

```bash
  C:\WebDriver\msedgedriver.exe
```

:bulb: If you choose to place it in a different location, remember to update the path in your code accordingly.

## :running: How to run
To run the program, open the code file and execute the following command in the terminal

```bash
  python teste-selenium.py
  or
  python3 teste-selenium.py
```
