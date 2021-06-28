#
#
# main.py 
# Codium(R) Flash Utility.
#
#

# import necessary python modules:
from webbot import Browser
import pyautogui
import time

# Static values that are required to execute the program:input()
#
# IP = '10.25.1.225'
USERNAME = '#USERNAME'
PASSWORD = '#PASSWORD' 
ACS_URL = "http://IP:PORT"
ACS_USER = "#USERNAME"
ACS_PASSWORD = "#PASSWORD"
INFORM = "#INTERVAL"

#
#
# Begin function definitions:
#
#

def login_cpe(ip, uname, passwd):
    sess_init = Browser()
    login = sess_init.go_to(f"https://{ip}/pub/login.htm")
    time.sleep(5)
    sess_init.type(f"{uname}", into="Username")
    sess_init.type(f"{passwd}", into="Password")
    sess_init.click("Login", tag="span")
    return sess_init

def upgrade_cpe(sess, ip, file):
    sess.go_to(f"https://{ip}/version-manager.asp")
    time.sleep(5)
    sess.type(f"{file}", id="file")
    sess.click("Upgrade")

def add_certs_cpe(sess, ip, ca_cert, certpair_loc):
    sess.go_to(f"https://{ip}/cbsd.asp")
    time.sleep(5)
    cbsd_serial = sess.find_elements(id="serial_number")[0].get_attribute('innerHTML')  
    pem_loc = str(f"{certpair_loc}2AWJHOCB6_{cbsd_serial}.p12.pem")     # Adjust or tweak file names as necessary.
    key_loc = str(f"{certpair_loc}2AWJHOCB6_{cbsd_serial}.p12.key")
    sess.type(f"{ca_cert}", id="ca_file")
    sess.type(f"{pem_loc}", id="cert_file")
    sess.type(f"{key_loc}", id="key_file")
    sess.click("Upload", tag="span") 
    time.sleep(30)
    pyautogui.press('enter')

def upload_config_cpe(sess, ip, conf):
    sess.go_to(f"https://{ip}/maintenance.asp")
    time.sleep(5)
    sess.type(f"{conf}", id="file")
    sess.click("Upload", tag="span")
    time.sleep(30)
    pyautogui.press('enter')

def activate_acs(sess, ip):
    sess.go_to(f"https://{ip}/tr069.asp")
    time.sleep(3)
    sess.click(id="enable")
    time.sleep(3)
    sess.type(f"{ACS_URL}", id="url")
    sess.type(f"{ACS_USER}", id="username")
    sess.type(f"{ACS_PASSWORD}", id="password")
    sess.click(id="periodic_enable")
    time.sleep(3)
    sess.type(f"{INFORM}", id="periodic_interval")
    sess.click("Submit")
    time.sleep(5)
    pyautogui.press('enter') # for some reason, it's critical to dismiss prompt!!

#
#
# End Function Definitions
#
#

#
#
# Begin Main Runtime Definition:
#
#

def main():

    with open("ips.txt","r") as ips:
        for ip in ips:
            IP = f"{ip}"
        
            main_session = login_cpe(IP, USERNAME, PASSWORD) 
            # Wait for main page to load:    
            time.sleep(5)

            activate_acs(main_session, IP)
            # Prompt to end the program.  
            print(f"done with {IP}")
            main_session.close_current_tab()

# 
#
# End Main Runtime Definition
#
#

#
#
# Boilerplate Execution Condition:
#
#

if __name__ == "__main__":
    main()
