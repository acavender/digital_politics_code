# Code and instructions from https://colab.research.google.com/drive/1VyWXq_RAqeq-6UIiiM-3vpyKpIozKvsL?usp=sharing#scrollTo=LtIh5Yr57Zs8 and https://www.scrapingbee.com/blog/python-wget/.

# For passing a variable as a URL, I found good information at https://askubuntu.com/questions/351093/how-to-pass-url-as-variable-to-wget.

import subprocess
import os
from sys import prefix

def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE, 
        stderr = subprocess.PIPE,
        text = True, 
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

pdfs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# pdfs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
docnum = 1

while docnum <= len(pdfs):
    base_url = 'https://amycavender.org/pdf_demo/'
    url_plus = str(docnum) + ".pdf"
    url_final = base_url + url_plus
    os.system('wget %s -P downloaded_pdfs' %url_final)
    print("Downloaded file " +str(docnum)+ ".pdf.")
    docnum += 1


