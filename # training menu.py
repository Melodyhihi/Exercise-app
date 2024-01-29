# training menu
import pandas as pd
import random
import math
from tabulate import tabulate
train_file = pd.read_csv('\\Users\\User\\Desktop\\python 練習檔\\專案碼\\動作菜單分類.csv')

# 開啟檔案
"""with open('\\Users\\User\\Desktop\\python 練習檔\\專案碼\\動作菜單分類.csv', mode='r', encoding='cp950') as file:
    # 逐行讀取檔案內容
    for line in file:
        # 對每一行進行處理，例如印出該行內容
        print(line.strip())"""

# function for random selecting training items

def SelectTraining(list, k=1):
    if __name__ == '__main__':
        return random.SystemRandom().sample(list, k)
 # 制定六大法所產生的練習清單，每個法隨機挑一個

def TrainListGenerator(file_name, method_list, difficulty=0):
    if difficulty == 0:
        diff = '易'
    elif difficulty == 1:
        diff = '中'
    train_list = []
    for i in method_list:
        filt = (file_name['六大推拉分法'] == i) & (file_name['難易度'] == diff)
        train_list += SelectTraining(list(file_name.loc[filt]['動作']))
    return train_list
train_list = TrainListGenerator(train_file, method_list=['上肢水平拉', '上肢水平推'], difficulty=1)
print(train_list)

# # 初始菜單設定
menu_dict = {'Day1': '休', 'Day2': '休', 'Day3': '休',
             'Day4': '休', 'Day5': '休', 'Day6': '休', 'Day7': '休'}


exp = input('新手請輸入A, 中手請輸入B，按Enter送出：')
if exp == 'B':
    print('功能建立中，敬請期待：）')
elif exp == 'A':
    f = input('請輸入您一週預計運動的天數，按Enter送出：')
    # 2 days per week
    if f == '2':
        six_method = ['下肢推', '下肢拉', '上肢水平推', '上肢水平拉', '上肢垂直推', '上肢垂直拉']
        menu_dict['Day1'] = TrainListGenerator(train_file, six_method, 0)
        menu_dict['Day4'] = TrainListGenerator(train_file, six_method, 0)
    # 4 days per week
    elif f == '4':
        # upper body menu
        # 所有關於上半身的，六法各一個
        six_method_up = ['上肢水平推', '上肢水平拉', '上肢垂直推', '上肢垂直拉']

        # lower body menu
        six_method_low = ['下肢推', '下肢拉']

        # 4-day menu list: upper_list + lower_list
        # 禮拜一四上、禮拜二五下
        # 補到四個
        menu_dict['Day1'] = TrainListGenerator(train_file, six_method_up, 0)
        menu_dict['Day2'] = TrainListGenerator(train_file, six_method_low, 0) + ['x', 'x']
        menu_dict['Day4'] = TrainListGenerator(train_file, six_method_up, 0)
        menu_dict['Day5'] = TrainListGenerator(train_file, six_method_low, 0) + ['x', 'x']

    # 6 days per week
    elif f == '6':
        six_method_push = ['上肢垂直推', '上肢水平推']
        six_method_pull = ['上肢垂直拉', '上肢水平拉']
        six_method_leg = ['下肢推', '下肢拉']
        six_days_list_all = []

        # 三個一循環，一週兩循環
        menu_dict['Day1'] = TrainListGenerator(train_file, six_method_push, 0)
        menu_dict['Day2'] = TrainListGenerator(train_file, six_method_pull, 0)
        menu_dict['Day3'] = TrainListGenerator(train_file, six_method_leg, 0)
        menu_dict['Day4'] = TrainListGenerator(train_file, six_method_push, 0)
        menu_dict['Day5'] = TrainListGenerator(train_file, six_method_pull, 0)
        menu_dict['Day6'] = TrainListGenerator(train_file, six_method_leg, 0)

#Display menu
print(menu_dict)
menu_dataframe = pd.DataFrame(menu_dict)
print(tabulate(menu_dataframe, headers='keys', tablefmt='fancy_grid'))

# # 組數
print('第一個月，每個動作組數如下安排：')
num_new = round(6 / int(f))  # 如果一週四天是否一天兩組
newbie = {'week1': [f'{num_new}組 x 8下'], 'week2': [f'{num_new}組 x 10下'],'week3': [f'{num_new}組 x 12下'], 'week4': [f'{num_new}組 x 12下']}
newbie_df = pd.DataFrame(newbie)
print(tabulate(newbie_df, headers='keys', tablefmt='fancy_grid'))

num = int(12 / int(f))
print(f'第二個月開始，每個動作{num}組 x 12下') 
