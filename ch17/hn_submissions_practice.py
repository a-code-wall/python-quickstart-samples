import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from operator import itemgetter

# 执行API调用并存储响应
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
proxies = {'http': 'socks5://127.0.0.1:10808' , 'https': 'socks5://127.0.0.1:10808'}
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url, headers=headers, proxies=proxies, verify=False)

print("Status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
names, submission_dicts = [], []
for submission_id in submission_ids[:30]:
	# 对于每篇文章, 都执行一个API调用
	url = ('https://hacker-news.firebaseio.com/v0/item/' +
			str(submission_id) + '.json')
	submission_r = requests.get(url, headers=headers, proxies=proxies, verify=False)
	print(submission_r.status_code)
	response_dict = submission_r.json()

	names.append(response_dict['title'])

	submission_dict = {
		'label': response_dict['title'],
		'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
		'value': response_dict.get('descendants', 0)
	}

	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('value'),
							reverse=True)

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Most Active Discussions on Hacker News'
chart.x_labels = names

chart.add('', submission_dicts)
chart.render_to_file('hn_submissions_practice.svg')