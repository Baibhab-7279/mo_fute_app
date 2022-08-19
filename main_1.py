from datetime import date
from datetime import datetime
import os
from kivymd.app import MDApp
import pandas as pd
from matplotlib import pyplot as plt
#from kivy.config import Config
#from kivymd.uix.label import Label
#from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.tabbedpanel import TabbedPanel
#from kivy.garden.matplotlib import FigureCanvasKivyAgg


Window.size = (288,560)




#Config.set("graphics","resizable","0")

#Config.set("graphics","height","560")
#Config.set("graphics","width","257")

class reader:
    def __init__(self,total):
        self.rt_1 = total
        self.rd_1 = str(date.today())

    def r_d1(self):
        self.pa = "kivy_python/data_kivy/data_app.txt"
        self.b1 = os.path.exists(self.pa)
        if(self.b1):
            self.t1 = open(self.pa,"a")
            self.t1.write(f"\n{self.rd_1},{self.rt_1}")
            self.t1.close()
        else:
            self.t2 = open(self.pa,"w")
            self.t2.write(f"date,total")
            self.t2.close()
            self.t3 = open(self.pa,"a")
            self.t3.write(f"\n{self.rd_1},{self.rt_1}")
            self.t3.close()
    def r_d2(self):
        #now = datetime.now()
        self.d1 = pd.read_csv("kivy_python/data_kivy/data_app.txt")
        self.d2 = list(self.d1.loc[:,"total"])
        self.d3 = list(self.d1.loc[:,"date"])
        #checking any graph file is there or not
        self.pa_1 = "kivy_python/graph_kivy/graph_app.jpg"
        #self.file_name = f"graph_{now.hour}-{now.minute}-{self.rd_1}.jpg"
        #self.ma_pa = os.path.join(self.pa_1,self.file_name)
        #print(self.ma_pa)
        plt.xlabel("date")
        plt.ylabel("total amount")
        plt.plot(self.d3,self.d2)
        self.b2 = os.path.exists(self.pa_1)
        if(self.b2):
            os.remove(self.pa_1)
            plt.savefig(self.pa_1)
        else:
            plt.savefig(self.pa_1)
    


class Sec1(TabbedPanel):
    pass
class LoginScreen(Screen):
    def acces_1(self,instance):
        self.manager.current = "sec"
    
    def submit_b1(self):
        self.o1 = pd.read_csv("kivy_python\login.txt")
        self.user_name = self.ids.User_name.text
        self.user_passwod = self.ids.Password.text
        self.user_list = list(self.o1.loc[:,"name"])
        self.password_list = list(map(str,self.o1.loc[:,"password"]))
        #print(type(self.password_list[0]))
        #self.bbo_1 = False
        
        if(self.user_name in self.user_list):
            if(self.password_list[self.user_list.index(self.user_name)] == self.user_passwod):
                self.ids.Replay.text = "welcome to mo-fute"
                self.ids.Replay.color = (0,1,0,1)
                self.ids.Submit_button.bind(on_release = self.acces_1)

                        
            else:
                self.ids.Replay.text = "data is incorrect"
                self.ids.Replay.color = (1,0,0,1)
                #self.ids.Submit_button.disabled = "True"

        else:
            self.ids.Replay.text = "data is incorrect"
            self.ids.Replay.color = (1,0,0,1)    

           

    

class SecScreen(Screen):
    def Se_bu1(self):
        #print(self.ids)
        self.am1 = int(self.ids.am_1.text)
        self.am2 = int(self.ids.am_2.text)
        self.am3 = int(self.ids.am_3.text)
        self.am4 = int(self.ids.am_4.text)
        self.am5 = int(self.ids.am_5.text)

        self.t1 = str(self.am1+self.am2+self.am3+self.am4)
        self.ids.total.text = self.t1
        reader(self.t1).r_d1()
        #reader(self.t1).r_d2()
        #self.pa_2 = "kivy_python/graph_kivy/graph_app.jpg"
        #now = datetime.now()
        #self.r_d1 = str(date.today())
        #self.pa_2 = "kivy_python/graph_kivy/"
        #self.file_name_1 = f"graph_{now.hour}-{now.minute}-{self.r_d1}.jpg"
        #self.ca_fi = os.path.join(self.pa_2,self.file_name_1)
        #print(self.ca_fi)
        #self.ids.graph_ima_1.source = self.pa_2 
        #print(f"your name is:- {type(self.name)}\nregestration no:-{self.reg_no}\namount1:- {self.am1}\namount2:- {type(self.am2)}\namount3:- {self.am3}\namount4:- {self.am4}\ntotal= {type(self.t1)}")
        #self.re1 = reader(self.name,self.reg_no,self.t1)
        #self.re1.d_r()
        #self.re1.gr_d() 
        #self.ids.graph_ima_1.source = "kivy_python/graph_kivy/data_graph.jpg"
    def Se_bu2(self):
        self.t2 = self.ids.total.text
        reader(self.t2).r_d2()
        self.ids.graph_ima_1.source = "kivy_python/graph_kivy/graph_app.jpg"
        self.ids.graph_ima_1.reload()

        



sm = ScreenManager()
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(SecScreen(name="sec"))



class TrailApp(MDApp):
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Red"
        #return(Builder.load_file("trail.kv"))

#    def submit_b1(self):
#        self.o1 = pd.read_csv("kivy_python\login.txt")
#        self.user_name = self.root.ids.User_name.text
#        self.user_passwod = self.root.ids.Password.text
#        self.user_list = list(self.o1.loc[:,"name"])
#        self.password_list = list(map(str,self.o1.loc[:,"password"]))
#        print(type(self.password_list[0]))
#        
#        if(self.user_name in self.user_list):
#            if(self.password_list[self.user_list.index(self.user_name)] == self.user_passwod):
#                self.root.ids.Replay.text = "welcome to mo-fute"
#                self.root.ids.Replay.color = (0,1,0,1)

        
#        else:
#            self.root.ids.Replay.text = "data is incorrect"
#            self.root.ids.Replay.color = (1,0,0,1)




if(__name__ == "__main__"):
    TrailApp().run()


#default username = baibhab password = 5816 username1= krupasindhu password = 9437
