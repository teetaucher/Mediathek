import re

sendungen = []
reTime1 = re.compile('VIDEO, (\d+):(\d+)')
reTime2 = re.compile('VIDEO, (\d+) min')

def unifyTime(strTime):
	t1 = reTime1.match(strTime)
	if t1:
		return (int(t1.group(1)),int(t1.group(2)))  
	t2 = reTime2.match(strTime)
	if t2:
		return (int(t2.group(1)), 0)
	return

with open('links.txt', 'r') as f:
	for l in f.readlines():
		vId, vTitle, vDur = l.split(';')
		sendungen.append(
				{
					'id' : vId, 
					'title' : vTitle,
					'dur' : unifyTime(vDur)
				}
			)
# als map
echteSendungen = [s['title'] for s in sendungen if s['dur'][0] > 30]
for e in echteSendungen:
	print e