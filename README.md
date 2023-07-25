# Selenium-SAML-OpenFortiVPN: OpenFortiClient SAML Login Cookie Retrieval using Selenium

The "Selenium-SAML-OpenFortiVPN" is a Python script designed to automate the process of retrieving the SVPNCOOKIE required for authenticating an OpenFortiClient session using the SAML login mechanism. The script utilizes the Selenium WebDriver library to automate interactions with a web browser. It navigates to the SSL VPN login page and, upon successful login, retrieves the essential authentication cookie.

## Usage:
To run the script, ensure you have Python 3 installed on your system along with the required dependencies, including the Selenium WebDriver, and either the Firefox or Chrome browser. The script can be executed from the command line as follows:

```
python3 script_name.py <host> [--port <port>] [--browser <browser>]
```

- `<host>`: The hostname or IP address of the target OpenFortiGate SSL VPN server.
- `--port <port>`: (Optional) The port number of the SSL VPN server. The default value is 10443.
- `--browser <browser>`: (Optional) The browser to use for automation. Available choices are "firefox" and "chrome". The default is "chrome".

## Script Flow:
1. The script initializes the specified browser using the Selenium WebDriver and navigates to the target SSL VPN URL.
2. It waits for the presence of the element with the ID "saml-login-bn," which corresponds to the SAML login button on the SSL VPN login page.
3. The script then executes a JavaScript function, "launchSamlLogin()", to initiate the SAML login process.
4. It further waits for the browser to navigate to a page ending with "/sslvpn/portal.html," which indicates a successful login and redirection to the portal page.
5. Once the SAML authentication process is complete, the script retrieves the "SVPNCOOKIE" from the browser's cookies and prints its value to the console.

## Purpose:
The primary purpose of this script is to automate the SAML login process for OpenFortiClient authentication and obtain the required SVPNCOOKIE. By running this script, users can conveniently retrieve the necessary cookie, which can then be used with the "openfortivpn --cookie" command to establish a secure SSL VPN connection using OpenFortiClient.

## Note:
- The script's successful execution depends on the SSL VPN login page's structure and behavior. Any changes to the login process or elements on the page may require adjustments to the script for it to function correctly.
- It is essential to exercise caution when automating login processes and handling authentication cookies. Ensure compliance with security policies and obtain proper authorization before using this script in production environments.