from stanford_parser.parser import Parser

def analyze_likes(t):

    #get subject from tweet
    stanford_parser = Parser()

    dependencies = stanford_parser.parseToStanfordDependencies(t)

    print "\nDone parsing. REturned value:\n"
    print dependencies

if __name__=='__main__':
    analyze_likes()
