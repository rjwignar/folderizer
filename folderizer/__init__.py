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

def main():
    images = [".jpeg", ".jpg", ".png", ".gif"]
    videos = [".mp4", ".flv", ".m4v", ".webm"]
    text = [ ".txt", ".md", ".doc", ".docx", ".pdf"]
    imageCount = 0
    movedImagesCount = 0
    videoCount = 0
    movedVideosCount = 0
    textCount = 0
    movedTextFilesCount = 0

    parser = argparse.ArgumentParser(
        prog="folderizer",
        description="File organization command-line tool.",
        epilog="Thanks for using %(prog)s!")
    parser.add_argument('filepath')
    parser.add_argument("-v","--version", action="version", version="%(prog)s 0.1.1")
    parser.add_argument("-d", "--default", action='store_true', help="Sorts files into folders by category (image, video, text, code, etc)")
    args = parser.parse_args()
    print(args, args.filepath, args.default)
    if args.default:
        print("Default behaviour")
        print(os.path.abspath(args.filepath))
        target_path = os.path.abspath(args.filepath)
        print("Target Path: " + target_path)
        if (os.access(target_path, os.F_OK)):
            print("Filepath exists")
            print(os.scandir(target_path))
            with os.scandir(target_path) as it:
                for entry in it:
                    if not entry.name.startswith('.') and entry.is_file():
                        print("Entry name: " + entry.name)
                        print(os.path.splitext(entry.name)[1])
                        if os.path.splitext(entry.name)[1] in images:
                            imageCount+=1
                            folderPath = createFolder(target_path, "images")
                            # move file to images folder
                            print("Image file name: " + entry.name)
                            print(entry)
                            oldPath = target_path + "\\" + entry.name
                            newPath = folderPath + "\\" + entry.name
                            print("old filepath: " + oldPath)
                            print("new filepath: " + newPath)
                            # attempt rename
                            os.rename(oldPath, newPath)
                            movedImagesCount+=1
                        elif os.path.splitext(entry.name)[1] in videos:
                            videoCount+=1
                            folderPath = createFolder(target_path, "videos")
                            # move file to videos folder
                            print("Video file name: " + entry.name)
                            print(entry)
                            oldPath = target_path + "\\" + entry.name
                            newPath = folderPath + "\\" + entry.name
                            print("old filepath: " + oldPath)
                            print("new filepath: " + newPath)
                            # attempt rename
                            os.rename(oldPath, newPath)
                            movedVideosCount+=1
                        elif os.path.splitext(entry.name)[1] in text:
                            textCount+=1
                            folderPath = createFolder(target_path, "textFiles")
                            # move file to videos folder
                            print("Text file name: " + entry.name)
                            print(entry)
                            oldPath = target_path + "\\" + entry.name
                            newPath = folderPath + "\\" + entry.name
                            print("old filepath: " + oldPath)
                            print("new filepath: " + newPath)
                            # attempt rename
                            os.rename(oldPath, newPath)
                            movedTextFilesCount+=1
                print('------------------------------------')
                print('SUMMARY')
                print('------------------------------------')
                print('Images found: ',imageCount)
                print('Images successfully moved: ', movedImagesCount)
                print('Videos found: ',videoCount)
                print('Videos successfully moved: ', movedVideosCount)
                print('Text files found: ',textCount)
                print('Text files successfully moved: ', movedTextFilesCount)
        else:           
            print("Filepath doesn't exist")
def example_function():
    return 1 + 1

if __name__ == "__main__":
    main()
