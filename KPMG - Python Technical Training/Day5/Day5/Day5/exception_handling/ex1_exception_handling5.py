def main(filename):
    try :
        for line in readfile(filename):
            print(line.strip())
    except IOError as o:
        print(o.__class__.__name__," Msg:- ",o)
        gh=open('demo.txt','r')
        for line in gh:
            print(line.strip())
    except ValueError as v:
        print(v,"Ext. should be .txt")  
    
    except Exception as e:
        print("Error Handled!")
        print("Error NAme:-",e.__class__.__name__)
        print("Error Msg:-",e)

def readfile(filename):
    if filename.endswith(".txt"):
        fh=open(filename)
        return fh 
    else:
        raise ValueError("Bad Ext.")
    
main("lines.pdf")