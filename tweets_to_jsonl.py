# converts the JSON tweet archive file tweets.js into
# JSON-lines format file tweet.jl

import json
import re
from dateutil import parser
import codecs

# set these paths to what you want for your installation
PATH_TO_JS = 'D:/somecrazyblogger-org/twitter/norsivaeb/tweets.js'
PATH_TO_JL = 'D:/somecrazyblogger-org/twitter/norsivaeb/tweet.jl'

#read JSON into an array
print('reading lines')
lines = [l for l in codecs.open(PATH_TO_JS, encoding='utf-8')];
#clean up non JSON characters in first line
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
	j['iso'] = (parser.parse(j["created_at"])).isoformat()
print('dumping tweet.jl')
jf = codecs.open(PATH_TO_JL, 'w', encoding='utf-8')
tws = 0
for j in sorted(js,key = lambda i: i['iso'],reverse=True):
	jf.write(json.dumps(j))
	jf.write('\n')
	tws += 1
jf.close()
print('Tweets = %i' % (tws))
