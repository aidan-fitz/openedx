
#import bs4 as BeautifulSoup
from openedxtozim.utils import make_dir, jinja
import os
from slugify import slugify

class GradeMeButton:
    def __init__(self,json,path,rooturl,id,descendants,mooc):
        self.mooc=mooc
        self.json=json
        self.path=path
        self.rooturl=rooturl
        self.id=id
        self.is_video=True
        self.output_path=self.mooc.output_path
        self.folder_name = slugify(json["display_name"])
        self.output_path = os.path.join(self.mooc.output_path,self.path)
        make_dir(self.output_path)

    def download(self, c):
      return

    def render(self):
            return "Grade Me ! ; Not available offline" #TODO loca, to bettter
