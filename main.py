import Darkness as dark
from colorama import Fore, Style

def main():
    # Insert a project name
    print("Input a project name:")
    project_name = str(input().lower())

    print("Input the project's site URL:")
    project_site = str(input().lower())
    # Create google search strings.
    result_num_c = 1
    community_queries = [
        
        '{} failures'.format(project_name),
        '{} bug'.format(project_name),
        '{} problems'.format(project_name),
        '{} risks'.format(project_name),
        
        ]
    
    result_num_d = 1
    development_queries = [
        
        '{} team members site:{}'.format(project_name, project_site),
        '{} development team'.format(project_name),
        'who built {}'.format(project_name),
        '{} company location'.format(project_name),
        '{} company formation'.format(project_name),
        
        ]

    result_num_t = 1
    tokenomics_queries = [
        
        "{} purpose site:{}".format(project_name, project_site), 
        '{} token usecase'.format(project_name),
        '{} whitepaper filetype:pdf'.format(project_name),
        '{} whitepaper site:{}'.format(project_name, project_site),

        ]
    
    # Create project directory. [0, 1, 2, 3] = [main, community, development, tokenomics]
    project_directory = dark.create_directory(project_name)

    # Grab project URLs
    print(Fore.YELLOW + "GETTING URLS" + Style.RESET_ALL)
    
    community_urls = dark.project_search(community_queries, result_num_c, 'community')
    dark.write_url_list_txt(community_urls, project_directory, project_name)
   
    development_urls = dark.project_search(development_queries, result_num_d, 'development')
    dark.write_url_list_txt(development_urls, project_directory, project_name)
    
    tokenomics_urls = dark.project_search(tokenomics_queries, result_num_t, 'tokenomics')
    dark.write_url_list_txt(tokenomics_urls, project_directory, project_name)
    
    # Take URL page screenshots and post to the project folder
    print(Fore.YELLOW + "ATTEMPTING TO TAKE SCREENSHOTS" + Style.RESET_ALL)
    
    dark.screenshot_threading(project_name, community_urls, project_directory[1], "community")
    
    dark.screenshot_threading(project_name, development_urls, project_directory[2], "development")
    
    dark.screenshot_threading(project_name, tokenomics_urls, project_directory[3], "tokenomics")


    print(Fore.YELLOW + "Finished preliminary recon: {}".format(project_name) + Style.RESET_ALL)

if __name__=='__main__':
    main()