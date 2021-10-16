#!/usr/bin/env python
import json
import argparse

def gen_folder(data):
        return f'<DT><H3>{data}</H3>\n'
        
def gen_bmark(data):
            return f'<DT><A HREF="{data.get("url")}" ADD_DATE="{data.get("ts_created")}"">{data.get("title")}</A>\n'

def convert(filename_input, filename_output):
    page = '''
        <!DOCTYPE NETSCAPE-Bookmark-file-1>
        <!--This is an automatically generated file.
            It will be read and overwritten.
            Do Not Edit! -->
        <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
        <TITLE>Bookmarks</TITLE>
        <H1>Bookmarks</H1>
        <DL><p>
        <DT><H3 PERSONAL_TOOLBAR_FOLDER="true">Bookmarks</H3>
        <DL><p>
        '''
    try:
        with open(filename_input, "r") as f:
            data=json.load(f)
        # HomeScreen
        data["groups"].append({"id": 0, "title": "Home"})
        for i in data.get("groups"):
            page += gen_folder(i.get("title"))
            page += "<DL><p>\n"
            for _i in data.get("dials"):
                if _i.get("idgroup") == i.get("id"):
                    page += gen_bmark(_i)
            page += "</DL><p>\n"
        page += "</DL><p>\n"
        with open(f"{filename_output}.html", "w") as f:
            f.write(page)
    except Exception as e:
        print(Exception, e)
    
def main():
  parser = argparse.ArgumentParser(description = "Convert Speed Dial 2 Format to the Netscape Bookmark File Format.")
  parser.add_argument('input_file', help = "Speed Dial 2 .dms file to convert")
  parser.add_argument('output_file', help = "Output *.html file")
  parser.add_argument('--verbose', '-v', action='store_true', default=False)
  options = parser.parse_args()
  convert(options.input_file, options.output_file)


if __name__ == '__main__':
  main()