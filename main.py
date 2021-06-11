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

# Static values that are required to execute the program:
#
IP = '192.168.0.1'
USERNAME = '#USERNAME'
PASSWORD = '#PASSWORD' 
UPGRADE_FILE = '#FILE'
TARFILE = '#FILE'
CERTPAIR_LOC = '#FILE'
CONFIG_LOC = '#FILE'

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
    # This is a basic example of the program running:
    # in a nutshell, the radio gets firmware flashed,
    # certificates added, and a custom config uploaded.  
    # The idea behind the example is to illustrate taking a radio from 
    # out-of-box condition to production-ready.
    #
    # Initiate main browser session:
    main_session = login_cpe(IP, USERNAME, PASSWORD) 
    # Wait for main page to load:    
    time.sleep(5)
    # Example, Upgrade CPE:
    upgrade_cpe(main_session, IP, UPGRADE_FILE)
    # Wait for reboot post-upgrade:
    time.sleep(60)
    # NOTE system reboots after update, login required:
    main_session = login_cpe(IP, USERNAME, PASSWORD) 
    # Example, add certificates:
    add_certs_cpe(main_session, IP, TARFILE, CERTPAIR_LOC)
    # Example, add configuration:
    upload_config_cpe(main_session, IP, CONFIG_LOC)

    # Prompt to end the program.  
    input('press enter to exit program successfully.')

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
