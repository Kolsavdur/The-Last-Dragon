from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    name = "The Last Dragon"
    version = "v1.08"
    author = "Kolsavdur"
    dependencies = ["MagmaLink"]

    def mod_load(self):
        ml = modinfo.get_mod("MagmaLink").import_ml() #Checks if MagmaLink is installed

        #Searches for Remy's last encounter, checks the line in which it will hook to during Remy's bad ending and hooks the mod if Lorem 3 is played and Remy received the PDA during Chapter 3
        ml.find_label("remy5") \
            .search_say("I don't think you realize what is at stake here. All the others you have met are dead", depth=800) \
            .hook_to("tld_day1", return_link=False, condition="lorem3unplayed==False and c4libraryavailable==False")


    def mod_complete(self):
        pass
