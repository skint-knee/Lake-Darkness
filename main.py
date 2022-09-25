import Darkness as dark

def main():
    
    # Put screenshots in the directory

    # Insert a project name
    print("Input a project name:")
    project_name = str(input().lower())

    # Create project directory.
    #print("CREATING DIRECTORIES")
    #dark.create_directory(project_name)

    print("GETTING URLS")
    project_urls = dark.project_search(project_name)
    
    print("TAKING SCREENSHOTS")
    dark.screenshots(project_name, project_urls)

if __name__=='__main__':
    main()