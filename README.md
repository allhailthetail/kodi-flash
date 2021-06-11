# kodi-flash
A Collection of Simple Flash Scripts for CBRS LTE CPEs

# Description:
* kodi-flash is a simple set of scripts which aids in automating the tedious "flashing" of configurations and firmware to LTE CPEs.  More specifically, this project was designed for Codium(R) brand radios, which lack an API or other means of automation.  

* In a nutshell, the script initiates a Chrome web wrapper and uses python modules to parse data and interact with the webpage.  

# Other Requirements:
* Because this project uses chrome for the web wrapper, Google Chrome is an obvious dependency. 
* As this project was developed solely on Linux, it's currently recommended to follow suit and avoid mac or Windows.  Support for other operating systems should be farily easy.  However, that is for a later date.  
* For stability, create a Python virtual environment and install dependencies per "requirements.txt" 

# NOTE: 
* This utility interacts with a web browser session in order to carry out automation.  As the project currently stands, it's best to call the program and sit back and watch.  Trying to multi-task while the program is running isn't a great idea.  
