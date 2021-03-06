from rules import *
import re


def lines(file):
    for line in file:
        yield line
        yield "\n"

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield " ".join(block).strip()
            block = []
            
class Parser:
    
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []
        
    def addRule(self, rule):
        self.rules.append(rule)
        
    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)
        
    def parse(self, infile, outfile):
        self.handler.start('document', outfile)
        for block in blocks(infile):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    if rule.action(block, self.handler, outfile):
                        break
        self.handler.end('document', outfile)
        
class BasicTextParser(Parser):
    
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')
        