import urllib.request, urllib.error, urllib.parse
import sys
import io

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan 
def clone():
    print((''+T+'Remember to put https:// in front of the website!'))
    hey = input(''+T+'' + color.UNDERLINE + 'Website>' + color.END)
    response = urllib.request.urlopen(hey)
    page_source = response.read()

    with io.FileIO("websitesource.html", "w") as file:
        file.write(page_source)
    print((''+G+'[*] Finished!'))