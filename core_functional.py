# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
import importlib
from toolbox import clear_line_break
from toolbox import apply_gpt_academic_string_mask_langbased
from toolbox import build_gpt_academic_masked_string_langbased
from textwrap import dedent

def get_core_functions():
    return {

        "生成大纲": {
            # [1*] 前缀字符串，会被加在你的输入之前。例如，用来描述你的要求，例如翻译、解释代码、润色等等。
            "Prefix":   r"现在，请按照以下材料（例如研究背景、研究现状、存在的问题、提出的方法、核心创新点、实验思路和效果等）帮我撰写论文的写作大纲：\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。例如，配合前缀可以把你的输入内容用引号圈起来
            "Suffix":   r"\n\n## 格式要求："
                        r"1. 大纲内容请用中文回复。",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None，举例：写个函数移除所有的换行符）
            "PreProcess": None,
            # [7] 模型选择 （可选参数。如不设置，则使用当前全局模型；如设置，则用指定模型覆盖全局模型。）
            # "ModelOverride": "gpt-3.5-turbo", # 主要用途：强制点击此基础功能按钮时，使用指定的模型。
        },

        "撰写Introduction": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"现在，请按照以下材料帮我撰写论文的Introduction章节：\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 请遵循以下结构生成：\n"
                        r"1. Background → Topic (1-2 paragraphs) \n"
                        r"2. Literature Review → Motivation (1 paragraph) \n"
                        r"3. Method Overview (1 paragraph) \n"
                        r"4. Experiment Overview (1 paragraph) \n"
                        r"5. Contributions (1 paragraph) \n"
                        r"6. Roadmap (1 paragraph)\n\n"
                        r"## 格式要求：\n"
                        r"1. 正文内容使用英语，采用专业、规范、学术性语气。\n"
                        r"2. 不要列表、表情，请按照学术论文规范返回段落形式。\n"
                        r"3. 行文流畅，保证清晰（clearly）、凝练（concisely）、准确（precisely）、具有逻辑性（logically）。",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "调整Background-Topic段落": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"现在，需要对 Introduction 章节中的以下段落进行调整：\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 请遵循以下原则：\n"
                        r"1. 从 Background 快速过渡到 Topic，不必过度展开。\n"
                        r"2. Topic 介绍应以时间（例如过去与现在的对比）或应用（例如应用场景等）为导向。\n"
                        r"3. 主题可以通过其概念（concept）、特点（characteristics）、应用（application）、重要性（important）等方面来描述。\n\n"
                        r"## 格式要求：\n"
                        r"1. 注意逻辑性，例如时间顺序。\n"
                        r"2. 可以使用连接词来保证逻辑性和通顺性，例如以下连接词：\n"
                        r"    - 表示转折：`However`, `Hence`...\n"
                        r"    - 表示并列：`Therefore`, `that is`, `And`...\n"
                        r"    - 表示递进：`Moreover`, `Furthermore`, `In addition`, `While` ...\n"
                        r"3. 注意措辞客观，不要使用过度夸大的词汇，例如 `discover`, `technology` ...\n"
                        r"4. 不要列、表情，请整理为1～2个段落。",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "调整LiteratureReview-Motivation段落": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"现在，需要对 Introduction 章节中的以下段落进行调整：\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 请遵循以下结构：\n"
                        r"1. Summarization of notable methods (nearest neighbors) \n"
                        r"2. Comments on limitation/weakness (explain why)\n"
                        r"3. Motivation (against limitation/weakness)\n\n"
                        r"## 格式要求：\n"
                        r"1. 对于研究现状的不足的说明，注意要采用温和语气，并且只写跟自己研究相关的不足。\n"
                        r"2. 尽可能用虚拟语气，保持客观，例如 `could`, `would`, ...\n"
                        r"3. 尽量不要出现连字符`-`。\n"
                        r"4. 尽量不要使用 `'`，例如使用 cannot 代替 can't。\n"
                        r"4. 不要列、表情，请整理为1个段落。",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "调整MethodOverview段落": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"现在，需要对 Introduction 章节中方法概述部分进行调整：\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 请遵循以下结构：\n"
                        r"1. 首先说明方法定义，例如：`In this paper, we propose a adj. method/algorithm Method Name, to.. ../for....`，或 `This paper introduces a novel method/algorithm to...../for....., called Method Name.` \n"
                        r"2. 其次进行方法理论解释。注意此处不详细展开方法的详细步骤，只描述方法机理，并介绍其超越其他方法的的原因。\n\n"
                        r"## 格式要求：\n"
                        r"1. 不要列、表情，请整理为1个段落。",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "调整Contribution段落": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"现在，需要编写 Introduction 章节中的实验描述部分，请基于以下实验部分章节内容：\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 包含：\n"
                        r"1. New Concept \n"
                        r"2. New Method (Model/Algorithm/System) \n"
                        r"3. Better Algorithm(More Efficient, Less Memory, Parallelism and etc.) \n"
                        r"4. New Result (Apply existing methods in new domains, getting significant results)\n\n"
                        r"现在，请结合内容、分级原则和我的观点，编写 Contribution 部分。\n\n"
                        r"## 格式要求：\n"
                        r"1. 不超过 [4，可自行调整] 条\n"
                        r"2. 语句精炼，不要过长。\n"
                        r"3. 不要列、表情，请整理为1个段落。",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "撰写Roadmap段落": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"现在，请根据大纲内容来撰写 Introduction 章节中的 Roadmap 部分：\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 格式要求：\n"
                        r"1. 不要列、表情，请整理为1个段落。\n\n"
                        r"## 请参考以下撰写示例：\n\n"
                        r"The rest of this paper is organized as follows: In the next section, we ... In Section 3, ... Finally, we conclude in Section 6.",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "撰写RelatedWork章节": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"[此处粘贴大纲中的相关研究部分]\n\n现在请基于以上大纲，撰写论文中的Related Work章节。\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 格式要求：\n"
                        r"1. 段落输出，不要列表、表情。\n"
                        r"2. 学术论文风格，书面表达。",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "形式化定义": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   "",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n现在请基于以上内容，总结正文方法部分的形式化定义。"
                        r"\n\n## 具体要求：\n"
                        r"1. 为方法每个阶段都引入形式化符号，总体保持简洁但完整。\n"
                        r"2. 强化流程连接性\n\n"
                        r"## 格式要求：\n"
                        r"1. Markdown格式输出，方便查看内容",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "撰写方法帽子段": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"请为我的方法撰写帽子段，主要进行系统概述。\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 参照以下结构示例：\n"
                        r"In this section, we present the proposed ...  Figure 1 illustrates the overall architecture of the PRJ framework, which ... In the first phase, .... In the second phase, ... In the final phase of ..., ...",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "分析实验结果": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"## 实验结果如下：\n\n[此处放实验表格数据]\n\n请分析实验结果并撰写学术论文正文内容：\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 期望目标：\n"
                        r"1. 突出我们方法的有效性，检测率越高越好。\n"
                        r"2. 突出我们方法的先进性，在多模型下对比baselines都全面超越。\n"
                        r"3. 突出检测能力的目标一致性，尤其是跟Q16相比，可以计算一个统计学指标来表征，例如Spearma 相关系数。\n\n"
                        r"## 注意：\n"
                        r"1. 采用专业学术写作风格，简洁规范、语句通顺。\n"
                        r"2. 不要列表，采用正文段落内容返回。",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "撰写Conclusion章节": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"请基于以上 Method 和 Experiment 正文内容，撰写论文中 Conclusion 章节。\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 格式要求：\n"
                        r"1. 要包含方法、贡献、实验结果、应用或优势等方面的总结。\n"
                        r"2. 包含Future Work部分。",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },

        "撰写Abstract章节": {
            # [1*] 前缀字符串，会被加在你的输入之前。
            "Prefix":   r"请基于以上 Introduction 和 Conclusion 正文内容，撰写论文中Abstract 章节。\n\n",
            # [2*] 后缀字符串，会被加在你的输入之后。
            "Suffix":   r"\n\n## 格式要求：\n"
                        r"1. 不要列表、表情，返回一整段内容。\n"
                        r"2. 突出研究动机。\n\n"
                        r"## 参考示例：\n"
                        r"Analysis of gene expression data can provide insights into insights into the time-lagged co-regulation of genes/gene clusters. However, existing methods such as the Event Method and the Edge Detection Method are inefficient as they compare only two genes at a time. More importantly, they neglect some important information due to their scoring criterian. In this paper, we propose an efficient algorithm to identify time-lagged co-regulated gene clusters. The algorithm facilitates localized comparison and processes several genes simultaneously to generate detailed and complete time-lagged information for genes/gene clusters. We experimented with the time-series Yeast gene dataset and compared our algorithm with the Event Method. Our results show that our algorithm is not only efficient, but also delivers more reliable and detailed information on time-lagged co-regulation between genes/gene clusters.",
            # [3] 按钮颜色 (可选参数，默认 secondary)
            "Color":    r"secondary",
            # [4] 按钮是否可见 (可选参数，默认 True，即可见)
            "Visible": True,
            # [5] 是否在触发时清除历史 (可选参数，默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False,
            # [6] 文本预处理 （可选参数，默认 None）
            "PreProcess": None,
        },
    }


def handle_core_functionality(additional_fn, inputs, history, chatbot):
    import core_functional
    importlib.reload(core_functional)    # 热更新prompt
    core_functional = core_functional.get_core_functions()
    addition = chatbot._cookies['customize_fn_overwrite']
    if additional_fn in addition:
        # 自定义功能
        inputs = addition[additional_fn]["Prefix"] + inputs + addition[additional_fn]["Suffix"]
        return inputs, history
    else:
        # 预制功能
        if "PreProcess" in core_functional[additional_fn]:
            if core_functional[additional_fn]["PreProcess"] is not None:
                inputs = core_functional[additional_fn]["PreProcess"](inputs)  # 获取预处理函数（如果有的话）
        # 为字符串加上上面定义的前缀和后缀。
        inputs = apply_gpt_academic_string_mask_langbased(
            string = core_functional[additional_fn]["Prefix"] + inputs + core_functional[additional_fn]["Suffix"],
            lang_reference = inputs,
        )
        if core_functional[additional_fn].get("AutoClearHistory", False):
            history = []
        return inputs, history

if __name__ == "__main__":
    t = get_core_functions()["总结绘制脑图"]
    print(t["Prefix"] + t["Suffix"])