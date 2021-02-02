from AC_GUI import mainFrame
from datetime import datetime
from pathlib import Path
from playsound import playsound
import PIL
import csv
from datetime import datetime
import glob 
import os.path
import random
import schedule
import sys
import threading
import time
import wx



class Main(wx.Frame):
    def __init__(self, parent):
        mainFrame.__init__(self, parent)
        self.auds = []
        self.times = []
        self.stop_run_continuously = None
        
        self.loadAudioFiles()
        self.loadSchedule()
        
        from PIL import Image
        filename = r'res/Clock.png'
        img = Image.open(filename)
        img.save('res/Clock.ico')
        
        if hasattr(sys, "_MEIPASS"):
            ico_str = os.path.join(sys._MEIPASS, 'res/Clock.ico')
        else:
            ico_str = 'res/Clock.ico'

        ico = Path(ico_str)
        if ico.is_file():
            ico = wx.Icon(ico_str, wx.BITMAP_TYPE_ICO)
            self.SetIcon(ico)
        else:
            print("Ico File Not Found")

        self.Show(True)
        
    def run_continuously(self, interval=1):
        """Continuously run, while executing pending jobs at each
        elapsed time interval.
        @return cease_continuous_run: threading. Event which can
        be set to cease continuous run. Please note that it is
        *intended behavior that run_continuously() does not run
        missed jobs*. For example, if you've registered a job that
        should run every minute and you set a continuous run
        interval of one hour then your job won't be run 60 times
        at each interval but only once.
        """
        cease_continuous_run = threading.Event()

        class ScheduleThread(threading.Thread):
            @classmethod
            def run(cls):
                while not cease_continuous_run.is_set():
                    schedule.run_pending()
                    time.sleep(interval)

        continuous_thread = ScheduleThread()
        continuous_thread.start()
        return cease_continuous_run

    def loadAudioFiles(self):
        for mp3 in glob.glob('./audio/*.mp3'):
            self.auds.append(mp3)

        for wav in glob.glob('./audio/*.wav'):
            self.auds.append(wav)

        for aud in self.auds:
            print(aud)
        
        self.lbFiles.Clear()
        try:
            self.lbFiles.InsertItems(self.auds, 0)
        except:
            print("No Audio File Found")
            
    def loadSchedule(self):
        with open('clock_schedule.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            
            for row in csv_reader:
                self.times.append(row[0])
                print(row[0])
            # print(self.times)
        
        self.lbSchedule.Clear()        
        try:
            self.lbSchedule.InsertItems(self.times, 0)
        except:
            print("No Schedule Found")
            
    def play_random(self):
        rand = random.randrange(0, len(self.auds))
        self.lbFiles.SetSelection(rand)
        now = datetime.now()
        now_str = "{:02d}:{}".format(now.hour, now.minute)
        # print(now_str)
        if  now_str in self.times:
            self.lbSchedule.SetStringSelection(now_str)
        self.play_file(self.auds[rand])
    
    def FormDisable(self):
        # self.Disable()
        self.btnRandom.Disable()
        self.btnPlay.Disable()
        self.lbFiles.Disable()
        
    def FormEnable(self):
        wx.Yield() 
        # self.Enable()
        self.btnRandom.Enable()
        self.btnPlay.Enable()
        self.lbFiles.Enable()
    
    def play_file(self, aud):
        try:
            self.FormDisable()
            playsound(aud)
            print("{} - {}".format(datetime.now(), aud))
            self.FormEnable()
        except Exception as e:
            print(e)
            
    def DClickFile( self, event ):
        self.play_file(event.GetString())
     
    def ClickStart( self, event ):
        # print(event)
        if self.btnStart.GetLabel() == "Start":
            self.btnStart.SetLabel("Stop")
            self.FormDisable()
            
            for t in self.times:
                schedule.every().day.at(t).do(self.play_random)
                
            # Start the background thread
            self.stop_run_continuously = self.run_continuously()

            # Do some other things...
            # time.sleep(10)

        elif self.btnStart.GetLabel() == "Stop":
            
            self.btnStart.SetLabel("Start")
            schedule.clear()
            # Stop the background thread
            self.stop_run_continuously.set()
            self.FormEnable()
            
        self.btnStart.Layout()
        self.btnStart.Refresh()
        self.Layout()
        self.Refresh()
        
        
    def ClickPlay( self, event ):
        self.play_file(self.lbFiles.GetString(self.lbFiles.GetSelection()))
        
    def ClickRandom( self, event ):
        self.play_random()

if __name__ == "__main__":
    app = wx.App(False)
    frame = Main(None)
    app.MainLoop()
