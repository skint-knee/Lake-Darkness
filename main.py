import Darkness as dark

def main():
    # Insert a project name
    print("Input a project name:")
    project_name = str(input().lower())
    # Create google search strings.
    queries = [
        
        "{} community".format(project_name), 
        "{} documentation whitepaper filetype:pdf".format(project_name), 
        "{} total supply".format(project_name)
        
        ]

    # Create project directory. [0, 1, 2, 3] = [main, community, development, tokenomics]
    print("CREATING DIRECTORIES")
    project_directory = dark.create_directory(project_name)

    # Grab project URLs
    print("GETTING URLS")
    print("community")
    project_urls_0 = dark.project_search(queries[0])
    print("development")
    project_urls_1 = dark.project_search(queries[1])
    print("tokenomics")
    project_urls_2 = dark.project_search(queries[2])
    
    url_list_of_lists = [project_urls_0, project_urls_1, project_urls_2]
    # Take URL page screenshots and post to the project folder
    print("TAKING SCREENSHOTS")
    dark.screenshots(project_name, url_list_of_lists, project_directory)

if __name__=='__main__':
    main()