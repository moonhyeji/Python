from wordcloud import WordCloud
import json

cloud = WordCloud(font_path='Goyang.otf', background_color='white', max_words=30, width=400, height=300)
#폰트는 mac에서는 otf, window는 ttf 파일을 visul package아래에 넣어준다. wordcloud가 한글은 인코딩 못하기 때문에 폰트를 지정해준다.

with open('webtoons.json', encoding='utf-8') as file:
    webtoon = json.load(file)
    
    
res = dict()
for wt in webtoon['webtoons']:
    res[wt['title']] = int(float(wt['star'])*100)  #9.97을 997로 바꿔서 크기가 더 구분 잘되도록 함.
    
visual = cloud.fit_words(res)
visual.to_image()
visual.to_file('cloud.png')  #그림으로 저장 



#preferencies → python interpreter → new→ Browse for python/pypy exe →usr/local/anaconda3/envs/aitest/bin/python3 넣어서 python3을 위로 올려주고,

#python02 를 실행하고 , 패키지에서 새로고침 해주면 webtoons.json 이생성됨.생성된 webtoons.json 을 복해서 visual패키지않에 넣어주고, word01.py실행 

#실행 하면 visual 패키지 아래에 cloud.png 가 생성된다. 생성된 것을 열어보면 별점순이 높은대로 크키가 크게 지정되어서 나타나는 것을 알 수 있다.




