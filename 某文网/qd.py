# -*- coding: utf-8 -*-
import hashlib

from fontTools.ttLib import TTFont


codeStr = """
! ( ) . / 0 1 2 3 4 5
6 7 8 9 A B C D E F G
H I J K L M N O P Q R
S T U V W X Y Z a b c
d e f g h i j k l m n
o p q r s t u v w x y
z · [ ] 万 三 上 下 与 专 世
东 丝 两 为 主 举 乐 乡 书 争 事
二 云 互 五 人 今 介 他 付 仙 代
令 们 价 份 众 会 传 体 作 你 侠
侦 信 修 俱 儿 元 先 免 入 全 公
共 关 其 典 内 军 击 分 创 到 前
剑 剧 力 功 加 动 包 化 区 十 单
南 危 即 历 原 去 友 双 发 变 口
古 另 史 号 同 名 后 吐 启 告 员
周 品 唐 商 喜 团 园 国 土 在 场
堂 墓 增 声 复 外 多 大 奇 女 她
妖 妙 姻 娱 婚 子 字 存 学 它 宅
宇 宋 完 官 宙 宝 实 宠 宫 家 容
寻 导 封 小 已 市 帖 常 幻 广 度
建 开 异 张 强 录 影 往 待 微 快
态 怖 怪 总 恐 息 悚 悬 情 惊 想
感 戏 成 我 战 所 手 才 打 扫 技
投 抗 抢 护 报 抱 拟 指 捷 排 探
推 提 搜 搞 播 支 收 散 数 文 斗
新 方 旅 无 日 时 明 星 春 昨 是
晋 普 暗 更 替 最 月 有 朝 期 未
末 本 术 机 权 条 来 果 架 校 梭
榜 槽 次 欢 歉 歌 步 武 民 气 水
求 汉 江 沉 法 活 浪 浮 消 涯 添
清 游 湖 漫 激 火 点 热 烽 爱 版
物 玄 王 现 球 理 生 田 申 电 界
疑 登 百 的 目 相 看 真 短 码 示
社 神 票 禁 种 科 秘 秦 空 穿 立
站 竞 章 童 笑 笔 等 签 简 管 篇
篮 籍 类 粉 精 系 索 红 约 级 练
经 结 统 维 编 缘 网 置 美 耀 者
职 联 育 能 至 节 苏 荐 荣 萌 藏
虚 行 行 袭 要 视 言 订 讨 记 论
设 访 证 评 诗 话 诡 详 误 说 请
读 谈 豪 账 费 赏 赛 赞 起 超 越
足 路 身 轻 载 辑 过 运 近 还 这
进 远 连 逆 选 通 速 道 部 都 重
钱 销 锐 错 门 闭 问 间 阅 队 际
陆 限 险 隋 随 集 需 霸 青 面 韵
页 预 频 题 风 首 香 验 高 魔 鲜
黑 （ ） ，""".replace("\n", "").split(" ")
# codeStr = """. 0 1 2 3 4 5 6 7 8 9""".replace("\n", "").split(" ")
print(len(codeStr))
font = TTFont("FZZCYSK.f7b3a.woff")
uniMap = font['cmap'].tables[1].ttFont.getBestCmap()
print(uniMap)
uniCode = font['cmap'].tables[1].ttFont.getGlyphOrder()
strDict = dict(zip(uniCode, codeStr))
print(strDict)
uniMd5 = {}
strMd5Dict = {}
for i in uniCode:
    strData = font['glyf'].glyphs.get(i)
    if strData:
        md5data = hashlib.md5(strData.data).hexdigest()
        uniMd5[i] = md5data
        if strDict.get(i):
            strMd5Dict[md5data] = strDict.get(i)
print("uniMd5")
print(uniMd5)
print(str(uniMd5).encode("utf8"))
print(hashlib.md5(str(uniMd5).encode("utf8")).hexdigest())
print("strMd5Dict")
print(strMd5Dict)
