import sys
import re
import util
import handlers
import rules
# import util 这种方式导入模块时函数前必须加模块名
# from util import * 这种方式导入时不需要

def main():
#     +符号保证文件不存在时可以创建
    outfile = open("text_out.html", 'w+')
#     outfile.write('<html><head><title>...</title></head><body>')
    
    infile = open("text_input.txt", "r")
    
    handler = handlers.HTMLRenderer()
    parser = util.BasicTextParser(handler)
    
    parser.parse(infile, outfile)
#     title = True
#     
#     for block in util.blocks(infile):
# #     for block in blocks(infile):
# # \1为组号，匹配字符串中的第一组字符串
#         block = re.sub(r"\*(.+?)\*", r"<em>\1</em>", block)
#         if title:
#             outfile.write("<h1>")
#             outfile.write(block)
#             outfile.write("</h1>")
#             title = False
#             
#         else:
#             outfile.write("<p>")
#             outfile.write(block)
#             outfile.write("</p>")
#             
#     outfile.write("</body></html>")
            
    outfile.close()
    infile.close()

if __name__ == "__main__":
    main()
    