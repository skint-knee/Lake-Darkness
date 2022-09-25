from colorama import Fore, Style
import os
import shutil
import googlesearch
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def main():
    pass

def create_directory(p_name):
    # checks to see if a directory exists. If it doesn't, it makes a new one.
    screenshots_dir = os.getcwd() + '\crypto_projects\{}'.format(p_name)
    
    isExist = os.path.exists(screenshots_dir)
    
    if not isExist:
        os.makedirs(screenshots_dir)
        os.makedirs(screenshots_dir + "\community")
        os.makedirs(screenshots_dir + "\development")
        os.makedirs(screenshots_dir + "\\tokenomics")

        print(Fore.GREEN + "Successfully created:", screenshots_dir)
        print("Successfully created:", screenshots_dir + "\community")
        print("Successfully created:", screenshots_dir + "\development")
        print("Successfully created:", screenshots_dir + "\\tokenomics" + Style.RESET_ALL)
    
    else:
        print("A directory for {} exists. Replace?".format(p_name))

        y_list = ("y", "yes", "Y", "YES", "Yes")
        
        replace = input()

        if replace in y_list:
            shutil.rmtree(screenshots_dir)

            print(Fore.YELLOW + "Previous project data removed: {}.".format(p_name))
            print(">> Creating new directory...\n" + Style.RESET_ALL)
            
            create_directory(p_name)     
        else:
            print(Fore.RED + "Declined action." + Style.RESET_ALL)

def project_search(p_name):
    # OSINT search on crypto project
    new_search_generator = googlesearch.search(query=p_name, lang="en", start=1, stop=3, pause=2) 
    
    return list(new_search_generator)
    

def screenshots(p_name, url_list):
    # Screenshot results
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    
    screenshot = 0
    for url in url_list:

        driver.get(url)
        sleep(1)
        screenshot = screenshot + 1
        driver.get_screenshot_as_file("{}_screenshot_{}.png".format(p_name, screenshot))
    
    driver.close()

if __name__=='__main__':
    main()