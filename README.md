# Whatsapp Automation

This script automates the process of sending a message through Whatsapp using the selenium web driver.

## **Requirements**

- Python 3.5 or higher
- Selenium
- Webdriver for your chosen browser (in this case, Microsoft Edge)

## **Usage**

1. Enter the phone number of the recipient when prompted.
2. Enter the message you want to send.

The script will automatically open a new window in your web browser and navigate to the chat with the specified phone number. The message will then be sent.

## **Details**

The script uses asyncio to run the following functions concurrently:

- **`get_input`**: Prompts the user for the phone number and message.
- **`browser_start`**: Opens a new window in the web browser and navigates to the chat with the specified phone number.
- **`send_message`**: Enters the message in the chat and hits send.
- **`disconnect`**: Closes the web browser window.

The **`xpath_list`** function returns a list of xpaths that are used to locate and click the necessary elements to close the web browser window.
