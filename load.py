from datetime import datetime
from playsound import playsound
from config import config
import os, sys, urllib

def plugin_start(plugin_dir):
   """
   Load this plugin into EDMC
   """
   print("EDSM System Checker as been loaded in the plugin folder {}").format(plugin_dir.encode("utf-8"))
   return "EDSM System Checker"

def plugin_stop():
    """
    EDMC is closing
    """

def journal_entry(cmdr, is_beta, system, station, entry, state):
   if entry['event'] == 'FSDTarget':
      request = urllib.urlopen('https://www.edsm.net/api-v1/system?systemName=' + entry['Name'])
      resulttext = request.read()
      text = resulttext.decode(encoding='utf-8',errors='ignore')

      if text == '[]' :
         print("We didn't find:" + entry['Name'])
         LogUnregisteredSystem(entry['Name'])
         playsound(os.path.join(os.path.dirname(os.path.realpath(__file__)), "Unregistered_System.mp3"))
      else :
         print("We found:" + entry['Name'])
         playsound(os.path.join(os.path.dirname(os.path.realpath(__file__)), "Registered_System.mp3"))
             
def LogUnregisteredSystem(systemName):
      fileName = os.path.join(os.path.dirname(os.path.realpath(__file__)), "UnregisteredSystems_" + datetime.now().strftime("%d%m%Y") + ".txt")
      logEntry = datetime.now().strftime("%d-%m-%Y_%H:%M:%S | \"") + systemName + "\"\n"
      with open(fileName, "a") as myfile: myfile.write(logEntry)