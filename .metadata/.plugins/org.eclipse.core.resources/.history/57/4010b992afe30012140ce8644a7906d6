class Handler:
    
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)
        
    def start(self, name):
        self.callback("start_", name)
    
    def end(self, name):
        self.callback("end_", name)
        
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
        file.write()
        
    def end_paragraph(self, file):
        file.write()
        
    def start_heading(self, file):
        file.write()
        
    def end_heading(self, file):
        file.write()
        
    def start_list(self, file):
        file.write()
        
    def end_list(self, file):
        file.write()
        
    def start_listitem(self, file):
        file.write()    
        
    def end_listitem(self, file):
        file.write()
        
    def start_title(self, file):
        file.write()
        
    def end_title(self, file):
        file.write()
        
    def sub_emphasis(self, match):
        return "<em>%s</em>" % match.group(1)
           
    def sub_url(self, match):
        return "<a href='%s'>%s</a>" % (match.group(1), match.group(1))
            
    def sub_mail(self, match):
        return "<a href='mailto:%s'>%s</a>" % match.group(1)
            
    def feed(self, data, file):
        file.write(data)