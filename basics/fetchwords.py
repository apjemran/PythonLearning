'''
Created on 17-Sep-2020

@author: mohd.e.khan
'''

"""Retrieve and print words from a URL
   
   Usage:
   
   python3 fetchwords.py <URL>
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch list of words from URL
    
    Args:
        url: The URL of UTF-8 text document
    
    Returns:
        A list of string containing the words from the document.
           
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)      
    story.close()    
    return story_words

def print_items(items):
    
    """Print list of items
    
    Args:
        items: List of words               
    """
    for item in items:
        print(item)
        
def main(url):
    """Main function to fetch words from URL and then print those words
    
    Args:
        url: The URL of UTF-8 text document               
    """
    items = fetch_words(url)
    print_items(items)
    
if __name__ == '__main__':
    main(sys.argv[1])  # 0th Argument is always module file name
