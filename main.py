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
        
        '{} negative news'.format(project_name),
        '{} issues'.format(project_name),
        '{} problems'.format(project_name),
        '{} risks'.format(project_name),
        
        ]
    
    development_queries = [
        
        '{} team members'.format(project_name),
        '{} site:linkedin.com'.format(project_name),
        'who built {}'.format(project_name),
        '{} company location'.format(project_name),
        '{} team location'.format(project_name),
        
        ]
    tokenomics_queries = [
        
        "{} token purpose".format(project_name), 
        '{} token usecase'.format(project_name),
        '{} token whitepaper'.format(project_name),

        ]
    
    # Create project directory. [0, 1, 2, 3] = [main, community, development, tokenomics]
    print("CREATING DIRECTORIES")
    project_directory = dark.create_directory(project_name)

    # Grab project URLs
    print("GETTING URLS")
    print("Getting Community URLs...")
    community_urls = dark.project_search(community_queries, result_num)
    dark.write_url_list_txt(community_urls, project_directory, project_name)
    print("Getting Development URLs...")
    development_urls = dark.project_search(development_queries, result_num)
    dark.write_url_list_txt(development_urls, project_directory, project_name)
    print("Getting Tokenomics URLs...")
    tokenomics_urls = dark.project_search(tokenomics_queries, result_num)
    dark.write_url_list_txt(tokenomics_urls, project_directory, project_name)
    
    #url_list_of_lists = [community_urls, development_urls, tokenomics_urls]
    # Take URL page screenshots and post to the project folder
    print("ATTEMPTING TO TAKE SCREENSHOTS")
    
    

    dark.screenshot_threading(project_name, community_urls, project_directory[1], "community")
    dark.screenshot_threading(project_name, development_urls, project_directory[2], "development")
    dark.screenshot_threading(project_name, tokenomics_urls, project_directory[3], "tokenomics")
    
    

    print(Fore.YELLOW + "Finished preliminary recon: {}".format(project_name) + Style.RESET_ALL)

if __name__=='__main__':
    main()