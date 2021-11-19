""" importing packages
downloading youtube files
"""
import settings
from pytube import YouTube
from pytube import Playlist
import os
import re,time
import glob
import threading
from functions import music
import settings
class downtube:
    def __init__(self,file,save="musik\\storage"):
        self.file = file
        self.filename = []
        self.save = save
        self.queue = music.stats.queue
        self.index = music.stats.index
        self.i = 0
        self.down = []
        self.queuelist = glob.glob(settings.path+"musik\\storage\\*.mp3")

        self.playlistfiles = music.stats.playlistfiles
    async def downloader(self):
        #print([x[12:-4] for x in self.queuelist])
        try:
            myfile = Playlist(self.file)
            myfile._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

            for raw,file in enumerate(myfile.videos):
                self.down.append(threading.Thread(target=self.download,args=(file,raw,)))
                self.down[raw].start()
                try:
                    self.down[len(myfile.videos)].join()
                    music.stats.queuelistfiles = glob.glob(settings.path+"musik\\storage\\*.mp3")
                except:pass
            self.down[1].join()
        except:
            myfile = YouTube(self.file)

            if not myfile.title in [x[12:-4] for x in self.queuelist]:
                filename = myfile.streams.last().download(self.save,myfile.title+".mp3")
                music.stats.queue.append(filename)
                #self.convert(len(self.filename)-1)
            else:
                music.stats.queue.append(settings.path+"musik\\storage\\"+myfile.title+".mp3")
        #self.queue.extend([x[:-5]+".mp3" for x in self.filename])
        #print(self.queue,self.index)

        return music.stats.queue,self.index

    def download(self,title,raw):
        try:
            self.down[raw-1].join()
        except:pass
        try:


            if not title.title in [x[12:-4] for x in self.queuelist]:
                filename = title.streams.last().download(self.save,title.title+".mp3")
                print(filename)
                music.stats.queue.append(filename)
                #self.convert(len(self.filename)-1)
            else:
                music.stats.queue.append(settings.path+"musik\\queue\\"+title.title+".mp3")
        except:pass
    def convert(self,index):
        try:
            os.rename(self.filename[index], self.filename[index][:-5]+".mp3")
            if self.filename[index][:-5]+".mp3" not in music.stats.queue:
                music.stats.queue.extend(self.filename[index][:-5]+".mp3")
        except:
            os.remove(self.filename[index])
