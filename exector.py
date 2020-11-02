import os

if __name__ == '__main__':

    pageUrlList = [
        "https://www.avito.ru/saratov/kvartiry/1-k_kvartira_34_m_89_et._1989595079",
        "https://www.avito.ru/saratov/kvartiry/1-k_kvartira_40.3_m_216_et._1989100669",
        "https://www.avito.ru/saratov/kvartiry/1-k_kvartira_35_m_79_et._2032144390",
        "https://www.avito.ru/saratov/kvartiry/1-k_kvartira_42_m_1125_et._1998994605"
    ]
    savePathList = ['imgs/webpage' + f'{last[-5:]}' + '.png' for last in pageUrlList]

    for pageUrl, savePath in zip(pageUrlList, savePathList):
        print(f'run {pageUrl}')
        prog = 'python screenThePage.py'
        print(savePath)
        os.system(" ".join([prog, pageUrl, savePath]))
