#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='flask_templates')

# ログを保存（グローバル変数として使う）
message_data = []

@app.route('/', methods=['GET'])
def http_get():
    global message_data
    return render_template('index6.html',
                            title='メッセージボード',
                            data=message_data, #dataにログを代入
                            name='名前:', message='メッセージ:')

import datetime

@app.route('/', methods=['POST'])
def http_post():
    global message_data #messageをグローバル変数として使う
  
    # 投稿内容
    yt = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') #現在時刻
    ip = request.remote_addr #送信されたIPアドレス
    idx, text = request.form['idx'], request.form['text'] #名前、メッセージ

    # 現在時刻、IPアドレス、名前、メッセージをログに追加
    message_data.append((text, idx, yt, ip))
  
    # ページ内容を読み直してログの表示を更新する
    return redirect('/')

app.run()


# In[ ]:





# In[ ]:




