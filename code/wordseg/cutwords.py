# -*- coding: utf-8 -*-


class MM(object):
    """正向最大匹配法"""
    def __init__(self):
        self.window_size = 3
    
    def cut(self, text):
        result = []
        index = 0
        text_length = len(text)
        dic = ['研究', '研究生', '生命', '命', '的', '起源']
        while text_length > index:
            for size in range(self.window_size+index, index, -1):
                piece = text[index:size]
                if piece in dic:
                    index = size - 1
                    break
            index = index + 1
            result.append(piece + '-------')
        return result


class RMM(object):
    """逆向最大匹配法"""
    def __init__(self):
        self.window_size = 3
    
    def cut(self, text):
        result = []
        index = len(text)
        dic = ['研究', '研究生', '生命', '命', '的', '起源']
        while index > 0:
            for size in range(index-self.window_size, index):
                piece = text[size: index]
                if piece in dic:
                    index = size + 1
                    break
            index = index - 1
            result.append(piece + '------')
        result.reverse()
        return result

class HMM(object):
    """隐含马尔可夫模型"""
    def __init__(self):
        pass
    
    def try_load_model(self, trained):
        pass
    
    def train(self, path):
        pass
    
    def viterbi(self, text, states, start_p, trans_p, emit_p):
        pass
    
    def cut(self, text):
        pass

if __name__=='__main__':
    mm = MM()
    rmm = RMM()
    text = '研究生命的起源'
    result_mm = mm.cut(text)
    print(result_mm)
    result_rmm = rmm.cut(text)
    print(result_rmm)