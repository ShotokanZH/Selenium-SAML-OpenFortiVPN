#!/usr/bin/env python3
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import argparse
import sys


def prepareBrowser(name:str) -> WebDriver:
    """
    browsers，"firefox","chrome"
    """
    width = 800
    height = 800
    name = name.lower()
    if name == "firefox":
        print("Starting: Firefox", file=sys.stderr)
        options = webdriver.FirefoxOptions()
        options.add_argument(f"--width={width}")
        options.add_argument(f"--height={height}")
        driver = webdriver.Firefox(options=options)
        return driver
    elif name == "chrome":
        print("Starting: Chrome", file=sys.stderr)
        options = webdriver.ChromeOptions()
        options.add_argument(f"--window-size={width},{height}")
        driver = webdriver.Chrome(options=options)
        return driver
    raise Exception("Unknown browser!")


def browse(url:str, browser:str) -> str:
    driver = prepareBrowser(browser)
    driver.get(url)
    wait = WebDriverWait(driver, 120)
    wait.until(EC.presence_of_element_located((By.ID, "saml-login-bn")))
    driver.execute_script("launchSamlLogin()")
    wait.until(lambda driver: driver.current_url.split("#")[0].endswith("/sslvpn/portal.html"))
    cookie = driver.get_cookie("SVPNCOOKIE")
    return cookie["value"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", type=str)
    parser.add_argument("--port", "-p", type=int, default=10443)
    parser.add_argument("--browser", "-b", choices=["firefox","chrome"], default="chrome")
    args = parser.parse_args()
    url = f"https://{args.host}:{args.port}"
    cookie = browse(url, args.browser)
    print(cookie)

if __name__ == "__main__":
    main()