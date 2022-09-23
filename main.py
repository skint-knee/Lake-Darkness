import Darkness as dark

def main():
    print("Input a project name:")
    project_name = str(input().lower())

    dark.create_directory(project_name)

    # OSINT search on crypto project
    # Screenshot results
    # Put screenshots in the directory


if __name__=='__main__':
    main()