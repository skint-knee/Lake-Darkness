import Darkness as dark
from colorama import Fore, Style

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
        "{} ICO or token distribution".format(project_name), 
        "which exchange to buy {}".format(project_name)
        
        ]

    # Create project directory. [0, 1, 2, 3] = [main, community, development, tokenomics]
    print("CREATING DIRECTORIES")
    project_directory = dark.create_directory(project_name)

    # Grab project URLs
    print("GETTING URLS")
    print("community")
    community_urls = dark.project_search(community_queries, result_num)
    print("development")
    development_urls = dark.project_search(development_queries, result_num)
    print("tokenomics")
    tokenomics_urls = dark.project_search(tokenomics_queries, result_num)
    
    url_list_of_lists = [community_urls, development_urls, tokenomics_urls]
    # Take URL page screenshots and post to the project folder
    print("ATTEMPTING TO TAKE SCREENSHOTS")
    dark.screenshots(project_name, url_list_of_lists, project_directory)

    print(Fore.YELLOW + "Finished preliminary recon on: {}".format(project_name) + Style.RESET_ALL)

if __name__=='__main__':
    main()