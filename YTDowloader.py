#Transfer required libraries
import pytube
import os
from enum import IntEnum 

#Selection menu with the option to choose the file type and its Itag
Selection_Menu_1 = IntEnum("Selection Menu 1", {"Mp4": 1, "Mp3": 2})
Selection_Menu_2 = IntEnum("Selection Menu 2", {"Choice_18": 18, "Choice_22": 22, "Choice_137": 137, "Choice_394": 394})
Selection_Menu_3 = IntEnum("Selection Menu 3", {"Choice_140": 140, "Choice_249": 249, "Choice_250": 250, "Choice_251": 251})

#The program checks if the link and the choices made by the user are correct. If not, the program will display "Invalid input. Please try again"
try:
    #Here the user enters the link to the video
    link = input("Enter YT video link: ")
    print()

    #Here the user selects where the downloaded file will be located
    Dir = input("Enter the path of the downloaded file: ")
    print()

    #Here the user selects the format in which the file should be downloaded
    choice1 = int(input("In what type of file do you want this video to be downloaded? \n1-Mp4 2-Mp3 "))
    print()

    #Depending on the previous file format selection, the program shows further details of the downloaded file (resolution, frame rate, vcodec, acodec and file type)
    if choice1==Selection_Menu_1.Mp4:
        print("18 - video/mp4, res-360p, fps-30, vcodec- avc1.42001E, acodec- mp4a.40.2, type- video")
        print("22- video/mp4, res-720p, fps-30 vcodec- avc1.64001F, acodec- mp4a.40.2, type- video")
        print("137- video/mp4, res-1080p, fps-30 vcodec- avc1.640028, type- video")
        print("394- video/mp4, res-None, fps-30 vcodec- avc1.640028, type- audio")
        print()

        #Here the user selects the format in which the file should be downloaded (in this case mp4)
        choice2 = int(input("Which option do you choose? "))

        if choice2==Selection_Menu_2.Choice_18:
            print()
            print("Downloading...")
            yt = pytube.YouTube(link)
            stream = yt.streams.get_by_itag(18) #The program downloads the video according to the user's choice along with itag from the pytube documentation
            Dir2 = stream.download(output_path = Dir) #The user indicates the appropriate path
            os.path.join(Dir2) #The operation of adding a file to the path selected by the user takes place here e.g .: C:\Users\marek\Desktop
            print("Your yt video has been successfully downloaded.")

        elif choice2==Selection_Menu_2.Choice_22:
            print()
            print("Downloading...")
            yt = pytube.YouTube(link)
            stream = yt.streams.get_by_itag(22)
            Dir2 = stream.download(output_path = Dir)
            os.path.join(Dir2)
            print("Your yt video has been successfully downloaded.")

        elif choice2==Selection_Menu_2.Choice_137:
            print()
            print("Downloading...")
            yt = pytube.YouTube(link)
            stream = yt.streams.get_by_itag(137)
            Dir2 = stream.download(output_path = Dir)
            os.path.join(Dir2)
            print("Your yt video has been successfully downloaded.")

        elif choice2==Selection_Menu_2.Choice_394:
            print()
            print("Downloading...")
            yt = pytube.YouTube(link)
            stream = yt.streams.get_by_itag(394)
            Dir2 = stream.download(output_path = Dir)
            os.path.join(Dir2)
            print("Your yt video has been successfully downloaded.")

        else:
            print("Invalid input. Please try again.")

    #Depending on the previous file format selection, the program shows further details of the downloaded file (resolution, frame rate, vcodec, acodec and file type)
    elif choice1==Selection_Menu_1.Mp3:
        print("140 - audio/mp4, abr=128kbps, acodec- mp4a.40.2, type- audio")
        print("249 - audio/webm, abr=50kbps, acodec- opus, type- audio")
        print("250 - audio/webm, abr=70kbps, acodec- opus, type- audio")
        print("251 - audio/webm, abr=160kbps, acodec- opus, type- audio")
        print()

        #Here the user selects the format in which the file should be downloaded (in this case audio/mp3)
        choice2 = int(input("Which option do you choose? "))

        if choice2==Selection_Menu_3.Choice_140:
            print()
            print("Downloading...")
            yt = pytube.YouTube(link)
            stream = yt.streams.get_by_itag(140)
            DownloadedMp3 = stream.download(output_path = Dir)
            os.path.join(DownloadedMp3)
            base, ext = os.path.splitext(DownloadedMp3)
            NewMp3 = base + ".mp3"
            os.rename(DownloadedMp3, NewMp3) #Here the file extension from webm is replaced with audio (mp3)
            print("Your yt video has been successfully downloaded.")

        elif choice2==Selection_Menu_3.Choice_249:
            print()
            print("Downloading...")
            yt = pytube.YouTube(link)
            stream = yt.streams.get_by_itag(249)
            DownloadedMp3 = stream.download(output_path = Dir)
            os.path.join(DownloadedMp3)
            base, ext = os.path.splitext(DownloadedMp3)
            NewMp3 = base + ".mp3"
            os.rename(DownloadedMp3, NewMp3)
            print("Your yt video has been successfully downloaded.")

        elif choice2==Selection_Menu_3.Choice_250:
            print()
            print("Downloading...")
            yt = pytube.YouTube(link)
            stream = yt.streams.get_by_itag(250)
            DownloadedMp3 = stream.download(output_path = Dir)
            os.path.join(DownloadedMp3)
            base, ext = os.path.splitext(DownloadedMp3)
            NewMp3 = base + ".mp3"
            os.rename(DownloadedMp3, NewMp3)
            print("Your yt video has been successfully downloaded.")

        elif choice2==Selection_Menu_3.Choice_251:
            print()
            print("Downloading...")
            yt = pytube.YouTube(link)
            stream = yt.streams.get_by_itag(251)
            DownloadedMp3 = stream.download(output_path = Dir)
            os.path.join(DownloadedMp3)
            base, ext = os.path.splitext(DownloadedMp3)
            NewMp3 = base + ".mp3"
            os.rename(DownloadedMp3, NewMp3)
            print("Your yt video has been successfully downloaded.")
            
        else:
            print("Invalid input. Please try again.")
    else:
        print("Invalid input. Please try again.")
except:
    print("Invalid input. Please try again.")