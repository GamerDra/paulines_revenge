import webbrowser
"""Oh yeah! Mario time!"""

def main(slice=1):
    urls = [
        'https://r.mtdv.me/videos/314mMJGmMl',
        'https://en.wikipedia.org/wiki/Digital_object_identifier',
        'https://r.mtdv.me/articles/RxP-Bn9nuW',
        'https://r.mtdv.me/watch?v=uCBw5tZwyZ',
        'https://r.mtdv.me/videos/314mMJGmMl'
    ]


    for url in urls[0:slice]:
        webbrowser.open(url)

if __name__ == "__main__":
    main(5)