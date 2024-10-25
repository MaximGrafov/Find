from googleapiclient.discovery import build

with open('ApiKey.txt', encoding='utf-8').read() as api_key:
    pass

with open('result.txt', 'w+', encoding='utf-8') as result_file:
    pass

youtube = build("YouTube", "v3", developerKey=api_key)





class GetData():
    
    def __init__(self):
        self.URLs = ['Xd_r2Z03vG8', 'chT-guufvzI', 'buipq8xnxy0']
        self.comments = []

    print(''.split())

    def counter(self):
        self.total_counter = 0
        self.total_counter += 1
        return f'{self.total_counter} видео есть нахуй!'
   
    def  get_comments(self):
    
        for url in self.URLs:

            response = youtube.commentThreads().list(
                part = 'snippet',
                videoId = url,
                maxResults = 100,
            ).execute()

            while response:

                for item in response['items']:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    self.comments.append(comment)

                if 'nextPageToken' in response:
                    response = youtube.commentThreads().list(
                        part = 'snippet',
                        videoId = url,
                        maxResults = 100,
                        pageToken = response['nextPageToken']
                    ).execute()
                else:

                    break

            

    
    


for comment in GetData.comments:
        result_file.write(comment + '\n')

print('end...')