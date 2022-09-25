import Darkness as dark

from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

def main():
    
    # Insert a project name
    print("Input a project name:")
    project_name = str(input().lower())

    # Create project directory.
    #dark.create_directory(project_name)

    project_urls = dark.project_search(project_name)
    
    num = 0
    for n in project_urls:
        num = num + 1
        print("{}: {}".format((num), n))


"""
    # Screenshot results
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.get("http://www.python.org")

    sleep(1)
    driver.get_screenshot_as_file("screenshot.png")

    driver.close()
    # Put screenshots in the directory
"""

if __name__=='__main__':
    main()