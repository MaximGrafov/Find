from googleapiclient.discovery import build



api_key = open('ApiKey.txt', encoding='utf-8').read()

result_file = open('result.txt', 'w+', encoding='utf-8')

youtube = build("YouTube", "v3", developerKey=api_key)

URLs = ['Xd_r2Z03vG8', 'chT-guufvzI', 'buipq8xnxy0']

comments = []

print(''.split())
total_counter = 1

for url in URLs:

    response = youtube.commentThreads().list(
        part = 'snippet',
        videoId = url,
        maxResults = 100,
    ).execute()

    while response:

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        if 'nextPageToken' in response:
            response = youtube.commentThreads().list(
                part = 'snippet',
                videoId = url,
                maxResults = 100,
                pageToken = response['nextPageToken']
            ).execute()
        else:

            break

    print(total_counter, 'видео есть нахуй!')
    total_counter += 1

for comment in comments:
    result_file.write(comment + '\n')

print('end...')