# V02｜15 秒总片第一次尝试：失败版本

状态：**失败 FAILED**。原文件：[video-02-MASTER-15s-roll1-FAILED.txt](source__JackDaniels_BornFromFire_Workflow_Pack__06-Prompts__video-02-MASTER-15s-roll1-FAILED.txt)。

## 这条用来做什么

第一次尝试在一段视频里串起人物、焦木、酒滴、倒酒与酒瓶五段。

**先看这一点：先看第一版让人物“待着”，再看下一版怎样补出动作与运镜触发。**

## 原始设置的中文说明

这些是作者记录的请求设置，不是当前渠道可用性或输出规格的保证。

| 项目 | 原始记载 |
|---|---|
| 模型代号 | seedance_2_0 |
| 请求时长 | 15s |
| 请求分辨率 | 1080p |
| 请求画幅 | 16:9 |
| 生成音频 | on |
| 原附件记载 | image_1 = master distiller (Midjourney source, locked identity), image_2 = reference image, image_3 = reference image, image_4 = reference image, image_5 = locked bottle hero plate (2K) |

## 中文完整译文

以下依据英文正文翻译，分段仅为易读；不把整理者注释放入提示词。不声称中文译文已经生成验证。

```text
参考图说明：<<<image_1>>> 是饱经风霜的酿酒大师、火光中的伦勃朗式肖像；<<<image_2>>> 是焦黑橡木桶内壁上的火焰微距；<<<image_3>>> 是黑木炭上方的一滴琥珀色威士忌；<<<image_4>>> 是威士忌浇过方冰、一只饱经风霜的手；<<<image_5>>> 是暖色火光中的 Old No. 7 方瓶。

风格与氛围：电影级照片写实，柯达 Vision3 500T 钨丝灯胶片效果，细腻 35mm 颗粒，变形宽银幕观感。唯一光源是火光，暗部深近黑，采用暖琥珀与黑色配色，精致、低沉，全程富有运动能量，每一帧都鲜活，不要定格。

动态描述：手持中近景缓慢推向火光中的酿酒师（<<<image_1>>>），焦点从柔软的前景火焰转移到他的眼睛，余烬在暗处上升；随后摄影机猛地向右甩动，以运动模糊甩离人物。

甩镜进入焦黑桶沿的极近微距环绕（<<<image_2>>>）。鲜活橙色火焰沿鳄鱼皮状焦壳快速蔓延，火星向镜头迸出，焦点沿燃烧线移动；在一颗飞溅火星上突然硬切。

一次快速向下的纵向甩镜追随一滴晶亮琥珀色酒液（<<<image_3>>>），它落向黑色糖枫木炭；焦点迅速锁定酒滴，运动通过变速转入慢动作，接触炭面的位置扩散出一圈柔和痕迹，随后借这圈形状做匹配剪辑。

稳定的环绕镜头扫过厚重水晶杯（<<<image_4>>>），琥珀色威士忌浇在透明方冰上，火光透过酒液折射金色，飞溅配合速度变化；酿酒师那只饱经风霜的手举起杯子，摄影机随之上仰，再向上甩离。

向上甩镜衔接流畅连续的摇臂下降，落到 Old No. 7 方瓶（<<<image_5>>>）。火焰持续活动，余烬上升，运动轻柔收束到停留展示；瓶身上方保留深色留白，黑色正面标签清楚可读。

静态描述：黑暗中只有一处温暖火光，全程有木烟和漂浮余烬；酿酒师穿深炭灰工作衬衫和帆布围裙；新制美国白橡木桶烧焦的内壁；粗糙黑木炭；厚重水晶威士忌杯与方冰；深色反光台面上，一只带黑底奶白与白色字体酒标、盛着琥珀色威士忌的杰克丹尼 Old No. 7 方瓶；四周深近黑。

音频：只用场内音效。持续低沉的火焰轰鸣和噼啪，每次甩镜带一记掠过声（whoosh），一声被放大的滴落、一记冰裂，以及低沉有共鸣的室内底噪。没有音乐，没有配乐，没有歌曲。
```

## 新手解读与对应边界

- 原设置只明确图 1 是人物、图 5 是产品；图 2—4 的文件名没有完整记载。正文可推知内容，但第 4 张旧倒酒图在包中缺失。
- 作者原有中文包含“胖像”“坜向”等错字。本译文依据英文整理，不改动原始提交文件。
- 这里可分析输入设计的差异；因没有失败视频，不能做逐帧的失败前后效果对照。

## 看结果时检查

- 人物是否有明确、可观察的行为
- 甩镜是否有画面中的触发
- 手与杯子的互动是否给整次生成增加负担

## 关联素材

这里是相关文件，不是自动上传清单；确切顺序与不确定项见上方原设置和说明。

- [01-References/master-distiller-locked-midjourney.png](source__JackDaniels_BornFromFire_Workflow_Pack__01-References__master-distiller-locked-midjourney.webp)
- [02-Keyframes/keyframe-char-barrel.png](source__JackDaniels_BornFromFire_Workflow_Pack__02-Keyframes__keyframe-char-barrel.webp)
- [02-Keyframes/keyframe-charcoal-drip.png](source__JackDaniels_BornFromFire_Workflow_Pack__02-Keyframes__keyframe-charcoal-drip.webp)
- [02-Keyframes/keyframe-bottle-hero-plate.png](source__JackDaniels_BornFromFire_Workflow_Pack__02-Keyframes__keyframe-bottle-hero-plate.webp)

## 原始提交正文

保持原文内容，仅省略正文首尾空行。视频文件本来就含作者的中英混合文本；错字没有改写。完整源文件在顶部链接。

```text
<<<image_1>>> = weathered master distiller, firelit Rembrandt portrait; <<<image_2>>> = macro flame on charred oak barrel interior; <<<image_3>>> = a single amber whiskey drop above black charcoal; <<<image_4>>> = amber whiskey pouring over a square ice cube, a weathered hand; <<<image_5>>> = the square Old No. 7 bottle in a firelight pool. Style & Mood: Cinematic photoreal, Kodak Vision3 500T tungsten film stock, fine 35mm grain, anamorphic, firelight as the only light source, deep crushed near-black shadows, warm amber-and-black palette, premium and moody, kinetic energy throughout, every frame alive, no freeze frames. Dynamic Description: A handheld medium close-up pushes slowly in on the firelit master distiller (<<<image_1>>>), the focus racking from a soft foreground flame to his eyes as embers rise through the dark, then the camera whip-pans hard to the right, motion-blurring off him. Whip-pan in to an extreme close-up macro orbit around the charred barrel rim (<<<image_2>>>), live orange flame racing along the alligatored char as sparks spit toward the lens, focus racking down the burning line, then a hard smash cut on a flying spark. A fast vertical whip-down chases a single glistening amber drop (<<<image_3>>>) falling toward black sugar-maple charcoal, the focus snapping onto the drop as it eases into a speed-ramped slow motion, a soft ring spreading where it meets the charcoal, then a match cut on the ring. A stabilized orbit sweeps around a heavy crystal glass (<<<image_4>>>) as amber whiskey pours over a clear square ice cube, firelight refracting gold through the liquid, the splash hitting in a speed-ramp, and the camera tilts up as the distiller's weathered hand lifts the glass, then whips up and away. Whip up to a smooth continuous crane-down on the square Old No. 7 bottle (<<<image_5>>>), the fire alive and embers rising, the move easing into a held lock with dark negative space above the bottle, the black front label staying sharp and readable. Static Description: A single warm firelight source in darkness, drifting wood-smoke and floating embers throughout; a weathered distiller in a dark charcoal work shirt and canvas apron; a new charred American white oak barrel interior; rough black charcoal; a heavy crystal rocks glass with a square ice cube; the square Jack Daniel's Old No. 7 bottle with its black cream-and-white label and amber whiskey on a dark reflective surface; deep near-black surroundings. Audio: diegetic SFX only, low fire roar and crackle throughout, a whoosh on each whip transition, a single amplified drip, an ice crack, a low resonant room tone. No music, no score, no song. 镜头参考：<<<image_1>>>=饱经风霜的酿酒师，火光伦勃朗胖像；<<<image_2>>>=焦炭橡木桶内壁火焰微距；<<<image_3>>>=黑炭上方一滴琥珀色威士忌；<<<image_4>>>=威士忌浇过方形冰块、一只苍老的手；<<<image_5>>>=火光池中的Old No.7方瓶。风格与氛围：电影感写实，柯达Vision3 500T钨丝胶片，细腻35mm颗粒，宽银幕变形宽镜感，唯一光源为火光，深邃压暗黑位，暖琥珀与黑色调，高端低沉，全程充满动感，每一帧都在运动，无定格画面。动态描述：手持中近景缓缓推进火光中的酿酒师（<<<image_1>>>），焦点由柔和的前景火焰拉移至他的双眼，余烬在暗处升腾，随后镜头向右猛地甩镜，带motion blur甩离他。甩镜切入一段焦炭橡木桶边缘的极特写微距环绕（<<<image_2>>>），橙色活火沿鲗裂焦炭飞窜，火星朝镜头迸射，焦点沿燃烧线下移，随后在飞溅火星上硬切。一记快速纵向甩镜追随一滴晶亮的琥珀色酒滴（<<<image_3>>>）坜向黑色糖枫木炭，焦点猛地锁定酒滴，变速升格放慢，落点处一圈柔和涩漪扩散，随后在涩漪上匹配剪辑。稳定环绕扫过一只厚重水晶杯（<<<image_4>>>），琥珀色威士忌浇过透明方形冰块，火光在酒液中折射出金光，水花以变速溅起，镜头随酿酒师苍老的手举杯而上仰，随后向上甩离。向上甩镜接一个流畅连续的摇臂下降，落于Old No.7方瓶（<<<image_5>>>），火焰鲜活、余烬上升，运镜轻柔收束为锁定镜头，瓶身上方留深色负空间，黑色正面标签保持清晰可读。静态描述：黑暗中唯一温暖火光源，全程飘散木烟与漂浮余烬；身着深炭色工装衡衫与帆布围裙的酿酒师；新烧焦的美国白橡木桶内壁；粗糙黑炭；厚重水晶杯与方形冰块；杰克丹尼Old No.7方瓶带黑底奶白字标签、琥珀色威士忌，置于暗色反光台面；四周深近黑色。音频：仅环境音效，全程低沉火焰轰鸣与噪啪，每次甩镜转场一记whoosh，一声放大的滴落，一记冰裂，低沉室内底噪。无音乐、无配乐、无歌曲。
```
