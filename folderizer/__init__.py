import argparse
import os

def createFolder(targetPath, folderName):
    print(folderName + " type detected")
    folderPath = os.path.join(targetPath, folderName)
    print(folderPath)
    if not (os.access(folderPath, os.F_OK)):
        print('creating images folder')
        os.mkdir(folderPath)
    else:
        print(folderPath + " already created")
    return folderPath

fileCategories = {}
def addFileCategory(categoryName, extensions):
    fileCategories[categoryName] = {"folderName": f"{categoryName}", "extensions" : extensions, "fileCount" : 0, "movedCount" : 0}

def dictionarySummary(dictionary):
    print('------------------------------------')
    print('SUMMARY')
    print('------------------------------------')
    for entry, properties in dictionary.items():
        print(f"{entry} found: {properties['fileCount']}")
        print(f"{entry} successfully moved: {properties['movedCount']}")

def main():
    # Define extensions
    imageExtensions = [".jpeg", ".jpg", ".png", ".gif"]
    videoExtensions = [".mp4", ".flv", ".m4v", ".webm"]
    textExtensions = [ ".txt", ".md", ".doc", ".docx", ".pdf"]

    # Populate fileCategories with category and extensions
    addFileCategory("images", imageExtensions)
    addFileCategory("videos", videoExtensions)
    addFileCategory("textFiles", textExtensions)

    # Initialize parser
    parser = argparse.ArgumentParser(
        prog="folderizer",
        description="File organization command-line tool.",
        epilog="Thanks for using %(prog)s!")
    parser.add_argument('filepath')
    parser.add_argument("-v","--version", action="version", version="%(prog)s 0.1.1")
    parser.add_argument("-d", "--default", action='store_true', help="Sorts files into folders by category (image, video, text, code, etc)")
    args = parser.parse_args()
    print(args, args.filepath, args.default)

    # --default subroutine
    def defaultBehavior():
        # Extract target path from arguments
        target_path = os.path.abspath(args.filepath)
        # Check if filepath exists
        if (os.access(target_path, os.F_OK)):
            with os.scandir(target_path) as it:
                # Iterate through each non-hidden file in target_path
                for entry in it:
                    if not entry.name.startswith('.') and entry.is_file():
                        # Extract file extension from entry
                        fileExtension = os.path.splitext(entry.name)[1]
                        # Search for extension match in fileCategories
                        for fileType, properties in fileCategories.items():
                            if fileExtension in properties['extensions']:
                                properties['fileCount'] +=1
                                createFolder(target_path, fileType)
                                oldPath = os.path.join(target_path, entry.name)
                                newPath = os.path.join(target_path, fileType, entry.name)
                                # Move file into appropriate folder
                                os.rename(oldPath, newPath)
                                properties['movedCount'] +=1
                # Display file(s) found and file(s) moved by fileCategory
                dictionarySummary(fileCategories)
        else:           
            print("Filepath doesn't exist")

    # --default
    if args.default:
        defaultBehavior()
    
def example_function():
    return 1 + 1

if __name__ == "__main__":
    main()
