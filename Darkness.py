from colorama import Fore, Style
import os
import shutil
import googlesearch
from time import sleep
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
    

def screenshots(p_name, url_list, project_dir):
    # Screenshot results

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    screenshot_num = 0

    for url in url_list[0]:

        screenshot_num = screenshot_num + 1
        screenshot_name = '{}_community_screenshot_{}.png'.format(p_name, screenshot_num)

        driver.maximize_window()
        driver.get(url)
        sleep(3)
        driver.get_screenshot_as_file('{}\{}'.format(project_dir[1], screenshot_name))

        print("Took screenshot {}!".format(screenshot_name))
        print(url)

    for url in url_list[1]:

        screenshot_num = screenshot_num + 1
        screenshot_name = '{}_development_screenshot_{}.png'.format(p_name, screenshot_num)

        driver.maximize_window()
        driver.get(url)
        sleep(3)
        driver.get_screenshot_as_file('{}\{}'.format(project_dir[2], screenshot_name))

        print("Took screenshot {}!".format(screenshot_name))
        print(url)

    for url in url_list[2]:

        screenshot_num = screenshot_num + 1
        screenshot_name = '{}_tokenomics_screenshot_{}.png'.format(p_name, screenshot_num)

        driver.maximize_window()
        driver.get(url)
        sleep(3)
        driver.get_screenshot_as_file('{}\{}'.format(project_dir[3], screenshot_name))

        print("Saved {}!".format(screenshot_name))
        print(url)
    
    driver.close()

if __name__=='__main__':
    main()