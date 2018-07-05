import bs4 as BeautifulSoup
from openedxtozim.utils import make_dir, dl_dependencies
import os
from slugify import slugify
class Html:
    is_video = False
    def __init__(self,json,path,rooturl,id,descendants,mooc):
        self.mooc=mooc
        self.json=json
        self.path=path
        self.rooturl=rooturl
        self.id=id
        self.folder_name = slugify(json["display_name"])
        self.output_path = os.path.join(self.mooc.output_path,self.path)
        make_dir(self.output_path)
        self.html=""

    def download(self,c):
        content=c.get_page(self.json["student_view_url"]).decode('utf-8')
        soup=BeautifulSoup.BeautifulSoup(content, 'html.parser')
        html_content=soup.find('div', attrs={"class": "edx-notes-wrapper"})
        if html_content== None:
            html_content=str(soup.find('div', attrs={"class": "course-wrapper"}))
        self.html=dl_dependencies(html_content,self.output_path, self.folder_name, c)

    def render(self):
            return self.html
