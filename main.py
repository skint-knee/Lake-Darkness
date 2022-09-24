import Darkness as dark
import googlesearch

from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



def main():
    
    # Insert a project name to create directory
    #print("Input a project name:")
    #project_name = str(input().lower())

    #dark.create_directory(project_name)

    # OSINT search on crypto project
    #new_search = googlesearch.search("bitcoin", num_results=10, lang="en") 

    #num = 0
    #for n in new_search:
        #num = num + 1
        #print("{}: {}".format((num), n))

    # Screenshot results
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get("http://www.python.org")

    sleep(1)
    driver.get_screenshot_as_file("screenshot.png")

    driver.close()
    # Put screenshots in the directory


if __name__=='__main__':
    main()