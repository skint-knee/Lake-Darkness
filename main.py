import Darkness as dark


def main():
    
    # Put screenshots in the directory

    # Insert a project name
    print("Input a project name:")
    project_name = str(input().lower())

    # Create project directory.
    #dark.create_directory(project_name)

    project_urls = dark.project_search(project_name)

    dark.screenshots(project_name, project_urls)


    """
    num = 0
    for n in project_urls:
        num = num + 1
        print("{}: {}".format((num), n))

    
    """
    

if __name__=='__main__':
    main()