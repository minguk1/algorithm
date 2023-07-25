from pprint import pprint


movie = {"adult": False,
    "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
    "genre_ids": [
        18,
        80
    ],
    "id": 278,
    "original_language": "en",
    "original_title": "The Shawshank Redemption",
    "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
    "popularity": 67.931,
    "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
    "release_date": "1995-01-28",
    "title": "쇼생크 탈출",
    "video": False,
    "vote_average": 8.7,
    "vote_count": 18040}

def movie_info(movie):
    result_dict = {}
    for i in movie:
        if i in ["id", "title", "poster_path", "vote_average", "overview", "genre_is"]:
            result_dict[i] = movie.get(i)
    return result_dict

pprint(movie_info(movie))