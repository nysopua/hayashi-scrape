# Google Analytics API
import sys
import httplib2
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import AccessTokenRefreshError
import apiclient
from datetime import date,timedelta

def getData():

    #昨日の日付を指定する
    yesterday = date.today()-timedelta(1)
    yesterday = yesterday.strftime('%Y-%m-%d')

    # APIに利用する情報（スコープ、メールアドレス）
    ###↓ここにスラックの情報が入ります。
    scope = "https://www.googleapis.com/auth/analytics.readonly"
    key_file ="[KeyFile]"#ロケーション
    view_id = "[ViewId]"

    # 秘密鍵の読み込み
    with open(key_file, 'rb') as f:
        key = f.read()

    # コネクション作成
    credentials = ServiceAccountCredentials.from_json_keyfile_name(key_file, scopes=scope)
    service = build('analytics', 'v3', credentials=credentials)

    # service = HelloAnalytics.get_service('analytics', 'v3', scope, key_file, service_account_email)

    # データ取得
    ga_results = service.data().ga().get(
        ids=view_id,       # ビューID
        start_date=yesterday,        # 開始年月日
        end_date=yesterday,          # 終了年月日
        dimensions="ga:source",        # ディメンション
        metrics="ga:users", # メトリクス
        max_results=100                  # 最大件数
        # sort=""             # ソート（セッション数の降順）
    ).execute()

    # 取得した結果を表示
    rows = ga_results.get('rows')
    results = "【昨日の流入数】"+"\n"
    for row in rows:
        results = results+"・"+str(row[0])+"："+str(row[1])+"\n"
    return results
