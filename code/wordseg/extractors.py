# -*- coding: utf-8 -*-

def get_TF(words, topK=10):
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) + 1
    return sorted(tf_dic.items(), key = lambda x: x[1], reverse=True)[:topK]


if __name__=='__main__':
    words = '育儿 问答 育儿 知识 育儿网 解决问题 已有 回答 回答 率 友情 提醒 回答 时请 活动 规则 选 满意 回答 结束 提问 到期 采纳 系统 自动 帮 采纳 悬'
    words = words.split(' ')
    x = get_TF(words, topK=10)
    
    print(x)