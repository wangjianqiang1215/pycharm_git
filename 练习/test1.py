import requests
from bs4 import BeautifulSoup

# 创建一次性的会话对象
session = requests.Session()

# 定义请求头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
}

# 登录微博账号，获取Cookies信息
login_url = 'https://passport.weibo.com/login'
try:
    login_response = session.get(login_url)
    login_bs = BeautifulSoup(login_response.text, 'html.parser')
    vk_input = login_bs.select_one('input[name=vk]')['value']
    data = {
        'username': 'your_username',
        'password': 'your_password',
        'savestate': 1,
        'r': '',
        'ec': 0,
        'pagerefer': '',
        'entry': 'mweibo',
        'wentry': '',
        'loginfrom': '',
        'client_id': '',
        'code': '',
        'qq': '',
        'mainpageflag': 1,
        'hff': '',
        'hfp': '',
        'vt': '',
        'mss': '',
        'vk': vk_input,
        'remember': 1,
        'encoding': 'utf-8',
        'prelt': '60',
        'returntype': 'META',
    }
    session.post(login_url, data=data, headers=headers)
except Exception as e:
    print('登录微博失败！', e)

# 访问微博首页，获取评论
weibo_url = 'https://weibo.com'
try:
    response = session.get(weibo_url, headers=headers)
    bs = BeautifulSoup(response.text, 'html.parser')
    comments = bs.select('div.WB_text > span.ctt')
    for comment in comments:
        print(comment.text.strip())
except Exception as e:
    print('访问微博首页失败！', e)
