import tkinter as tk
from typing import List, Callable

class StringButtonList:
    """
    文字列のリストから縦一列のボタン群を生成し、
    クリックされたボタンの文字列を返す機能を持つクラス。
    """

    def __init__(self, master: tk.Tk, string_list: List[str], callback: Callable[[str], None]):
        """
        クラスの初期化（コンストラクタ）

        :param master: 親となるTkinterウィンドウ (例: tk.Tk())
        :param string_list: ボタンとして表示したい文字列のリスト
        :param callback: ボタンがクリックされたときに呼び出される関数。
                         クリックされたボタンの文字列が引数として渡される。
        """
        self.master = master
        self.string_list = string_list
        self.callback = callback

        # ボタンをまとめるためのフレームを作成
        # これにより、このクラスで作ったUI部品を一つのグループとして扱える
        self.frame = tk.Frame(self.master)
        self.frame.pack(pady=10, padx=10) # ウィンドウ内にフレームを配置

        # ボタンを生成して配置するメソッドを呼び出す
        self._create_buttons()

    def _create_buttons(self):
        """
        リストの各要素に対応するボタンを生成して、フレーム内に縦一列に配置する。
        """
        print("ボタンを生成します...")
        for item_text in self.string_list:
            # 各ボタンにcommandとしてlambda関数を割り当てる
            # これにより、どのボタンが押されたかを区別できる
            #
            # 重要: `t=item_text` のようにデフォルト引数を使うことで、
            #       ループの各時点でのitem_textの値を正しくボタンに束縛できる。
            button = tk.Button(
                self.frame,
                text=item_text,
                command=lambda t=item_text: self.callback(t)
            )
            
            # ボタンをフレーム内に配置する (packはデフォルトで縦に並べる)
            # fill='x'でボタンの幅をフレームの幅に合わせ、padyで上下に少し余白を作る
            button.pack(fill='x', pady=2)

# --- ここから下は、このクラスを実際に使うためのサンプルコード ---

