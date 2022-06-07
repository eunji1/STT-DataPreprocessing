from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=nv-c4SoA4qE&list=PLInPGbDZkjSRJ2GN7Ba481NdJGifY_lvC&index=24")
url = "https://www.youtube.com/watch?v=hVMvzCIdAsg"
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()


# import os 
# import pytube # pip install pytube 
# from pytube.cli import on_progress 

# url = "https://www.youtube.com/watch?v=hVMvzCIdAsg" 

# yt = pytube.YouTube(url, on_progress_callback=on_progress)
# print(yt.streams) 

# yt.streams.filter(progressive=True, file_extension="mp4")\
#     .order_by("resolution")\
#     .desc()\
#     .first()\
#     .download()


# url = "https://www.youtube.com/watch?v=hVMvzCIdAsg"
# yt = YouTube(url)
# 	# youtube mp4로 (영상만)
#     # 영상+음원은 adaptive=True
# stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
# stream.download()