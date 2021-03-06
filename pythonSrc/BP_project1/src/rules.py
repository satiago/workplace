class Rule:

    def action(self, block, handler, file):
        handler.start(self.type, file)
        handler.feed(block, file)
        handler.end(self.type, file)
        return True
    
class HeadingRule(Rule):
    
    type = "heading"
    
    def condition(self, block):
        return not "\n" in block and len(block) <= 70 and not block[-1] == ":"
    
class TitleRule(HeadingRule):
    
    type = "title"
    first = True
    
    def condition(self, block):
        if not self.first: 
            return False
        
        self.first = False
        return HeadingRule.condition(self, block)
    
class ListItemRule(Rule):
     
    type = "listitem"
    
    def condition(self, block):
        return block[0] == "-"
    
    def action(self, block, handler, file):
        handler.start(self.type, file)
        handler.feed(block[1:].strip(), file)
        handler.end(self.type, file)
        return True   
    
class ListRule(ListItemRule):
    
    type = 'list'
    
    inside = False
    
    def condition(self, block):
        return True
    
    def action(self, block, handler, file):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type, file)
            self.inside = True
            
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type, file)
            self.inside = False
            
        return False
    
class ParagraphRule(Rule):
    
    type = 'paragraph'
    
    def condition(self, block):
        return True
    
    
    
    
    
    
    
    
    
    
    
    