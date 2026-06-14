import pandas as pd

# データフレームの作成
df = pd.DataFrame({
    '日付': [
        '2023-05-17',
        '2023-05-18',
        '2023-05-19',
        '2023-05-20',
        '2023-05-21'
    ],
    'スケジュール': ['設計', '開発', 'テスト', '運用', '保守'],
    '優先レベル': [1, 2, 5, 4, 3],
    '状況': ['完了', '作業中', '作業中', '未着手', '未着手'],
})
df['平均レベル'] = df['優先レベル'].mean()

# 優先レベルで分岐して緊急度を求める関数
def prioritize(level):
    result = ''

    if level >= 5:
        result = '高'

    elif level == 4 or level == 3:
        result = '中'

    else:
        result = '低'

    return result

# 緊急度列を追加
df['緊急度'] = df['優先レベル'].apply(prioritize)
print(df)
# Excelファイルを作成
writer = pd.ExcelWriter('スケジュール管理表.xlsx')

# Excelファイルへ書き込み
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Excelファイルを閉じる
writer.close()
