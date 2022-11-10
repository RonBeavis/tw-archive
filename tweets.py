#!c:/python36/python.exe

import json
import codecs

path_dir = 'D:/somecrazyblogger-org/twitter/norsivaeb/'
path_to_tweets = path_dir + 'tweets.js'
path_to_jsonlines = path_dir + 'tweet.jl'

print('reading lines')
lines = [l for l in codecs.open(path_to_tweets, encoding='utf-8')];
lines[0] = re.sub(r'.+?\[','[',lines[0])
code = ""
print('joining lines')
code = ''.join(lines)
print('json parsing lines')
js_t = json.loads(code)
js = []
print('reformating json')
for j in js_t:
	js.append(j['tweet'])
for j in js:
	j['iso'] = (dateutil.parser.parse(j["created_at"])).isoformat()
print('dumping tweet.jl')
jf = codecs.open(path_to_jsonlines, 'w', encoding='utf-8')

for j in sorted(js,key = lambda i: i['iso'],reverse=True):
	jf.write(json.dumps(j))
	jf.write('\n')
jf.close()


