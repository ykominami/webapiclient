import requests
import json

def make_post_request(url, data=None, headers=None, timeout=30):
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
            headers = {
                'Content-Type': 'application/json',
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
        
        # POSTリクエストを実行
        response = requests.post(
            url=url,
            json=data,
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
        
        return result
        
    except requests.exceptions.RequestException as e:
        error_msg = f"リクエストエラー: {str(e)}"
        print(error_msg)
        return {'error': error_msg}
    except Exception as e:
        error_msg = f"予期しないエラー: {str(e)}"
        print(error_msg)
        return {'error': error_msg}

def main():
    """メイン関数 - 使用例"""
    # テスト用URL（実際のURLに変更してください）
    # test_url = "https://httpbin.org/post"
    test_url = "http://localhost:8080/post"
    
    # カスタムデータ
    custom_data = {
        "name": "test_user_3",
        "message": "POSTリクエストのテスト2",
        "value": 456
    }
    
    # カスタムヘッダー
    custom_headers = {
        "Content-Type": "application/json",
        "X-Custom-Header": "test-value"
    }
    custom_headers_2 = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Custom-Header": "test-value"
    }
    
    print("=== POSTリクエストのテスト ===")
    result = make_post_request(
        url=test_url,
        data=custom_data,
        headers=custom_headers_2
    )
    
    if 'error' not in result:
        print(f"\n=== 成功! ===")
        print(f"ステータスコード: {result['status_code']}")
        if result['json']:
            print(f"JSONレスポンス: {json.dumps(result['json'], indent=2, ensure_ascii=False)}")
    else:
        print(f"\n=== エラー ===")
        print(result['error'])

if __name__ == "__main__":
    main()
