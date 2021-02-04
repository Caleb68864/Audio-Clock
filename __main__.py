from AC_GUI import mainFrame
from AC_GUI import Dialog
from AC_GUI import audioDialog
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
from wx.lib.masked import TimeCtrl

class sheduleDialog(Dialog):
    def __init__(self, parent, title, rows):
        Dialog.__init__(self, parent)
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
        
        self.rows = rows

        self.timeSpin = wx.SpinButton(self,-1,style=wx.SP_VERTICAL)
        self.triggerTime = TimeCtrl(self,-1,format='24HHMM')
        self.triggerTime.BindSpinButton(self.timeSpin)
        
        self.GetSizer().GetItem(0).GetSizer().Add(self.triggerTime, 1, wx.ALL, 5 )
        self.GetSizer().GetItem(0).GetSizer().Add(self.timeSpin, 0, wx.EXPAND, 5 )
        self.SetTitle(title)
        
    def mdBtnAdd_Click( self, event ):

        self.rows.append(self.triggerTime.GetValue())
        self.rows.sort()
        # print(self.rows)
        # self.EndModal(self.rows)
        self.Close()
    
    def mdBtnCancel_Click(self, event):
        self.Close()

class audDialog(audioDialog):
    def __init__(self, parent, title, rows):
        audioDialog.__init__(self, parent)
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
        
        self.rows = rows

        # self.timeSpin = wx.SpinButton(self,-1,style=wx.SP_VERTICAL)
        # self.triggerTime = TimeCtrl(self,-1,format='24HHMM')
        # self.triggerTime.BindSpinButton(self.timeSpin)
        
        # self.GetSizer().GetItem(0).GetSizer().Add(self.triggerTime, 1, wx.ALL, 5 )
        # self.GetSizer().GetItem(0).GetSizer().Add(self.timeSpin, 0, wx.EXPAND, 5 )
        self.SetTitle(title)
        
    def mdBtnAdd_Click( self, event ):

        self.rows.append(self.fpAudio.GetPath())
        self.rows.sort()
        print(self.rows)
        # self.EndModal(self.rows)
        self.Close()
    
    def mdBtnCancel_Click(self, event):
        self.Close()
    
    
        


class Main(wx.Frame):
    def __init__(self, parent):
        mainFrame.__init__(self, parent)
        self.schedule_file = 'clock_schedule.csv'
        self.audio_file = 'clock_audio.csv'
        self.audio_dir = './audio'
        self.auds = []
        self.times = []
        self.stop_run_continuously = None
        
        # self.miAddTime.Enable(False)
        # self.miAddAudio.Enable(False)
        
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
        
        # for aud in self.auds:
            # print(aud)
        self.FormDisable()
        self.auds = []
        
        try:
            with open(self.audio_file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
            
                for row in csv_reader:
                    self.auds.append(row[0])
                    print(row[0])
        
        except:
            print("No Audio File Found")
            mp3s = glob.glob('{}/*.mp3'.format(self.audio_dir))
            wavs = glob.glob('{}/*.wav'.format(self.audio_dir))
            self.auds = mp3s + wavs
            file = open(self.audio_file, 'w+', newline ='') 
      
            with file:     
                write = csv.writer(file) 
                for row in self.auds:
                    write.writerow([row]) 
        # print(self.auds)
        self.lbFiles.Clear()
        self.lbFiles.InsertItems(self.auds, 0)
        self.FormEnable()
            
    def loadSchedule(self):
        self.FormDisable()
        self.times = []
        self.lbSchedule.Clear() 
        try:
            with open(self.schedule_file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                
                for row in csv_reader:
                    self.times.append(row[0])
                    print(row[0])
                # print(self.times)
            self.lbSchedule.InsertItems(self.times, 0)
        except:
            print("No Schedule Found")
            file = open(self.schedule_file, 'w+', newline ='') 
            with file:     
                write = csv.writer(file) 
                write.writerow(['']) 
            
        
        self.FormEnable()
            
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
        self.FormDisable()
        try:    
            playsound(aud)
            print("{} - {}".format(datetime.now(), aud))
            
        except Exception as e:
            print(e)
        self.FormEnable()
        
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
    
    def selReload(self, event):
        self.loadAudioFiles()
        self.loadSchedule()
    
    def selAddTime(self, event):
        atd = sheduleDialog(self, "Add Time", self.times)
        atd.ShowModal()
        # print(atd.rows)
        self.times = atd.rows
        file = open(self.schedule_file, 'w+', newline ='') 
      
        with file:     
            write = csv.writer(file) 
            for row in atd.rows:
                write.writerow([row]) 
        self.loadSchedule()
        atd.Destroy()
        
    def selRemoveTime(self, event):
        dlg = wx.MessageDialog(None, "Do you want to delete {}?".format(self.lbSchedule.GetString(self.lbSchedule.GetSelection())),'Delete Time',wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()

        if result == wx.ID_YES:
            # print("Yes pressed")
            try:
                self.lbSchedule.Delete(self.lbSchedule.GetSelection())
                rows = self.lbSchedule.GetStrings()
                # print(rows)
                file = open(self.schedule_file, 'w+', newline ='') 
      
                with file:     
                    write = csv.writer(file) 
                    for row in rows:
                        write.writerow([row]) 
                self.loadSchedule()
            except Exception as e:
                pass
        else:
            print("No pressed")
        

    def selAddFile(self, event):
        atd = audDialog(self, "Add Audio", self.auds)
        atd.ShowModal()
        # print(atd.rows)
        self.auds = atd.rows
        file = open(self.audio_file, 'w+', newline ='') 
      
        with file:     
            write = csv.writer(file) 
            for row in atd.rows:
                write.writerow([row]) 
        self.loadAudioFiles()
        atd.Destroy()
        
    def selRemoveFile(self, event):
        dlg = wx.MessageDialog(None, "Do you want to delete {}?".format(self.lbFiles.GetString(self.lbFiles.GetSelection())),'Delete Audio',wx.YES_NO | wx.ICON_QUESTION)
        result = dlg.ShowModal()

        if result == wx.ID_YES:
            # print("Yes pressed")
            try:
                self.lbFiles.Delete(self.lbFiles.GetSelection())
                rows = self.lbFiles.GetStrings()
                file = open(self.audio_file, 'w+', newline ='') 
      
                with file:     
                    write = csv.writer(file) 
                    for row in rows:
                        write.writerow([row]) 
                self.loadAudioFiles()
                        
            except Exception as e:
                pass
        else:
            print("No pressed")
        

if __name__ == "__main__":
    app = wx.App(False)
    frame = Main(None)
    app.MainLoop()