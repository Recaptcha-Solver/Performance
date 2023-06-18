import os, json

label = {} # 레이블 : 나온 횟수
result = [] # 레이블 별로 걸린 시간 저장할 리스트

cnt = 1
while cnt <= 55:
    with open(f'./file/{cnt}.json', 'r') as rf:
        json_data = json.load(rf)
        for data in json_data:
            # 나온 레이블의 개수
            if data['title'] not in label.keys():
                label[data['title']] = 1
            else:
                label[data['title']] += 1
            # 레이블 별로 걸린 시간
            print({data['title'] : data['end']-data['start']})
            result.append({data['title'] : data['end']-data['start']})
    cnt += 1

with open(f'./result.json', 'w') as wf:
    json.dump(result, wf, indent=4)

statistics = {} # 레이블 별로 총 걸린 시간
with open(f'./result.json', 'r') as f:
    result = json.load(f)
    for r in result:
        for k, v in r.items():
            if k not in statistics.keys():
                statistics[k] = v
            else:
                statistics[k] += v

# 레이블 별로 통계 구하기
for k, v in statistics.items():
    print(f'{k}: {v/label[k]}')