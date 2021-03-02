# -*- coding: utf-8 -*-
from fontTools.ttLib import TTFont


# 字体文件中字体名称所对应的字
strMd5Dict = {'.notdef': '!', 'parenleft': '(', 'parenright': ')', 'period': '.', 'slash': '/', 'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '56', 'six': '7', 'seven': '8', 'eight': '9', 'nine': 'A', 'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 'GH', 'G': 'I', 'H': 'J', 'I': 'K', 'J': 'L', 'K': 'M', 'L': 'N', 'M': 'O', 'N': 'P', 'O': 'Q', 'P': 'RS', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'a', 'Y': 'b', 'Z': 'cd', 'a': 'e', 'b': 'f', 'c': 'g', 'd': 'h', 'e': 'i', 'f': 'j', 'g': 'k', 'h': 'l', 'i': 'm', 'j': 'no', 'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't', 'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'yz', 'u': '·', 'v': '[', 'w': ']', 'x': '万', 'y': '三', 'z': '上', 'periodcentered': '下', 'uni300C': '与', 'uni300D': '专', 'uni4E07': '世东', 'uni4E09': '丝', 'uni4E0A': '两', 'uni4E0B': '为', 'uni4E0E': '主', 'uni4E13': '举', 'uni4E16': '乐', 'uni4E1C': '乡', 'uni4E1D': '书', 'uni4E24': '争', 'uni4E3A': '事二', 'uni4E3B': '云', 'uni4E3E': '互', 'uni4E50': '五', 'uni4E61': '人', 'uni4E66': '今', 'uni4E89': '介', 'uni4E8B': '他', 'uni4E8C': '付', 'uni4E91': '仙', 'uni4E92': '代令', 'uni4E94': '们', 'uni4EBA': '价', 'uni4ECA': '份', 'uni4ECB': '众', 'uni4ED6': '会', 'uni4ED8': '传', 'uni4ED9': '体', 'uni4EE3': '作', 'uni4EE4': '你', 'uni4EEC': '侠侦', 'uni4EF7': '信', 'uni4EFD': '修', 'uni4F17': '俱', 'uni4F1A': '儿', 'uni4F20': '元', 'uni4F53': '先', 'uni4F5C': '免', 'uni4F60': '入', 'uni4FA0': '全', 'uni4FA6': '公共', 'uni4FE1': '关', 'uni4FEE': '其', 'uni4FF1': '典', 'uni513F': '内', 'uni5143': '军', 'uni5148': '击', 'uni514D': '分', 'uni5165': '创', 'uni5168': '到', 'uni516C': '前剑', 'uni5171': '剧', 'uni5173': '力', 'uni5176': '功', 'uni5178': '加', 'uni5185': '动', 'uni519B': '包', 'uni51FB': '化', 'uni5206': '区', 'uni521B': '十', 'uni5230': '单南', 'uni524D': '危', 'uni5251': '即', 'uni5267': '历', 'uni529B': '原', 'uni529F': '去', 'uni52A0': '友', 'uni52A8': '双', 'uni5305': '发', 'uni5316': '变', 'uni533A': '口古', 'uni5341': '另', 'uni5355': '史', 'uni5357': '号', 'uni5371': '同', 'uni5373': '名', 'uni5386': '后', 'uni539F': '吐', 'uni53BB': '启', 'uni53CB': '告', 'uni53CC': '员周', 'uni53D1': '品', 'uni53D8': '唐', 'uni53E3': '商', 'uni53E4': '喜', 'uni53E6': '团', 'uni53F2': '园', 'uni53F7': '国', 'uni540C': '土', 'uni540D': '在', 'uni540E': '场堂', 'uni5410': '墓', 'uni542F': '增', 'uni544A': '声', 'uni5458': '复', 'uni5468': '外', 'uni54C1': '多', 'uni5510': '大', 'uni5546': '奇', 'uni559C': '女', 'uni56E2': '她妖', 'uni56ED': '妙', 'uni56FD': '姻', 'uni571F': '娱', 'uni5728': '婚', 'uni573A': '子', 'uni5802': '字', 'uni5893': '存', 'uni589E': '学', 'uni58F0': '它', 'uni590D': '宅宇', 'uni5916': '宋', 'uni591A': '完', 'uni5927': '官', 'uni5947': '宙', 'uni5973': '宝', 'uni5979': '实', 'uni5996': '宠', 'uni5999': '宫', 'uni59FB': '家', 'uni5A31': '容寻', 'uni5A5A': '导', 'uni5B50': '封', 'uni5B57': '小', 'uni5B58': '已', 'uni5B66': '市', 'uni5B83': '帖', 'uni5B85': '常', 'uni5B87': '幻', 'uni5B8B': '广', 'uni5B8C': '度建', 'uni5B98': '开', 'uni5B99': '异', 'uni5B9D': '张', 'uni5B9E': '强', 'uni5BA0': '录', 'uni5BAB': '影', 'uni5BB6': '往', 'uni5BB9': '待', 'uni5BFB': '微', 'uni5BFC': '快态', 'uni5C01': '怖', 'uni5C0F': '怪', 'uni5DF2': '总', 'uni5E02': '恐', 'uni5E16': '息', 'uni5E38': '悚', 'uni5E7B': '悬', 'uni5E7F': '情', 'uni5EA6': '惊', 'uni5EFA': '想感', 'uni5F00': '戏', 'uni5F02': '成', 'uni5F20': '我', 'uni5F3A': '战', 'uni5F55': '所', 'uni5F71': '手', 'uni5F80': '才', 'uni5F85': '打', 'uni5FAE': '扫', 'uni5FEB': '技投', 'uni6001': '抗', 'uni6016': '抢', 'uni602A': '护', 'uni603B': '报', 'uni6050': '抱', 'uni606F': '拟', 'uni609A': '指', 'uni60AC': '捷', 'uni60C5': '排', 'uni60CA': '探推', 'uni60F3': '提', 'uni611F': '搜', 'uni620F': '搞', 'uni6210': '播', 'uni6211': '支', 'uni6218': '收', 'uni6240': '散', 'uni624B': '数', 'uni624D': '文', 'uni6253': '斗新', 'uni626B': '方', 'uni6280': '旅', 'uni6295': '无', 'uni6297': '日', 'uni62A2': '时', 'uni62A4': '明', 'uni62A5': '星', 'uni62B1': '春', 'uni62DF': '昨', 'uni6307': '是晋', 'uni6377': '普', 'uni6392': '暗', 'uni63A2': '更', 'uni63A8': '替', 'uni63D0': '最', 'uni641C': '月', 'uni641E': '有', 'uni64AD': '朝', 'uni652F': '期', 'uni6536': '未末', 'uni6563': '本', 'uni6570': '术', 'uni6587': '机', 'uni6597': '权', 'uni65B0': '条', 'uni65B9': '来', 'uni65C5': '果', 'uni65E0': '架', 'uni65E5': '校', 'uni65F6': '梭榜', 'uni660E': '槽', 'uni661F': '次', 'uni6625': '欢', 'uni6628': '歉', 'uni662F': '歌', 'uni664B': '步', 'uni666E': '武', 'uni6697': '民', 'uni66F4': '气', 'uni66FF': '水求', 'uni6700': '汉', 'uni6708': '江', 'uni6709': '沉', 'uni671D': '法', 'uni671F': '活', 'uni672A': '浪', 'uni672B': '浮', 'uni672C': '消', 'uni672F': '涯', 'uni673A': '添清', 'uni6743': '游', 'uni6761': '湖', 'uni6765': '漫', 'uni679C': '激', 'uni67B6': '火', 'uni6821': '点', 'uni68AD': '热', 'uni699C': '烽', 'uni69FD': '爱', 'uni6B21': '版物', 'uni6B22': '玄', 'uni6B49': '王', 'uni6B4C': '现', 'uni6B65': '球', 'uni6B66': '理', 'uni6C11': '生', 'uni6C14': '田', 'uni6C34': '申', 'uni6C42': '电', 'uni6C49': '界疑', 'uni6C5F': '登', 'uni6C89': '百', 'uni6CD5': '的', 'uni6D3B': '目', 'uni6D6A': '相', 'uni6D6E': '看', 'uni6D88': '真', 'uni6DAF': '短', 'uni6DFB': '码', 'uni6E05': '示社', 'uni6E38': '神', 'uni6E56': '票', 'uni6F2B': '禁', 'uni6FC0': '种', 'uni706B': '科', 'uni70B9': '秘', 'uni70ED': '秦', 'uni70FD': '空', 'uni7231': '穿', 'uni7248': '立站', 'uni7269': '竞', 'uni7384': '章', 'uni738B': '童', 'uni73B0': '笑', 'uni7403': '笔', 'uni7406': '等', 'uni751F': '签', 'uni7530': '简', 'uni7533': '管', 'uni7535': '篇篮', 'uni754C': '籍', 'uni7591': '类', 'uni767B': '粉', 'uni767E': '精', 'uni7684': '系', 'uni76EE': '索', 'uni76F8': '红', 'uni770B': '约', 'uni771F': '级', 'uni77ED': '练经', 'uni7801': '结', 'uni793A': '统', 'uni793E': '维', 'uni795E': '编', 'uni7968': '缘', 'uni7981': '网', 'uni79CD': '置', 'uni79D1': '美', 'uni79D8': '耀', 'uni79E6': '者职', 'uni7A7A': '联', 'uni7A7F': '育', 'uni7ACB': '能', 'uni7AD9': '至', 'uni7ADE': '节', 'uni7AE0': '苏', 'uni7AE5': '荐', 'uni7B11': '荣', 'uni7B14': '萌', 'uni7B49': '藏虚', 'uni7B7E': '行', 'uni7B80': '行', 'uni7BA1': '袭', 'uni7BC7': '要', 'uni7BEE': '视', 'uni7C4D': '言', 'uni7C7B': '订', 'uni7C89': '讨', 'uni7CBE': '记', 'uni7CFB': '论设', 'uni7D22': '访', 'uni7EA2': '证', 'uni7EA6': '评', 'uni7EA7': '诗', 'uni7EC3': '话', 'uni7ECF': '诡', 'uni7ED3': '详', 'uni7EDF': '误', 'uni7EF4': '说', 'uni7F16': '请读', 'uni7F18': '谈', 'uni7F51': '豪', 'uni7F6E': '账', 'uni7F8E': '费', 'uni8000': '赏', 'uni8005': '赛', 'uni804C': '赞', 'uni8054': '起', 'uni80B2': '超', 'uni80FD': '越足', 'uni81F3': '路', 'uni8282': '身', 'uni82CF': '轻', 'uni8350': '载', 'uni8363': '辑', 'uni840C': '过', 'uni85CF': '运', 'uni865A': '近', 'uni884C': '还', 'uni884D': '这进', 'uni88AD': '远', 'uni8981': '连', 'uni89C6': '逆', 'uni8A00': '选', 'uni8BA2': '通', 'uni8BA8': '速', 'uni8BB0': '道', 'uni8BBA': '部', 'uni8BBE': '都', 'uni8BBF': '重钱', 'uni8BC1': '销', 'uni8BC4': '锐', 'uni8BD7': '错', 'uni8BDD': '门', 'uni8BE1': '闭', 'uni8BE6': '问', 'uni8BEF': '间', 'uni8BF4': '阅', 'uni8BF7': '队', 'uni8BFB': '际陆', 'uni8C08': '限', 'uni8C6A': '险', 'uni8D26': '隋', 'uni8D39': '随', 'uni8D4F': '集', 'uni8D5B': '需', 'uni8D5E': '霸', 'uni8D77': '青', 'uni8D85': '面', 'uni8D8A': '韵页', 'uni8DB3': '预', 'uni8DEF': '频', 'uni8EAB': '题', 'uni8F7B': '风', 'uni8F7D': '首', 'uni8F91': '香', 'uni8FC7': '验', 'uni8FD0': '高', 'uni8FD1': '魔', 'uni8FD8': '鲜黑', 'uni8FD9': '（', 'uni8FDB': '）', 'uni8FDC': '，'}


class DpFont(object):
    def __init__(self, fontname):
        """
        fontname下载的动态字体
        :param fontname:
        """
        self.fontname = fontname
        self.__get_woff_int()

    def __get_woff_int(self):
        font = TTFont(self.fontname)
        uniMap = font['cmap'].tables[1].ttFont.getBestCmap()
        # print(uniMap)
        # 字体文件中字体的int值对应字体的名字
        self.woffIntDict = uniMap

    def __code_md5(self, codeaft):
        """
        根据字符找到字符对应的md5值，并得到对应的映射字
        :param codeaft:
        :return:
        """
        codenum = self.woffIntDict.get(codeaft)
        if codenum:
            return strMd5Dict.get(codenum)
        return codeaft

    def get_decode(self, code):
        if isinstance(code, str):
            codeaft = int(code.replace("&#", ""))
            return self.__code_md5(codeaft)
        if isinstance(code, list):
            for num, codepro in enumerate(code):
                codeaft = int(codepro.replace("&#", ""))
                code[num] = self.__code_md5(codeaft)
            return code


if __name__ == '__main__':
    font = DpFont("OdoFTigw.woff")
    print(font.get_decode("&#100218"))
    print("".join(font.get_decode("&#100218;&#100218;&#100221;&#100218;&#100215".split(";"))))
