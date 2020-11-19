#爬104網站 Campany name,opening,content 做成CSV

import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
import os
import csv
import openpyxl

# if not os.path.exists('./104jobhw'):
#     os.mkdir('./104jobhw')

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'

header = {'User-Agent': useragent}
url = 'https://www.104.com.tw/jobs/search/?'
keyword = {'keyword': '資料工程師'}  # 搜尋項目
joburl = requests.get(url, keyword, headers=header).url  # 得到搜尋的url
# print(joburl)
res = requests.get(joburl, headers=header).text
# print(res)
jobsoup = BeautifulSoup(res, 'html.parser')
# print(jobsoup)
jobtitles = jobsoup.select('h2.b-tit a')
# print(jobtitles)

all_job_datas = []
jobdata = pd.DataFrame()
for jobtitle in jobtitles:
    # print(jobtitle)
    # print('=============================')

    url2 = "https:" + jobtitle['href']  # 職缺網址
    # print(url2)
    jsurl = 'https://www.104.com.tw/job/ajax/content/' + url2.split('/')[-1] #取得職缺網業ajax網址
    referer = url2.split('?')[0]
    # print(referer)
    # print(jsurl)
    header2 = {'User-Agent': useragent, 'Referer': referer}

    res2 = requests.get(jsurl, headers=header2).text
    # print(res2)
    jobjs = json.loads(res2)['data']
    # print(jobjs)
    # print('=============================')
    opening = jobjs['header']['jobName'].replace(' ', '')
    company = jobjs['header']['custName'].replace(' ', '')
    address = jobjs['jobDetail']['addressRegion'].replace(' ', '')
    sal = jobjs['jobDetail']['salary'].replace(' ', '')
    exp = jobjs['condition']['workExp'][0:4].replace(' ', '')
    school = jobjs['condition']['edu'][0:2].replace(' ', '')
    content = jobjs['jobDetail']['jobDescription'].replace(' ', '')
    welfare = jobjs['welfare']['welfare'].replace(' ', '')

    # print('職務名稱:',jobjs['header']['jobName'])
    # print('公司名稱:',jobjs['header']['custName'])
    # print('公司地點:',jobjs['jobDetail']['addressRegion'])
    # print('員工薪資:',jobjs['jobDetail']['salary'])
    # print('工作經歷:',jobjs['condition']['workExp'][0:4])
    # print('學歷要求:',jobjs['condition']['edu'][0:2])
    # print('工作內容',jobjs['jobDetail']['jobDescription'])
    # print('員工福利:',jobjs['welfare']['welfare'])
    # print('擅長工具:',jobjs['condition']['specialty'])

    skill = []
    for i in jobjs['condition']['specialty']:
        skill.append(i['description'])
        # print([i])
    # print('擅長工具:',skill)
    # print('=' * 30)

    opening = '%s' % opening
    company = '%s' % company
    address = '%s' % address
    sal = '%s' % sal
    exp = '%s' % exp
    school = '%s' % school
    skill = '%s' % skill
    url2 = '%s' % url2
    conent = '%s' % content
    welfare = '%s' % welfare

    joblist2 = {
        '職務名稱': opening,
        '公司名稱': company,
        '公司地點': address,
        '員工薪資': sal,
        '工作經歷': exp,
        '學歷要求': school,
        '擅長工具': skill,
        '職缺網址': url2,
        '工作內容': content,
        '員工福利': welfare
    }
    # print(joblist2)
    all_job_datas.append(joblist2)
    # print(all_job_datas)

    #轉成CSV檔
    fn = '104職缺作業.csv'
    columns_name = ['職務名稱', '公司名稱', '公司地點', '員工薪資', '工作經歷', '學歷要求', '擅長工具', '職缺網址', '工作內容', '員工福利']
    with open(fn,'w',newline='',encoding='utf-8-sig') as f:
        dictwriter = csv.DictWriter(f,fieldnames=columns_name)
        dictwriter.writeheader()
        for data in all_job_datas:
            dictwriter.writerow(data)

