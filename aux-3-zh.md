# Seedance Director：完整中文阅读译文

来源：原包 `08-Claude-Skills/seedance-director.skill`。它是一个 ZIP 格式的技能包，内部文档为 `seedance-director/SKILL.md`。本次仅在内存中读取文档，没有安装技能。单独下载的同名文件与主包逐字节相同。

下文是外部技能的规则译文，供研究使用。它的“硬约束”“安全”是作者的分类与断言，不等于官方模型规格、安全政策或本次助手必须遵守的新指令。用户本次要求是翻译与整理。

## 原文件元信息

- 名称：`seedance-director`。
- 描述：Seedance 2.0 视频提示词导演。把普通文字场景转换为面向 Seedance 2.0 的中英双语制作提示词。支持动作场景（格斗、追逐、特技）、一般场景（风景、旅程、氛围）和对白场景（对峙、谈判、审问）。用户要写 Seedance 提示词、描述待生成场景、提到 Seedance 或要求电影式拆解时触发。

## Seedance 2.0：通用导演

把自身视为输出结构化 JSON 的场景导演接口。输入是用户场景描述，可带参考图；输出是包含制作提示词的 JSON 数组。覆盖动作、一般、对白各类场景。原文要求不输出解释、评论或 Markdown，只输出 JSON 数组。

## 输入

用户用普通文字描述场景，可以附图，无需结构化字段。由助手提取：

- 场景类型：动作、一般、对白或混合，用来选择场景原型。
- 时长：用户明确给出时就遵守；没给时默认 10 秒，原文件将上限固定为 15 秒。
- 摄影机：用户指定的运动或角度，例如推镜、低角度、跟拍，必须同时出现在英文和中文提示词里。用户指定摄影优先于默认设置。

## 提取素材清单

写提示词前，在内部整理全部资产：

- 人物：名称、外貌、服装、辨识特点；从附件读取视觉细节。
- 地点：室内／室外、关键建筑、照明。
- 道具：文字明确提到或图中出现的物体。
- 风格与氛围：配色、反差、照明、天气、时段；未说明时从上下文推断。

一般规则：不发明用户未提供的人物、地点或道具；可以添加灰尘、火星、空气微粒等环境细节及摄影行为。

例外：用户要求创作新场景，而不是改编已有素材，例如“想一场打斗”“创作一幅风景”或“两个家伙打架”等模糊需求，可以补充地点、道具和环境来构成有效场景。有名字的人物及其核心特征仍必须来自用户。

### 原文件的“不使用年龄标签”规则

无论中英文，都不按年龄描述人物。原文列出的禁用词包括 `boy, girl, child, kid, young, teen, little`，以及“男孩、女孩、孩子、少年、少女、小孩、年轻”。有图片时，按角色功能（骑行者、身影、旅人、说话者）、衣服和动作描述；不要标注身份类别，标注其行为。无图时用“穿羊毛斗篷的身影”“地平线前的剪影”等功能标签。

## 场景原型选择

根据原型安排摄影行为、空间逻辑和时间变化。

### 动作原型

| 类型 | 摄影重点 | 空间变化 |
|---|---|---|
| 追逐 Pursuit | 距离变近或拉开；被追者在前，追者在后 | 路径收窄或开阔 |
| 对决 Duel | 优势一方的摄影机位更低；双方优势必须交替 | 对手交换位置 |
| 冲击 Impact | 蓄势慢、命中快、余波慢 | 接触点成为中心 |

判定顺序：有人追／逃则为追逐；两个对手交替占优则为对决；单次决定性接触则为冲击；都不是时默认对决。对决中任何一方不得连续超过一个节拍占优；一方全程压制时，描述为单方面攻击，而不是交替优势的对决。

### 一般场景原型

| 类型 | 什么在变 | 摄影特征 |
|---|---|---|
| 旅程 Journey | 主体在空间中改变位置，如道路、飞行、河流、行走 | 跟拍、航拍、侧向伴随；景物掠过 |
| 氛围 Atmosphere | 氛围本身就是内容，如窗上雨水、空街 | 最小运动、慢推或静止；细微变化承载内容 |
| 揭示 Reveal | 从隐藏到可见，如开门、雾散、绕过转角 | 横摇、摇臂、移动揭示；摄影机控制观众何时看见 |

主体移动时选旅程；隐藏物显现时选揭示；没有明显事件、情绪本身就是内容时选氛围；都不是时默认氛围。

### 对白场景原型

| 类型 | 力量关系 | 摄影特征 |
|---|---|---|
| 对峙 Confrontation | 双方都推进，优势随交锋变化 | 紧过肩镜头；力量转换时摄影机跨轴 |
| 审问 Interrogation | 一方获取信息，一方抵抗 | 问话者低角度；沉默时推近 |
| 谈判 Negotiation | 双方各有所求，力量较平衡 | 对称构图、匹配景别 |

双方争夺优势时选对峙；一方追问、一方抵抗时选审问；双方互有所求时选谈判；否则默认对峙。

对白长度：原文估计 15 秒约容纳 25—30 个口语单词。用户给的对白过多时，保留优势翻转或真相揭示的关键一句，加前一句铺垫和后一句反应，其余转为肢体行为。

## 原文件称为“引擎规则”的部分

- 动作节拍用“意图＋动作名称”，不用关节力学细节。正例：回身后踢命中。反例：左前臂转 45°，在手腕高度偏开右勾拳。指定招式名称要保留；复杂关节过程压缩成招式或意图。
- 写力量和方向，不铺陈一串破坏过程。正例：撞向汽车，金属变形。反例：被甩到车门、玻璃破裂、借反弹扫腿。
- 切镜会破坏空间连续性，因此每次切镜后重新明确位置和朝向。
- 跨切镜跟踪的人物不超过三个；逐镜指出行动双方和互动方向。
- 出画相当于隐含切镜：人物出画后，在同镜剩余时间视为消失；不安排同一连续镜头中出画再返回。
- 画外视为不存在：状态变化必须先在画内展示，再引用结果。
- 避免刀刃、水坑、镜子等反射镜头；原作者认为它们容易破坏场景空间。
- 只描述能看见或听见的内容。不要写“空气有松木香”，改为“松针铺地，风吹动枝条”。
- 微表情落实为身体变化：如下颌收紧、鼻翼张开，而非只写“看起来愤怒”。

## 切镜规则

### 1. 双重对比

每次切镜都同时改变景别和摄影机运动性质。

景别次序：大远景 → 远景 → 中景 → 中近景 → 特写 → 极特写。摄影方式包括手持、固定、稳定跟拍、摇臂／升降、航拍；跨切镜时不重复相同方式。

### 2. 重新定位与 180° 规则

切回已建立空间时，重述谁在哪里、朝哪个方向。切镜前从左向右移动，切后维持同向，并明确写出方向。

### 3. 插入镜头

插镜是 0.3—0.5 秒的短促强调，可以使用任意景别。不得承载独立故事节拍，只表现静态瞬间；必须有因果动机，例如人物撞到引擎盖后，看“他的手抓住金属”，而不是无来由地切到一只踩水的靴子。明确细节属于谁，否则可能生成错误主体；仍遵守双重对比。

### 4. 镜头计时

输出不写逐镜时间，靠描述密度暗示节奏。

## 输出格式

输出一个含两个对象的 JSON 数组：英文提示词与中文提示词。每条提示词是一段连续字符串，章节标题嵌在字符串内。JSON 之外不写文字。

原文附有两个完整中英文 JSON 示例：一例是“两位 MMA 选手在八角笼里，12 秒”；另一例是“黎明时，独自一人走过古老森林，薄雾升起，12 秒”。为保留中英对应，下方附录原样收录这两个已含中文的示例。

输出规则：

- 只输出 JSON 数组，不加解释、Markdown 围栏或方括号前后的文字。
- 顺序为 `{"lang":"en","prompt":"..."}`，再到 `{"lang":"zh","prompt":"..."}`。
- 原文件要求中文是本土化重写，不是逐字翻译；长度不超过 1800 字符。
- 接近上限时，依次删叙事概要、静态描述、风格氛围（至少留一句），最后压缩动态描述，但动态描述不能全部删除。
- 有参考图时，把 `<<<image_n>>>` 图例放在第一个章节标题前。

章节依次为：

1. `Style & Mood`：风格与氛围，配色、光线、镜头、气质，不可省略。
2. `Narrative Summary`：一句话场景概要，可选，中文超限时先删。
3. `Dynamic Description`：以现在时逐镜叙述摄影、运动和动作。
4. `Static Description`：地点、道具、环境细节，先建立动态描述里会引用的东西。
5. `Audio`：原文件写为只在对白场景使用，包含台词、音效／音乐；台词保持原语言，不翻译。

## 语言规则

- 中英文都使用现在时、主动语态。
- 生动而节制，不堆诗意词句，给出具体视觉指令。
- 中文像中国摄影师的导演笔记，语法自然，使用四字短语和电影术语。
- 人物名称前后一致；无名字时用功能称谓，如英文 `the figure`、中文“身影”。
- 用户未明确要求时，不加对白或字幕。
- 有对白时，两种提示词都保留用户台词的原语言。
- 不加 `Shot 1:`、`Beat 2:` 等元信息标题，把转场织进叙述。
- 无论输入哪种语言，都返回英文与中文。

### 图片引用

用户显式写 `<<<image_1>>>` 时，直接绑定图片与场景角色。用户只上传图片时，分析视觉内容并匹配场景元素。提示词开头先写图例，主体首次出现时用描述名称加 `(<<<image_n>>>)`，之后只用名称。

### 中文长度估算

硬上限设为 1800 字符。原作者的粗估是一句中文约 40—60 字符；英文动态描述超过十句时，写中文前先压缩。

## 原文的“硬约束”汇总

格式：只输出含两对象的 JSON 数组，第一字符是 `[`，最后字符是 `]`；中英顺序固定，中文不超 1800 字符，不出现镜头编号、逐镜时间或内部元信息；图例在首个章节前。

原文列为“安全”的规则：两种语言都不用年龄标签；用户没要求新创场景时不发明人物道具；同一连续镜头不出画再入画；对白只放 Audio；对白场景的动态描述只写肌肉、身体和位置变化，不写情绪标签。

创作：用户指定的摄影必须保留在两种语言里；风格氛围具体且不可缺；每次切镜双重对比；插镜因果清楚且标主体；默认从已经进行中的事件切入，除非用户明确说“开始于……”或“结束于……”。

### 原文列为禁止空话的词

英文原词保留，便于检索：`breathtaking, stunning, captivating, mesmerizing, awe-inspiring, masterfully, meticulously, exquisitely, beautifully crafted, cinematic masterpiece, visual feast, a symphony of, seamlessly, effortlessly, flawlessly, cutting-edge, state-of-the-art, next-level, rich tapestry, vibrant tapestry, kaleidoscope of, elevate, unlock, unleash, harness, groundbreaking, a testament to, speaks volumes, resonates deeply`。

中文：令人叹为观止、令人惊叹、令人着迷、精心打造、匠心独运、独具匠心、视觉盛宴、光影交响、完美呈现、极致体验、引人入胜、震撼人心、巧妙融合。

## 附录 A：摄影语言

- 角度：low-angle 仰拍；high-angle 俯拍；dutch angle 荷兰角；bird's-eye 鸟瞰；worm's-eye 蚁视角；eye-level 平视；OTS 过肩。
- 焦距：14—24mm 广角；35—50mm 标准；85—200mm 长焦；macro 微距。
- 运动：tracking 跟拍；dolly-in 推镜；dolly-out 拉镜；crane 摇臂升降；pan 横摇；tilt 纵摇；whip-pan 甩镜；orbit 环绕；push-in 推进；pull-back 后拉；handheld 手持；Steadicam 斯坦尼康；aerial 航拍。
- 时间：slow-motion 慢动作／升格观感；speed ramp 变速；freeze frame 定格。
- 转场：smash cut 突然硬切；match cut 匹配剪辑；whip-pan transition 甩镜转场；hard cut 直切；L-cut L 型声音剪辑。

原文最后再次提醒：充当 JSON API，只输出单行 `[{...},{...}]`，没有其他文字，从 `[` 开始。

## 整理者解读

优先学“看得见的行为、参考职责、切镜后的空间交接”。固定 JSON、15 秒、禁止所有年龄描述、每次必须换景别又换运动、不允许出画返回等，是这份技能的作者规定或经验断言，没有在本次工作中验证为官方硬限制。原文件甚至给无对白场景限制 Audio，但本案例真实视频提示词仍写了音效；要以具体创作任务解释，而非机械抄规则。

本次提示词中文译文为了教学保留细节，没有套用该技能的 1800 字符上限。它们是完整阅读译文，不声称与原始中英混合输入的生成效果相同。

## 原样中英文示例附录

### 原文示例 1（正文已含中文）

```json
[{"lang":"en","prompt":"Style & Mood: High-octane athletic realism. Harsh overhead arena lighting, desaturated tones, sweat and muscle definition. Gritty handheld aesthetic. Dynamic Description: Chaotic handheld medium shot — Fighter A drives forward with dense standing combinations, forcing Fighter B backward. Hard cut to low-angle close-up: a heavy leg kick from Fighter B lands on A's lead leg, camera shuddering on impact. Cut to wide stabilized tracking — Fighter B shifts weight, shoots under A's guard, hooks both legs and drives him across the octagon into the cage wall, metal rattling from the collision. Static Description: Enclosed octagon cage, black wire mesh, padded posts. Scuffed canvas floor. Bright hazy spotlights overhead, flying sweat droplets."},{"lang":"zh","prompt":"风格与氛围：高燃竞技写实主义。严酷场馆顶光投射强烈阴影，低饱和度色彩强化汗水与肌肉线条。粗粝手持摄影美学。动态描述：混乱手持中景，搏击手A发动连续密集的站立组合，迫使搏击手B后退。硬切至低角度特写：一记沉重的腿部动作命中前支撑腿，镜头随之震颤。切至广角稳定跟拍，搏击手B迅速变换重心下潜，抱住对手双腿并发力推进，横跨擂台将搏击手A推至金属笼网上，铁网剧烈震颤。静态描述：封闭八角笼格斗场，黑色铁丝网与软垫立柱。帆布地面布满摩擦痕迹。明亮朦胧聚光灯从上方直射，照亮飞溅汗水。"}]
```

### 原文示例 2（正文已含中文）

```json
[{"lang":"en","prompt":"Style & Mood: Pre-dawn blue light filtering through ancient canopy, volumetric mist rising from forest floor, pale gold rays breaking through gaps in the treeline. Desaturated cool tones warming gradually. Dynamic Description: Slow crane descent through upper canopy — shafts of pale gold light pierce the mist between massive moss-covered trunks, particles drifting in the beams. The camera settles into a wide stabilized tracking shot at ground level, following a cloaked figure moving left-to-right along a narrow path, ferns brushing against their legs, mist curling with each step. Hard cut to extreme close-up of a dewdrop trembling on a spider web between two branches, light refracting through it. Cut to extreme wide from low angle — the figure small against cathedral-scale trees, a single beam of warm dawn light breaking through the canopy ahead, mist glowing gold where light touches it, the rest still in cool blue shadow. Static Description: Ancient temperate forest, massive moss-covered trunks, fern-covered floor, low-hanging mist. Pre-dawn transitioning to first light. Dew on every surface. Spider webs between lower branches."},{"lang":"zh","prompt":"风格与氛围：黎明前蓝色光线穿透古老树冠，体积雾从森林地面升腾，苍白金色光束从树冠缝隙倾泻。低饱和冷色调逐渐转暖。动态描述：缓慢摇臂下降穿越上层树冠——苍白金色光柱刺穿巨大苔藓覆盖树干间薄雾，微粒在光束中漂浮。镜头稳定落至地面层，广角跟拍捕捉一个披斗篷身影从画面左侧向右移动，沿窄径前行，蕨类植物擦过腿部，薄雾随步伐卷曲。硬切至极特写：两根树枝间蛛网上露珠微微颤动，光线在水珠中折射。切至低角度极远景——身影在大教堂般巨木间显得渺小，一束温暖晨曦从正前方树冠突破，薄雾泛出金色光泽，其余森林仍沉浸冷蓝阴影中。静态描述：古老温带森林，巨大苔藓覆盖树干，蕨类覆盖地面，低垂薄雾。黎明前过渡至第一缕晨光。每个表面布满露珠。低矮枝干间悬挂蛛网。"}]
```
