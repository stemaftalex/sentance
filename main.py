from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase
import random

# 註冊支援中文的微軟正黑字體
LabelBase.register(name="MicrosoftJhengHei", fn_regular="msjh.ttc")

class SentenceReorderGame(App):
    def build(self):
        self.sentences = [
            "我 喜歡 學習 Python",
            "這 是 一個 有趣 的 遊戲",
            "天氣 很 好 今天",
            "我們 一起 去 海邊"
        ]

        self.word_types = {
            "我": "代名詞",
            "喜歡": "動詞",
            "學習": "動詞",
            "Python": "名詞",
            "這": "代名詞",
            "是": "動詞",
            "一個": "形容詞",
            "有趣": "形容詞",
            "的": "介係詞",
            "遊戲": "名詞",
            "天氣": "名詞",
            "很": "副詞",
            "好": "形容詞",
            "今天": "名詞",
            "我們": "代名詞",
            "一起": "副詞",
            "去": "動詞",
            "海邊": "名詞"
        }

        self.colors = {
            "名詞": [1, 0.8, 0.8, 1],  # 淡紅色
            "代名詞": [1, 0.8, 1, 1],  # 淡粉色
            "動詞": [0.8, 0.8, 1, 1],  # 淡藍色
            "形容詞": [0.8, 1, 1, 1],  # 淡青色
            "副詞": [0.8, 1, 0.8, 1],  # 淡綠色
            "介係詞": [1, 1, 0.8, 1],  # 淡黃色
            "連接詞": [1, 0.8, 0.6, 1],  # 淡橙色
            "感嘆詞": [1, 0.85, 0.73, 1]  # 淡桃色
        }

        self.main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.sentence_label = Label(text="重組下列句子：", font_size='30sp', font_name="MicrosoftJhengHei")
        self.main_layout.add_widget(self.sentence_label)

        self.words_layout = BoxLayout(size_hint_y=None, height=300)
        self.scroll_view = ScrollView(size_hint=(1, None), size=(800, 300))
        self.scroll_view.add_widget(self.words_layout)
        self.main_layout.add_widget(self.scroll_view)

        self.input_entry = TextInput(font_size='30sp', size_hint_y=None, height=70, multiline=False, font_name="MicrosoftJhengHei")
        self.main_layout.add_widget(self.input_entry)

        self.submit_button = Button(text="提交答案", font_size='30sp', on_press=self.check_answer, font_name="MicrosoftJhengHei")
        self.main_layout.add_widget(self.submit_button)

        self.new_sentence_button = Button(text="下一句", font_size='30sp', on_press=self.new_sentence, font_name="MicrosoftJhengHei")
        self.main_layout.add_widget(self.new_sentence_button)

        self.new_sentence()

        return self.main_layout

    def new_sentence(self, *args):
        self.current_sentence = random.choice(self.sentences)
        words = self.current_sentence.split()
        random.shuffle(words)
        self.shuffled_words = words

        self.words_layout.clear_widgets()

        for word in words:
            word_type = self.word_types.get(word, "名詞")
            color = self.colors[word_type]
            button = Button(text=word, font_size='30sp', background_color=color, size_hint_x=None, width=200,
                            on_press=lambda btn: self.add_word_to_entry(btn.text), font_name="MicrosoftJhengHei")
            self.words_layout.add_widget(button)

        self.input_entry.text = ""



    def add_word_to_entry(self, word):
        current_text = self.input_entry.text
        if current_text:
            current_text += " "
        self.input_entry.text = current_text + word

    def check_answer(self, instance):
        user_input = self.input_entry.text
        if user_input == self.current_sentence:
            self.show_popup("結果", "恭喜你！重組正確！")
        else:
            self.show_popup("結果", "重組錯誤！請再試一次。")

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_label = Label(text=message, font_size='20sp', font_name="MicrosoftJhengHei")
        close_button = Button(text="關閉", font_size='20sp', size_hint_y=None, height=50, font_name="MicrosoftJhengHei")
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.5))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    SentenceReorderGame().run()