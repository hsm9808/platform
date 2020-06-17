# -*- coding:utf8   -*-
# @Author :George华
# @Time : 2020/6/14 7:11 下午
import urllib.request
import re
import xlwt
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    baseurl = "https://movie.douban.com/top250?start="
    save_path = r".\豆瓣电影Top250.xls"
    # 1.爬取网页
    data_list = get_data(baseurl)
    # 3.保存数据
    save_data(data_list, save_path)


findLink = re.compile(r'<a href="(.*?)">')
findImgsrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def get_data(baseurl):
    datalist = []
    for i in range(0, 226, 25):
        url = baseurl + str(i)
        html = get_one(url)

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            link = re.findall(findLink, item)[0]  # 影片超链接
            data.append(link)
            imgsrc = re.findall(findImgsrc, item)[0]  # 图片链接
            data.append(imgsrc)
            title = re.findall(findTitle, item)  # 片名
            if (len(title) == 2):
                ctitle = title[0]  # 中文名
                data.append(ctitle)
                otitle = title[1].replace("/", "")  # 外国名
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(' ')
            inq = re.findall(findInq, item)  # 简介
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd, item)[0]  # 信息
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br/>
            data.append(bd.strip())  # 去掉前后的空格
            datalist.append(data)
    return datalist


def get_one(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf8")
        return html
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


# 保存数据
def save_data(datalist,savepath):
    book = xlwt.Workbook(encoding="utf8")
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ('电影详情链接', '图片链接', '中文名', '外国名', '概况', '相关信息')
    for i in range(0, 6):
        sheet.write(0, i, col[i])  # 列名
    for j in range(0,250):
        print("第%d条" % (j+1))
        data = datalist[j]
        for k in range(0, 6):
            sheet.write(j+1, k, data[k])
    book.save('豆瓣top250.xls')


if __name__ == "__main__":
    main()
