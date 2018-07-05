import bs4 as BeautifulSoup
from openedxtozim.utils import make_dir, jinja, download
import os
from slugify import slugify

class Lti:
    def __init__(self,json,path,rooturl,id,descendants,mooc):
        self.mooc=mooc
        self.json=json
        self.path=path
        self.rooturl=rooturl
        self.id=id
        self.is_video=True
        self.folder_name = slugify(json["display_name"])
        self.output_path = os.path.join(self.mooc.output_path,self.path)
        make_dir(self.output_path)

    def download(self, c):
        #TODO LTI can be lot of contnt type ? Here pdf, + utiliser le code du formulaire POST html + voir le code du xblock LTI
        url = self.json["lms_web_url"].replace("/jump_to/","/xblock/") + "/handler/preview_handler"
        print(url)
        content=c.get_page(url).decode('utf-8')
        soup=BeautifulSoup.BeautifulSoup(content, 'html.parser')
        content_url=soup.find('form')
        download(content_url["action"],os.path.join(self.output_path,"content.pdf"),c)

    def render(self):
            return "<p> This content can be download <a href='{}'> here </a>".format(os.path.join(self.folder_name,"content.pdf")) #TODO loca + do better