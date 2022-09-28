import calendar
from pydoc import visiblename
from colorama import Fore, Style
import os
import shutil
import googlesearch
from time import sleep
import time
from datetime import datetime
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def main():
    pass

def create_directory(p_name):
    # checks to see if a directory exists. If it doesn't, it makes a new one.
    screenshots_dir = os.getcwd() + '\Lake-Darkness\projects\{}'.format(p_name)
    
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
            sys.exit()
    
    directory_tuple = (
        screenshots_dir, 
        screenshots_dir + "\community",
        screenshots_dir + "\development",
        screenshots_dir + "\\tokenomics"
        )
    
    return directory_tuple

def project_search(search_query, results):
    # OSINT search on crypto project
    url_list = []
    for q in search_query:

        new_search_generator = googlesearch.search(query=q, lang="en", start=1, stop=results, pause=3)
    
        url_list_conv = list(new_search_generator)
        
        for u in url_list_conv:
            
            url_list.append(u)

    return url_list
    

def screenshots(driver, p_name, url_list, project_dir):
    # Screenshot results
    screenshot_num = 0            

    for url in url_list:

        screenshot_num = screenshot_num + 1
        screenshot_name = '{}_community_screenshot_{}.png'.format(p_name, screenshot_num)
    
        driver.maximize_window()
        

        finished = 0
        while finished == 0:
            try:
                driver.set_page_load_timeout(15)
                driver.get(url)
                driver.get_screenshot_as_file('{}\{}'.format(project_dir, screenshot_name))
                finished = 1
            except:
                with open('{}\\{}_community_URLs.txt'.format(project_dir, p_name), 'a') as f:
                    f.write("Screenshot failed.\n")  
                    
                pass

        t_stamp = timestamp()

        with open('{}\\{}_community_URLs.txt'.format(project_dir, p_name), 'a') as f:
            
            f.write("{}\n".format(screenshot_name))  
            f.write("{}\n".format(url))            
            f.write("{}\n\n".format(t_stamp))

        print(Fore.GREEN + "Took screenshot {}!".format(screenshot_name) + Style.RESET_ALL)
        print(url)

def timestamp():
    current_est = time.gmtime()
    ts = calendar.timegm(current_est)
    ts_conv = datetime.fromtimestamp(ts, tz=None)

    return ts_conv

if __name__=='__main__':
    main()