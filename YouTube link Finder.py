Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [DEBUG ON]
>>> def extract_video_id(url):
...     #Check if the URL is in the full format
...     if "youtube.com/watch" in url:
...         #Split the URL using "?" as a delimiter and get the second part
...         params = url.split("?")[1]
...         #Split the parameters using "&" as a delimiter
...         param_list =params.split("&")
...         for param in param_list:
...             if param.startswith("v="):
...                 #Extract and return the video ID
...                 return param[2:]
... 
...             
>>> [DEBUG ON]
>>>    #If not inthe full format, check for the shortened format
   if "youtu.be/" in url:
...        #Split the URLusing "/" as a delimiter and get the last part
...        parts = url.split("/")
...        return parts[-1]
...     #If the URL format is not recognized, return an error message
...     return "Invalid YouTube URL format"
... #Input Youtube URL as a string
... url_input input()
... 
... #Get and print the video ID
... video_id = extract_video_id(url_input)
... []
... 
