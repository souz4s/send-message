from selenium import webdriver

phoneNumber = input("Enter phone number: ")
message = input("Enter the message you want to send: ")


def browserStart(phoneNumber, message):
    driver = webdriver.Edge(executable_path=r"../../drivers/msedgedriver.exe")
    driver.get("https://web.whatsapp.com/send/?phone=" +
               phoneNumber + "&text&type=phone_number&app_absent=0")


browserStart(phoneNumber, message)
