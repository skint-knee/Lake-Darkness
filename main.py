import Darkness as dark
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def main():
    # Insert a project name
    print("Input a project name:")
    project_name = str(input().lower())
    # Create google search strings.
    result_num = 1
    
    
    
    community_queries = [
        
        "{} site:twitter.com -hashtag".format(project_name), 
        '{} governance'.format(project_name), 
        '{} competitors'.format(project_name)
        
        ]
    
    development_queries = [
        
        "{} website".format(project_name), 
        "{} whitepaper OR developer docs".format(project_name), 
        "{} purpose".format(project_name)
        
        ]
    tokenomics_queries = [
        
        "{} total supply".format(project_name), 
        "{} ICO or token distribution -site:icodrops.com".format(project_name), 
        "which exchange to buy {}".format(project_name)
        
        ]
    
    # Create project directory. [0, 1, 2, 3] = [main, community, development, tokenomics]
    print("CREATING DIRECTORIES")
    project_directory = dark.create_directory(project_name)

    # Grab project URLs
    print("GETTING URLS")
    print("Getting Community URLs...")
    community_urls = dark.project_search(community_queries, result_num)
    print("Getting Development URLs...")
    development_urls = dark.project_search(development_queries, result_num)
    print("Getting Tokenomics URLs...")
    tokenomics_urls = dark.project_search(tokenomics_queries, result_num)
    
    #url_list_of_lists = [community_urls, development_urls, tokenomics_urls]
    # Take URL page screenshots and post to the project folder
    print("ATTEMPTING TO TAKE SCREENSHOTS")
    d = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    dark.screenshots(d, project_name, community_urls, project_directory[1])
    dark.screenshots(d, project_name, development_urls, project_directory[2])
    dark.screenshots(d, project_name, tokenomics_urls, project_directory[3])
    
    d.close()

    print(Fore.YELLOW + "Finished preliminary recon: {}".format(project_name) + Style.RESET_ALL)

if __name__=='__main__':
    main()