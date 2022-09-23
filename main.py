import os
import shutil
from colorama import Fore, Back, Style


def main():
    print("Input a project name:")
    project_name = str(input().lower())

    create_directory(project_name)

    # OSINT search on crypto project
    # Screenshot results
    # Put screenshots in the directory

def create_directory(p_name):
    # checks to see if a directory exists. If it doesn't, it makes a new one.
    screenshots_dir = 'C:/Users/rayqu/Documents/Programming/Python/LakeDarkness/{}'.format(p_name)
    
    isExist = os.path.exists(screenshots_dir)
    
    if not isExist:
        os.makedirs(screenshots_dir)
        os.makedirs(screenshots_dir + "/community")
        os.makedirs(screenshots_dir + "/development")
        os.makedirs(screenshots_dir + "/tokenomics")

        print(Fore.GREEN + "Successfully created:", screenshots_dir)
        print("Successfully created:", screenshots_dir + "/community")
        print("Successfully created:", screenshots_dir + "/development")
        print("Successfully created:", screenshots_dir + "/tokenomics" + Style.RESET_ALL)
    
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

if __name__=='__main__':
    main()