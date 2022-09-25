import Darkness as dark

def main():
    
    # Put screenshots in the directory

    # Insert a project name
    print("Input a project name:")
    project_name = str(input().lower())

    # Create project directory. [0, 1, 2, 3] = [main, community, development, tokenomics]
    print("CREATING DIRECTORIES")
    project_directory = dark.create_directory(project_name)

    # Multi-query 

    # Grab project URLs
    print("GETTING URLS")
    project_urls = dark.project_search(project_name)
    
    # Take URL page screenshots and post to the project folder
    print("TAKING SCREENSHOTS")
    dark.screenshots(project_name, project_urls, project_directory)

if __name__=='__main__':
    main()