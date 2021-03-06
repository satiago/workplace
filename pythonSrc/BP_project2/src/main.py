from urllib import urlopen
from reportlab.lib import colors
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.textlabels import  Label
from reportlab.graphics.shapes import *

def test1_main():
    d = Drawing(100, 100)
    s = String(50, 50, 'BP_project2', textAnchor = 'middle')
    
    d.add(s)
    
    renderPDF.drawToFile(d, 'test_out.pdf', 'a simple PDF file')
    
def test2_main():
    data = [
        (2012,12,61.2,62.2,60.2),
        (2013,1,63.2,65.2,61.2),
        (2013,2,65.3,68.3,62.3),
        (2013,3,67.5,72.5,62.5),
        (2013,4,70.1,75.1,65.1),
        (2013,5,72.7,78.7,66.7),
        (2013,6,75.7,82.7,68.7),
        (2013,7,78.6,85.6,71.6),
        (2013,8,81.6,89.6,73.6),
        (2013,9,84.7,93.7,75.7)
        ]

    drawing = Drawing(4000, 150)
    
    pred = [row[2] - 40 for row in data]
    high = [row[3] - 40 for row in data]
    low = [row[4] - 40 for row in data]
    times = [200 * ((row[0] + row[1]/12.0) - 2007) -  110 for row in data]
    
    print(times)
    print(pred)
    print(high)
    
    drawing.add(PolyLine(zip(times, pred), strokeColor = colors.blue))
    drawing.add(PolyLine(zip(times, high), strokeColor = colors.red))
    drawing.add(PolyLine(zip(times, low), strokeColor = colors.green))
    drawing.add(String(65, 115, 'Sunspots', fontSize = 18, fillColor = colors.red))

    renderPDF.drawToFile(drawing, 'report.pdf', 'Sunspots')

def main():
    URL = 'http://www.swpc.noaa.gov/ftpdir/weekly/Predict.txt'
    COMMENT_CHARS = '#:'
    
    drawing = Drawing(400, 200)
    data = []
    
    for line in urlopen(URL).readlines():
        if not line.isspace() and not line[0] in COMMENT_CHARS:
            data.append([float(n) for n in line.split()])
            
    pred = [row[2] for row in data]
    high = [row[3] for row in data]
    low = [row[4] for row in data]
    times = [row[0] + row[1]/12.0 for row in data]
       
    lp = LinePlot()
    lp.x = 50
    lp.y = 50
    lp.height = 125
    lp.width = 300
    lp.data = [zip(times, pred), zip(times, high), zip(times, low)]
    lp.lines[0].strokeColor = colors.blue
    lp.lines[1].strokeColor = colors.red
    lp.lines[2].strokeColor = colors.green
    
    drawing.add(lp)
    
    drawing.add(String(250, 150, 'Sunspots', fontSize = 14, fillColor = colors.red))
    
    renderPDF.drawToFile(drawing, 'report.pdf', 'Sunspots')
    
     
if __name__ == '__main__':
    main()