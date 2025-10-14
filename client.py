import requests
import json
import urllib.parse

import tkinter as tk
from stringbuttonlist import StringButtonList

def object_to_url_encoded(obj):
    """
    JavaScriptのオブジェクトをURLエンコーディング形式の文字列に変換する関数
    
    Args:
        obj (dict): 変換するオブジェクト（辞書）
    
    Returns:
        str: URLエンコーディングされた文字列
    
    Example:
        >>> obj = {"name": "John Doe", "age": 30, "city": "New York"}
        >>> result = object_to_url_encoded(obj)
        >>> print(result)
        name=John%20Doe&age=30&city=New%20York
    """
    try:
        # 辞書の各キーと値をURLエンコード形式に変換
        encoded_pairs = []
        
        for key, value in obj.items():
            # キーと値をURLエンコード
            encoded_key = urllib.parse.quote(str(key), safe='')
            encoded_value = urllib.parse.quote(str(value), safe='')
            
            # key=value の形式で追加
            encoded_pairs.append(f"{encoded_key}={encoded_value}")
        
        # すべてのペアを & で結合
        result = "&".join(encoded_pairs)
        
        return result
        
    except Exception as e:
        error_msg = f"URLエンコーディングエラー: {str(e)}"
        print(error_msg)
        return ""

def make_get_request(url, params=None, headers=None, timeout=30):
    """
    指定されたURLにGETリクエストを送信する関数
    
    Args:
        url (str): GETリクエストを送信するURL
        params (dict, optional): クエリパラメータ
        headers (dict, optional): リクエストヘッダー
        timeout (int): タイムアウト時間（秒）
    
    Returns:
        dict: レスポンス情報を含む辞書
    """
    try:
        # デフォルトヘッダーを設定
        if headers is None:
            headers = {
                'User-Agent': 'Python-GET-Client/1.0'
            }
        
        print(f"GETリクエストを送信中: {url}")
        if params:
            print(f"クエリパラメータ: {json.dumps(params, indent=2, ensure_ascii=False)}")
        print(f"ヘッダー: {json.dumps(headers, indent=2, ensure_ascii=False)}")
        
        # GETリクエストを実行
        response = requests.get(
            url=url,
            params=params,
            headers=headers,
            timeout=timeout
        )
        
        # レスポンス情報を取得
        result = {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response.text,
            'url': response.url
        }
        
        # JSONレスポンスの場合は解析
        try:
            result['json'] = response.json()
        except json.JSONDecodeError:
            result['json'] = None
        
        print(f"\nレスポンス:")
        print(f"ステータスコード: {response.status_code}")
        print(f"レスポンス内容: {response.text[:200]}...")
        print(f"json: {result['json']}")
        
        return result
        
    except requests.exceptions.RequestException as e:
        error_msg = f"リクエストエラー: {str(e)}"
        print(error_msg)
        return {'error': error_msg}
    except Exception as e:
        error_msg = f"予期しないエラー: {str(e)}"
        print(error_msg)
        return {'error': error_msg}

def make_post_request(url, format, data=None, headers=None, timeout=30):
    """
    指定されたURLにPOSTリクエストを送信する関数
    
    Args:
        url (str): POSTリクエストを送信するURL
        data (dict, optional): 送信するデータ
        headers (dict, optional): リクエストヘッダー
        timeout (int): タイムアウト時間（秒）
    
    Returns:
        dict: レスポンス情報を含む辞書
    """
    try:
        # デフォルトヘッダーを設定
        if headers is None:
            if format == 'json':
                headers = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'Python-POST-Client/1.0'
                }
            elif format == 'form':
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'User-Agent': 'Python-POST-Client/1.0'
                }
        
        # デフォルトデータを設定
        if data is None:
            data = {
                'message': 'Hello from Python POST client',
                'timestamp': '2024-01-01T00:00:00Z'
            }
        
        print(f"POSTリクエストを送信中: {url}")
        print(f"送信データ: {json.dumps(data, indent=2, ensure_ascii=False)}")
        print(f"ヘッダー: {json.dumps(headers, indent=2, ensure_ascii=False)}")
        print(f"format: {format}")

        if format == 'json':
            # POSTリクエストを実行
            response = requests.post(
                url=url,
                json=data,
                headers=headers,
                timeout=timeout
            )
        else:
            # POSTリクエストを実行
            response = requests.post(
                url=url,
                data=data,
                headers=headers,
                timeout=timeout
            )

        # レスポンス情報を取得
        result = {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response.text,
            'url': response.url
        }
        
        # JSONレスポンスの場合は解析
        try:
            result['json'] = response.json()
        except json.JSONDecodeError:
            result['json'] = None
        
        print(f"\nレスポンス:")
        print(f"ステータスコード: {response.status_code}")
        print(f"レスポンス内容: {response.text[:200]}...")
        print(f"json: {result['json']}")

        return result
        
    except requests.exceptions.RequestException as e:
        error_msg = f"リクエストエラー: {str(e)}"
        print(error_msg)
        return {'error': error_msg}
    except Exception as e:
        error_msg = f"予期しないエラー: {str(e)}"
        print(error_msg)
        return {'error': error_msg}

    

def make_post_request_json(url, data=None, timeout=30):
    return make_post_request(url, 'json', data, timeout=timeout)


def make_get_request_simple(url, params=None, timeout=30):
    """
    シンプルなGETリクエスト関数
    
    Args:
        url (str): GETリクエストを送信するURL
        params (dict, optional): クエリパラメータ
        timeout (int): タイムアウト時間（秒）
    
    Returns:
        dict: レスポンス情報を含む辞書
    """
    return make_get_request(url, params, None, timeout)

def resultx(result):
    if 'error' not in result:
        print(f"\n=== 成功! ===")
        print(f"ステータスコード: {result['status_code']}")
        if result['json']:            print(f"JSONレスポンス: {json.dumps(result['json'], indent=2, ensure_ascii=False)}")
    else:
        print(f"\n=== エラー ===")
        print(result['error'])

def test_get(url, pattern):
    params = make_params(pattern)
    test_get_sub(url, params)

def test_get_sub(url, params):
    print("=== GETリクエストのテスト ===")
    # GETリクエストのテスト
    
    result = make_get_request_simple(
        url=url,
        params=params
    )
    resultx(result)
    print("==========================================")


def test_post_json(url, pattern):
    params = make_params(pattern)

    result = test_post_sub_json(url, params)
    resultx(result)
    print("==========================================")

def test_post_sub_json(url, params):
    print("=== POSTリクエストのテスト ===")
    # POSTリクエストのテスト
    
    result = make_post_request_json(
        url=url,
        data=params
    )
    return result

def test_post_form(url, pattern):
    params = make_params(pattern)

    result = test_post_sub_form(url, params)
    resultx(result)
    print("==========================================")

def test_post_sub_form(url, params):
    print("=== POSTリクエストのテスト ===")
    # POSTリクエストのテスト
    result = make_post_request(url, 'form', params)
    '''
    result = make_post_request_form(
        url=url,
        data=params
    )
    '''
    return result

def make_params(pattern):
    params = None

    if pattern == 'OpenAI-Cursor':
        params = {
            'cmd': 'web_api',
            'name': 'OpenAI',
            'kind': 'CursorCursor'
        }

    elif pattern == 'web_api_s':
        params = {
            'cmd': 'web_api_s',
            'name': 'OpenAI',
            'kind': 'CursorCursor'
        }
    elif pattern == 'web_api_2':
        params = {
            'cmd': 'web_api_2',
            'name': 'OpenAI',
            'kind': 'CursorCursor'
        }
    elif pattern == "web_api_list":
        params = {
            "cmd": "web_api_list",
        }
    elif pattern == "pc_config":
        params = {
            "cmd": "pc_config",
        }
    elif pattern == "planning":
        params = {
            "cmd": "planning",
        }
    else:
        print(f"pattern: {pattern} is not supported")

    return params

def main(choice):
    #url = "https://script.google.com/macros/s/AKfycbyVI7e9uZ9c7BDWXDd2-272hX2MefjUyJkzHsahYpAINn3-PPYnhKO4LcpvK9uxrIsq/exec"
    # url = "https://script.google.com/macros/s/AKfycbwFir48x3T1B9fY3aHGaMYpO96fxFsvTqDusbxe6FB92Htrj4xdO3ZccP_YscAdcAJt/exec" 
    url = "https://script.google.com/macros/s/AKfycbwFir48x3T1B9fY3aHGaMYpO96fxFsvTqDusbxe6FB92Htrj4xdO3ZccP_YscAdcAJt/exec"
    # test_get(url, "OpenAI-Cursor")
    # test_get(url, "web_api_s")
    # test_get(url, "web_api_2")
    # test_get(url, "web_api_list")
    # test_get(url, "pc_config")
    # test_get(url, "planning")

    test_post_json(url, choice)
    # test_post_json(url, "OpenAI-Cursor")
    # est_post_json(url, "web_api_s")
    # test_post_json(url, "web_api_2")
    # test_post_json(url, "web_api_list")
    # test_post_json(url, "pc_config")
    # test_post_json(url, "planning")

    # test_post_form(url, "OpenAI-Cursor")
    # test_post_form(url, "web_api_s")
    # test_post_form(url, "web_api_2")
    # test_post_form(url, "web_api_list")
    # test_post_form(url, "pc_config")
    # test_post_form(url, "planning")

    # test_post_form(url)
    
def gui_init():
    # 1. ボタンがクリックされたときに実行する関数を定義
    def handle_button_click(clicked_string: str):
        """
        コールバック関数。クリックされたボタンの文字列を受け取り、
        コンソールとウィンドウのラベルに表示する。
        """
        print(f"ボタン '{clicked_string}' がクリックされました！")
        # ウィンドウ下部のラベルのテキストを更新
        result_label.config(text=f"選択された項目: {clicked_string}")
        main(clicked_string)

    # 2. メインのウィンドウを作成
    root = tk.Tk()
    root.title("文字列リストからのボタン生成")
    root.geometry("300x400") # ウィンドウの初期サイズ

    # 3. ボタンにしたい文字列のリストを定義
    fruits = ["OpenAI-Cursor", "web_api_s", "web_api_2", "web_api_list", "pc_config", "planning"]

    # 4. StringButtonListクラスのインスタンスを生成
    #    ウィンドウ(root), 文字列リスト(fruits), コールバック関数(handle_button_click)を渡す
    button_list_widget = StringButtonList(
        master=root, 
        string_list=fruits, 
        callback=handle_button_click
    )
    
    # 結果を表示するためのラベルをウィンドウに配置
    result_label = tk.Label(root, text="上のボタンをクリックしてください", font=("Helvetica", 12))
    result_label.pack(pady=20)

    # 5. アプリケーションのメインループを開始
    #    これによりウィンドウが表示され、ユーザーの操作を待ち受ける
    root.mainloop()

    # main()

if __name__ == "__main__":
    gui_init()
