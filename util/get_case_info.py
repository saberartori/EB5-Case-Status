import bs4
import re
import requests
from datetime import date


# noinspection PyBroadException
def get_case_info(case_num, show_text=False):
    # Get the response
    url = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=WAC' + str(case_num)
    r1 = requests.get(url)
    content = r1.content
    soup = bs4.BeautifulSoup(content, 'html.parser')
    # if 'You must correct the following error(s) before proceeding:' in soup.text:
    #     raise ValueError(f"Case Number {case_num} doesn't exist!")

    res = []
    # get current case status
    for caseStatus in soup.findAll('div', {'class': 'rows text-center'}):
        if 'I-485' not in caseStatus.text and caseStatus.findAll('h1')[0].text not in \
                ['Card Was Delivered To Me By The Post Office', 'New Card Is Being Produced']:  # Don't have Form Type
            pass
        else:
            if show_text:
                print('---------------------------------')
                print(caseStatus.text)

            status = caseStatus.findAll('h1')[0].text
            desc = caseStatus.findAll('p')[0].text
            # print('CaseNum: ', caseNum)

            # Get date
            # Status below don't have a date so use today's date instead
            if caseStatus.findAll('h1')[0].text in ['Document Was Mailed',
                                                    'Interview Was Completed And My Case Must Be Reviewed']:
                dates = date.today().strftime("%B %d, %Y")
            else:
                try:
                    dates = '{0}, {1}'.format(re.search('On (.+?), ', caseStatus.text).group(1),
                                              re.search(', (.+?), ', caseStatus.text).group(1))
                except:
                    dates = '{0}, {1}'.format(re.search('As of (.+?), ', caseStatus.text).group(1),
                                              re.search(', (.+?), ', caseStatus.text).group(1))
            # Save info into a list
            res.extend([case_num, status, dates, desc])

    return res
