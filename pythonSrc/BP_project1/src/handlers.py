class Handler:
    
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)
        
    def start(self, name, outfile):
        self.callback("start_", name, outfile)
    
    def end(self, name, outfile):
        self.callback("end_", name, outfile)
        
    def sub(self, name):
        def substitution(match):
            result = self.callback("sub_", name, match)
            if result is None:
                result = match.group(0)
            return result
        return substitution
    
class HTMLRenderer(Handler):
    
    def start_document(self, file):
        file.write("<html><head><title>...</title></head><body>")
        
    def end_document(self, file):
        file.write("</body></html>")
        
    def start_paragraph(self, file):
        file.write('<p>')
        
    def end_paragraph(self, file):
        file.write('</p>')
        
    def start_heading(self, file):
        file.write('<h2>')
        
    def end_heading(self, file):
        file.write('</h2>')
        
    def start_list(self, file):
        file.write('<ul>')
        
    def end_list(self, file):
        file.write('</ul>')
        
    def start_listitem(self, file):
        file.write('<li>')    
        
    def end_listitem(self, file):
        file.write('</li>')
        
    def start_title(self, file):
        file.write('<h1>')
        
    def end_title(self, file):
        file.write('</h1>')
        
    def sub_emphasis(self, match):
        return "<em>%s</em>" % match.group(1)
           
    def sub_url(self, match):
        return "<a href='%s'>%s</a>" % (match.group(1), match.group(1))
            
    def sub_mail(self, match):
        return "<a href='mailto:%s'>%s</a>" % (match.group(1), match.group(1))
            
    def feed(self, data, file):
        file.write(data)