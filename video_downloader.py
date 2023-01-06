from pytube import YouTube

#downloads the given links and
def Download(link):
  video = YouTube(link)
  video = video.streams.get_highest_resolution()
  try:
      video.download("videos")
  except:
    print("There has been an error in downloading your youtube video")
  print("This download has completed!")

def scan_txt_file():
    with open("download.txt", "r") as file:
      for link in file:
          Download(link)

print("Welcome to the Youtube Downloader\nEnter the number of the option you would like to choose\n")
choice = int(input("1). Give a video link to download single video\n2). Download all videos in download.txt\n"))
if choice == 1:  
  link = input("Put your youtube link here!! URL: ")
  Download(link)
elif choice == 2:
    scan_txt_file()



          