import Darkness as dark

def main():
    # Insert a project name
    print("Input a project name:")
    project_name = str(input().lower())
    # Create google search strings.
    community_queries = [
        
        "{} site:twitter.com".format(project_name), 
        '{} site:reddit.com'.format(project_name), 
        '{} site:youtube.com'.format(project_name)
        
        ]
    development_queries = [
        
        "{} whitepaper".format(project_name), 
        "{} development team".format(project_name), 
        "{} roadmap".format(project_name)
        
        ]
    tokenomics_queries = [
        
        "{} price chart".format(project_name), 
        "{} total supply".format(project_name), 
        "{} tokenomics".format(project_name)
        
        ]

    # Create project directory. [0, 1, 2, 3] = [main, community, development, tokenomics]
    print("CREATING DIRECTORIES")
    project_directory = dark.create_directory(project_name)

    # Grab project URLs
    print("GETTING URLS")
    result_num = 3
    print("community")
    community_urls = dark.project_search(community_queries, result_num)
    print("development")
    development_urls = dark.project_search(development_queries, result_num)
    print("tokenomics")
    tokenomics_urls = dark.project_search(tokenomics_queries, result_num)
    
    url_list_of_lists = [community_urls, development_urls, tokenomics_urls]
    # Take URL page screenshots and post to the project folder
    print("TAKING SCREENSHOTS")
    dark.screenshots(project_name, url_list_of_lists, project_directory)

if __name__=='__main__':
    main()