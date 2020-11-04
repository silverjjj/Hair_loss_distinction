'''
크롤링 코드
'''
from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"o형탈모","limit":1000,"print_urls":True,"format":"jpg","chromedriver":"C:/Users/multicampus/Downloads/chromedriver_win32/chromedriver.exe"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images