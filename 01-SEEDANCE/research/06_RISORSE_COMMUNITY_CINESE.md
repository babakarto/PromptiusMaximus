# 06 - RESOURCES FROM THE CHINESE COMMUNITY: Seedance 2.0 / Jimeng (即梦) / Dreamina

## Comprehensive Guide from the Chinese Community Perspective

**Last revised:** March 24, 2026
**Sources:** Zhihu (知乎), Bilibili (B站), CSDN, Tencent News, iFanr, SegmentFault, GitHub, Xiaohongshu (小红书), WeChat, Sohu, Sina, Baidu Baike, and other Chinese platforms.

---

## TABLE OF CONTENTS

1. [Platform Overview and Chinese Ecosystem](#1-platform-overview-and-chinese-ecosystem)
2. [The Universal Prompt Formula (万能公式)](#2-the-universal-prompt-formula-万能公式)
3. [The 8-Dimension Framework (八维度框架)](#3-the-8-dimension-framework-八维度框架)
4. [Complete Camera Movement Vocabulary (运镜词库)](#4-complete-camera-movement-vocabulary-运镜词库)
5. [Lighting Quick Reference Table (光影速查表)](#5-lighting-quick-reference-table-光影速查表)
6. [Style Keywords (风格关键词)](#6-style-keywords-风格关键词)
7. [Constraint and Anti-Deformation Words (约束词)](#7-constraint-and-anti-deformation-words-约束词)
8. [Multimodal Reference System with @ Syntax](#8-multimodal-reference-system-with--syntax)
9. [Creation Modes: First/Last Frame vs Full Reference](#9-creation-modes-firstlast-frame-vs-full-reference)
10. [Complete Prompts from the Chinese Community (with Translation)](#10-complete-prompts-from-the-chinese-community-with-translation)
11. [9-Grid Storyboard Technique (九宫格分镜)](#11-9-grid-storyboard-technique-九宫格分镜)
12. [10 Detailed Official Use Cases](#12-10-detailed-official-use-cases)
13. [Long Video Workflow (over 15 seconds)](#13-long-video-workflow-over-15-seconds)
14. [Chinese vs English: Which Language to Use for Prompts](#14-chinese-vs-english-which-language-to-use-for-prompts)
15. [Common Mistakes Guide and How to Avoid Them (避坑指南)](#15-common-mistakes-guide-and-how-to-avoid-them-避坑指南)
16. [Access Platforms and Credit-Saving Strategies](#16-access-platforms-and-credit-saving-strategies)
17. [Automated Tools: Claude Code Skill for Prompts](#17-automated-tools-claude-code-skill-for-prompts)
18. [API and Developer Access via Volcano Engine](#18-api-and-developer-access-via-volcano-engine)
19. [Technical Architecture (for Advanced Users)](#19-technical-architecture-for-advanced-users)
20. [Bilibili, GitHub and Community Resources](#20-bilibili-github-and-community-resources)
21. [Ready-to-Use Templates by Category](#21-ready-to-use-templates-by-category)
22. [Intensity Words and Degree Adverbs (程度副词)](#22-intensity-words-and-degree-adverbs-程度副词)
23. [Troubleshooting: Debug Flowchart](#23-troubleshooting-debug-flowchart)
24. [Sources and References](#24-sources-and-references)

---

## 1. Platform Overview and Chinese Ecosystem

### What is Seedance 2.0

Seedance 2.0 is the next-generation AI video generation model developed by ByteDance's Seed team, officially launched on **February 7, 2026** on the **Jimeng (即梦)** platform. It has been described by the Chinese community as the **"Black Myth: Wukong moment" of AI video** -- a Chinese product that stunned the entire world.

### Key Features

- **Quad-modal input**: text + images + video + audio simultaneously
- **Native 2K resolution** with generation in ~60 seconds
- **Output duration**: 4-15 seconds per clip
- **Native audio**: sound effects and soundtrack generated automatically
- **Lip-sync**: error under 1 frame, support for 8 languages
- **Success rate**: 90%+ (vs. industry average ~20%)
- **Up to 12 reference files**: max 9 images + 3 videos + 3 audio

### Access Points in the ByteDance Ecosystem

| Platform | URL / App | Notes |
|---|---|---|
| **Jimeng (即梦)** Web | https://jimeng.jianying.com | Full access, all features |
| **Jimeng (即梦)** App | Chinese App Store | Full mobile version |
| **Doubao (豆包)** | https://doubao.com + App | 10 generations/day FREE, no image input |
| **Xiao Yunque (小云雀)** | Chinese App Store | 1200 credits on registration, top choice |
| **Dreamina** | https://dreamina.capcut.com | International version (Seedance 2.0 not yet available as of March 2026) |
| **Volcano Ark** | console.volcengine.com | API for developers |

### Credit System

| Platform | Free Credits | Cost per Video |
|---|---|---|
| Doubao | 10 attempts/day | 5s = 1 attempt, 10s = 2 attempts |
| Xiao Yunque | 1200 on registration + 130/day login | 8 credits/second |
| Jimeng | Limited free access (with watermark) | Variable by duration |

**Money-saving trick from the Chinese community**: Xiao Yunque and Jimeng use separate credit systems. You can register an account on both with the same phone number to double the benefits.

---

## 2. The Universal Prompt Formula (万能公式)

The Chinese community has developed a **universal formula** (万能公式, wanneng gongshi) that represents the base structure for every effective prompt:

### Basic Formula

```
主体 + 动作 + 场景 + 运镜 + 风格 + 画质
Subject + Action + Scene + Camera Movement + Style + Quality
```

### Complete Formula (Recommended)

```
主体 + 动作 + 场景 + 光影 + 镜头语言 + 风格 + 画质 + 约束
Subject + Action + Scene + Lighting + Cinematic Language + Style + Quality + Constraints
```

### S-A-C-S-C Formula (for Commercial Videos)

The 5-step **S-A-C-S-C** (Subject-Action-Camera-Style-Constraint) method is ideal for commercial videos that require precise framing control:

1. **S (Subject/主体)**: Who or what appears -- specific details
2. **A (Action/动作)**: What they do -- present tense verb, a single action
3. **C (Camera/镜头)**: Shot size + movement + angle + focal length
4. **S (Style/风格)**: Visual anchor, lighting, color treatment
5. **C (Constraint/约束)**: Exclusions, timing, consistency rules

### Practical Example of the Formula

**Chinese:**
```
动漫少女在樱花树下慢走，微风拂发，微笑看镜头，黄昏暖光，电影感，稳定跟拍，2K高清
```

**English:**
```
Anime girl walks slowly under a cherry blossom tree, light breeze
through her hair, smiling toward the camera, warm sunset light, cinematic
style, stable tracking, 2K HD
```

---

## 3. The 8-Dimension Framework (八维度框架)

The Chinese community has developed a structured **8-dimension** framework that covers every aspect of a perfect prompt:

### Dimension 1: Subject (主体描述)

Clear description of the character: physical appearance, clothing, hair, age, expression.

**Chinese example:**
```
一位穿白色亚麻连衣裙的年轻女生，长发微卷自然垂落
```
**Translation:** A young woman wearing a white linen dress, long slightly curly hair falling naturally

### Dimension 2: Action (动作描述)

Describe **slow and continuous** actions. Never more than 1-2 actions per clip.

**Chinese example (cafe scene):**
```
坐在咖啡馆靠窗座位，缓慢端起一杯拿铁，轻轻吹了一口热气，抿了一小口，然后抬眼看向窗外
```
**Translation:** Sitting at the window seat of a cafe, slowly lifting a cup of latte, gently blowing on the steam, taking a small sip, then looking up toward the window

### Dimension 3: Scene (场景)

Specific environment with atmospheric details.

**Chinese example:**
```
站在【春日午后】的【日式庭院木廊】上，樱花花瓣缓缓飘落在肩头和发间
```
**Translation:** Standing on the wooden veranda of a Japanese garden on a spring afternoon, cherry blossom petals slowly falling on shoulders and between the hair

### Dimension 4: Lighting (光影)

Color, light direction, temperature, specific effects.

**Chinese example:**
```
暖光从侧面洒入，柔光散射，日系清新暖色调
```
**Translation:** Warm light pouring in from the side, soft diffused light, fresh Japanese-style warm tones

### Dimension 5: Cinematic Language (镜头语言)

Shot type and camera movement.

**Chinese example:**
```
近景，缓慢推镜
```
**Translation:** Close shot, slow dolly-in

### Dimension 6: Style and Atmosphere (风格与氛围)

Overall visual style positioning.

**Chinese example:**
```
日系清新暖色调，电影质感
```
**Translation:** Fresh Japanese warm tones, cinematic texture

### Dimension 7: Quality (画质)

Resolution and texture requirements.

**Chinese example:**
```
4K超高清，细节丰富
```
**Translation:** 4K ultra HD, rich in detail

### Dimension 8: Constraints (约束条件)

Prevention of deformations and artifacts.

**Chinese example:**
```
面部清晰不变形，五官自然，画面稳定无抖动
```
**Translation:** Clear face without deformations, natural features, stable image without shaking

### Complete Prompt with All 8 Dimensions

**Chinese:**
```
一位穿白色亚麻连衣裙的年轻女生，长发微卷自然垂落，站在【春日午后】的
【日式庭院木廊】上，樱花花瓣缓缓飘落在肩头和发间。近景，缓慢推镜，暖光
从侧面洒入，柔光散射，日系清新暖色调，画面稳定无抖动，4K超高清，面部清晰
不变形，五官自然，细节丰富，电影质感。
```

**English:**
```
A young woman wearing a white linen dress, long slightly curly hair
falling naturally, standing on the wooden veranda of a Japanese garden
on a spring afternoon, cherry blossom petals slowly falling on shoulders
and between the hair. Close shot, slow dolly-in, warm light pouring in
from the side, soft diffused light, fresh Japanese-style warm tones,
stable image without shaking, 4K ultra HD, clear face without
deformations, natural features, rich in detail, cinematic texture.
```

---

## 4. Complete Camera Movement Vocabulary (运镜词库)

The Chinese community emphasizes that Seedance 2.0 has an **excellent understanding of camera movements in Chinese** -- no need to translate to English.

### Shot Type (景别)

| Chinese | Pinyin | English | English |
|---|---|---|---|
| 特写 | texi | Close-up | Close-up |
| 近景 | jinjing | Close shot | Close shot |
| 中景 | zhongjing | Medium shot | Medium shot |
| 全景 | quanjing | Full/Wide shot | Full/Wide shot |
| 远景 | yuanjing | Long shot | Long shot |
| 超远景 | chaoyuanjing | Extreme long shot | Extreme long shot |

### Camera Movements (运镜方式)

| Chinese | Pinyin | English | English |
|---|---|---|---|
| 缓慢推镜 | huanman tuijing | Slow dolly in | Slow dolly in |
| 轻微拉远 | qingwei layuan | Slight zoom out | Slight zoom out |
| 平稳横移 | pingwen hengyi | Smooth horizontal truck | Smooth truck |
| 环绕半圈 | huanrao banquan | Semicircular orbit | Half orbit |
| 固定镜头 | guding jingtou | Fixed shot | Static/locked shot |
| 手持稳定 | shochi wending | Stabilized handheld | Steady handheld |
| 跟拍 | genpai | Tracking/follow | Follow shot |
| 俯拍 | fupai | High angle / overhead | High angle / overhead |
| 仰拍 | yangpai | Low angle / contre-plongee | Low angle |
| 环绕拍摄 | huanrao paishe | Orbital shot | Orbit shot |
| 一镜到底 | yijing daodi | One-take / continuous shot | One-take/continuous shot |
| 旋转跟随 | xuanzhuan gensui | Rotating follow | Rotating follow |
| 缓慢下摇 | huanman xiayao | Slow tilt down | Slow tilt down |
| 缓慢上摇 | huanman shangyao | Slow tilt up | Slow tilt up |
| 镜头从下往上慢慢抬起 | jingtou cong xia wang shang manman taiqi | Camera slowly rising from below | Slow crane up |

### Speed Modifiers

| Chinese | English |
|---|---|
| 缓慢 | Slow |
| 轻微 | Slight |
| 平稳 | Stable |
| 丝滑 | Silky/smooth |
| 快速 | Fast |

### Universal Camera Suffixes

```
无抖动、丝滑流畅
No shaking, silky smooth
```

### Comparative Example from the Community

**Slow push-in version:**
```
中景，镜头从街道远处缓慢推近到女生面部特写
```
*Medium shot, the camera slowly pushes in from far down the street to a close-up of the girl's face*

**Orbit version:**
```
中景，镜头从女生正面缓慢环绕到侧面
```
*Medium shot, the camera slowly orbits from the girl's front to her side*

**Static version:**
```
中景，固定机位，画面静止只有人物微微动
```
*Medium shot, fixed camera, static image with only slight character movements*

---

## 5. Lighting Quick Reference Table (光影速查表)

The Chinese community has created a **Scene x Lighting association table** to avoid conflicts between style and light -- one of the most common errors.

### Lighting Keywords

| Chinese | Pinyin | English | English | Typical Use |
|---|---|---|---|---|
| 暖黄阳光 | nuanhuang yangguang | Warm yellow sunlight | Warm yellow sunlight | Relaxing/healing scenes |
| 柔光散射 | rouguang sanshe | Soft diffused light | Soft diffused light | Portraits, beauty |
| 霓虹灯光 | nihong dengguang | Neon light | Neon light | Cyberpunk, nighttime |
| 逆光剪影 | niguang jianying | Backlight/silhouette | Backlight silhouette | Dramatic, artistic |
| 伦勃朗光 | Lunbolang guang | Rembrandt lighting | Rembrandt lighting | Classic portraits |
| 次表面散射 | ci biaomian sanshe | Subsurface scattering | SSS lighting | Realistic skin |
| 体积光 | tiji guang | Volumetric light | Volumetric/god rays | Atmospheric, magical |
| 冷蓝紫色调 | leng lan zi sediao | Cool blue-purple tone | Cool blue-purple tone | Sci-fi, cyberpunk |
| 黄昏暖光 | huanghun nuanguang | Golden hour warm light | Golden hour warm light | Romantic, cinematic |
| 侧光勾勒 | ceguang goule | Side rim light | Side rim light | Fashion, dramatic |
| 柔光漫射 | rouguang manshe | Soft ambient light | Soft ambient light | General, everyday |

### FUNDAMENTAL RULE: Match Light and Style

| Style (风格) | Correct Lighting (光影) | WRONG Lighting |
|---|---|---|
| 赛博朋克 (Cyberpunk) | 霓虹灯光 + 冷蓝紫色调 | 暖黄阳光 |
| 治愈清新 (Healing/Fresh) | 暖黄阳光 + 柔光散射 | 霓虹灯光 |
| 电影感 (Cinematic) | 逆光剪影 + 伦勃朗光 | Flat 柔光漫射 |
| 日系清新 (Fresh Japanese) | 暖光 + 柔光散射 | 冷蓝紫色调 |
| 写实纪录片 (Documentary) | 自然光 + 侧光 | 霓虹灯光 |

> **Note from the community:** "光影和风格打架是最常见的翻车原因之一" -- The conflict between lighting and style is one of the most common causes of failure.

---

## 6. Style Keywords (风格关键词)

### Preset Styles on the Platform

Seedance 2.0 offers 4 main styles in the settings:
- **写实** (Realistic)
- **电影** (Cinematic)
- **动漫** (Anime)
- **赛博朋克** (Cyberpunk)

### Style Vocabulary from the Chinese Community

#### Everyday / Vlog
| Chinese | English |
|---|---|
| 治愈清新 | Healing/fresh |
| 日系清新 | Fresh Japanese style |
| 韩系氛围感 | Korean atmosphere |
| 暖色调 | Warm tones |

#### Sci-Fi / Futuristic
| Chinese | English |
|---|---|
| 赛博朋克 | Cyberpunk |
| 暗调高级 | Dark premium |
| 科技未来感 | Futuristic tech feel |
| 复古胶片 | Retro film |

#### Cinematic
| Chinese | English |
|---|---|
| 电影质感 | Cinematic texture |
| 电影感 | Cinematic feel |
| 胶片颗粒感 | Film grain |
| 变形镜头光晕 | Anamorphic lens flare |

#### Chinese-Specific Styles (Exclusive)
| Chinese | English |
|---|---|
| 国风 | Chinese national style |
| 古风 | Ancient/classical Chinese style |
| 水墨 | Chinese ink and wash |
| 武侠 | Wuxia martial arts |
| 邵氏兄弟武侠电影风格 | Shaw Brothers wuxia film style |

### GOLDEN RULE: One Stylistic Anchor Is Worth Six Adjectives

The Chinese community emphasizes: **don't write "唯美" (beautiful)**, instead write specifically what you mean:

| DON'T write (Vague) | Write THIS (Specific) |
|---|---|
| 唯美 (beautiful) | 治愈清新、日系暖色调、柔光散射 |
| 高级 (high quality) | 赛博朋克、暗调、极简干净 |
| 大片感 (blockbuster feel) | 电影质感、逆光、IMAX画幅比 |

### English Stylistic Anchors (Useful Even in Chinese Prompts)

The community suggests that some English terms can be mixed into Chinese prompts for greater precision:
- "Blade Runner color grade"
- "Studio Ghibli watercolor"
- "Kodak Portra 400 film"
- "Wes Anderson symmetrical framing"
- "bokeh"
- "tilt-shift"
- "cinematic"

---

## 7. Constraint and Anti-Deformation Words (约束词)

### VERY IMPORTANT: Seedance 2.0 Does NOT Support Negative Prompts

> **From the community:** "Seedance 2.0 的模型不会读负面提示词，即使你写了，它也会当没看见"
> *The Seedance 2.0 model does not read negative prompts. Even if you write them, it completely ignores them.*

Therefore: **use specific positive descriptions** instead of saying "don't do X".

### Essential Constraint Words (ALWAYS Add These)

**Chinese:**
```
面部稳定不变形，五官清晰，人体结构正常，比例自然，画面稳定，无抖动，
4K高清，电影质感
```

**English:**
```
Stable face without deformations, clear features, normal body structure,
natural proportions, stable image, no shaking, 4K HD,
cinematic texture
```

### Anti-Deformation Vocabulary for Actions

Fast and wide actions = higher probability of errors. Use these terms:

| Chinese | English | Function |
|---|---|---|
| 缓慢 | Slow | Reduces inter-frame errors |
| 轻柔 | Gentle | Soft movements |
| 连贯 | Coherent | Smooth transitions |
| 自然 | Natural | Realistic appearance |
| 流畅 | Fluid | Without interruptions |
| 不僵硬 | Not stiff | Prevents robotic movements |

### Constraint Templates by Category

**For videos with people:**
```
面部清晰不变形，五官自然，人体结构正常，比例自然，动作自然流畅不僵硬
```

**For product videos:**
```
产品细节清晰，材质质感真实，光影自然，无模糊无重影
```

**For landscapes:**
```
画面丝滑，无闪烁无重影，色彩自然，细节丰富
```

---

## 8. Multimodal Reference System with @ Syntax

### Upload Rules

| Type | Maximum | Limits |
|---|---|---|
| Images | 9 files | - |
| Videos | 3 files | Maximum total duration 15 seconds |
| Audio | 3 files | MP3/WAV, maximum total duration 15 seconds |
| **Total** | **12 files** | - |

### Basic @ Syntax

The @ syntax is the core of the multimodal system. It is used to **assign a specific role to each uploaded file**.

**Basic formula:**
```
@图片1 作为角色参考 @图片2 作为场景参考 @视频1 参考运镜和动作节奏
```
**Translation:**
```
@Image1 as character reference, @Image2 as scene reference,
@Video1 as reference for camera and action rhythm
```

### Optimal File Allocation

The community guide recommends: **5-8 files maximum, no more!**

> "3-5张图片足够。1-2张锁角色，1-2张定场景"
> *3-5 images are enough. 1-2 to lock the character, 1-2 to define the scene.*

**Recommended allocation:**
- 2 character images (角色)
- 1 scene image (场景)
- 1 reference video (运镜)
- 1 audio track (音频)
- + text prompt

> **Warning:** Too many materials confuse the model rather than improving the output!

### Advanced @ Usage Patterns

**First frame + movement reference:**
```
@图1为首帧，参考@视频1的打斗动作
```
*@Image1 as first frame, referencing the fighting actions from @Video1*

**Video extension:**
```
将@视频1延长5s
```
*Extend @Video1 by 5 seconds* (select 5s duration)

**Scene insertion:**
```
在@视频1和@视频2之间加一个场景，内容为xxx
```
*Add a scene between @Video1 and @Video2, the content is xxx*

**Character consistency:**
```
男人@图片1 下班后疲惫地走在走廊……
```
*The man @Image1 walks tiredly through the corridor after work...*

**Multi-material promotional video:**
```
帮我做一个春节快闪类的视频，图片1、图片2、图片3、图片4、图片5、图片6、
图片7、图片8、视频1中的图片和视频，根据音频1进行卡点，运镜风格参考视频2，
使画面中的人物更有过年的喜庆欢乐的氛围，视频最后出现"团圆才是年"的大字结尾
```
*Create a Chinese New Year flash video. Use images 1-8, video 1, sync with Audio 1 on the beats, reference the shooting style from Video 2, make the atmosphere festive and joyful, end with the large text "Reunion is the true New Year"*

**Lip-sync/speaking video:**
```
@图片1 作为角色形象,面对镜头说话,口型与 @音频1 同步, 表情自然亲切,
背景为简洁的书房环境,镜头稳定
```
*@Image1 as character appearance, speaking toward the camera, lip-sync with @Audio1, natural and friendly expression, simple study background, stable camera*

### Audio Priority

> **Rule from the community:** "干声优先" (Clean voice priority)
>
> For speaking videos, use audio without background music to ensure correct lip synchronization.

---

## 9. Creation Modes: First/Last Frame vs Full Reference

### First/Last Frame Mode (首尾帧模式)

**When to use:** For beginners or quick generation with a single image.

**Workflow:**
1. Upload 1 HD image as first frame
2. Write the prompt
3. Set parameters: 9:16 (TikTok/Douyin), 5-8 seconds, 1080P, cinematic style
4. Generate

**Ideal for:** Animating a single image, quick tests, beginners.

### Full Reference Mode (全能参考模式) -- RECOMMENDED

**When to use:** For any project requiring precise control.

**Workflow:**
1. Define the creative objective
2. Organize materials by functional role (character/scene/camera/audio)
3. Upload files (check max 5-8)
4. Use @ syntax to assign each material's role
5. Write the prompt using the 8-dimension formula
6. Generate
7. Evaluate -> Modify prompt or replace materials -> Regenerate

**Community rule:**
> "单图+文字 → 首尾帧；多素材 → 全能参考"
> *Single image + text -> First/Last frame; Multi-material -> Full Reference*

---

## 10. Complete Prompts from the Chinese Community (with Translation)

### Prompt 1: Japanese Cinematic Portrait

**Chinese:**
```
一位穿白色亚麻连衣裙的年轻女生，长发微卷自然垂落，站在春日午后的日式庭院
木廊上，樱花花瓣缓缓飘落在肩头和发间。近景，缓慢推镜，暖光从侧面洒入，
柔光散射，日系清新暖色调，画面稳定无抖动，4K超高清，面部清晰不变形，五官自然，
细节丰富，电影质感。
```

**English:**
Young woman wearing a white linen dress, long slightly wavy hair falling naturally, standing on the wooden veranda of a Japanese garden on a spring afternoon, cherry blossom petals slowly falling on shoulders and between the hair. Close shot, slow dolly-in, warm light from the side, soft diffused light, fresh Japanese warm tones, stable image without shaking, 4K ultra HD, clear face without deformations, natural features, rich in detail, cinematic texture.

---

### Prompt 2: Seaside Sunset (Landscape)

**Chinese:**
```
海边日落，海浪轻拍沙滩，镜头缓慢横移，暖橙色调，治愈清新，画面丝滑，
4K超高清，无闪烁无重影
```

**English:**
Seaside sunset, waves gently lapping the beach, slow horizontal tracking, warm orange tones, fresh and healing, silky image, 4K ultra HD, no flickering no ghosting.

---

### Prompt 3: Image-to-Video with First Frame

**Chinese:**
```
基于参考图保持人物样貌与服装一致，动作缓慢抬手转身，自然流畅，不僵硬不变形，
稳定运镜，高清细节，电影质感
```

**English:**
Based on the reference image, maintain the character's appearance and clothing consistency, action of slowly raising the hand and turning, natural and fluid, not stiff and without deformations, stable camera, HD detail, cinematic texture.

---

### Prompt 4: Wuxia Combat Scene

**Chinese:**
```
这两张图片是一段悬崖对手戏的两个女主，请围绕两个女主，生成一段流畅的红衣
女子东方不败与黑衣女刺客二人对手戏的画面，需要运用到分镜和不同视角切换，
让整个画面更有节奏感和电影感。仅生成打斗音效和环境的音效，不要配背景音乐
```

**English:**
These two images are the two protagonists of a cliff combat scene. Generate a fluid combat scene between the woman in red "Dongfang Bubai" and the black-clad female assassin, using storyboarding and different perspective switches, making the entire scene more rhythmic and cinematic. Generate only combat and environmental sound effects, no background music.

---

### Prompt 5: Food Preparation (Cooking)

**Chinese:**
```
主角进入画面，先往面粉里轻轻撒入盐，然后用手搅拌均匀，接着倒入适量的水，
打入一个鸡蛋，开始揉面团。
```

**English:**
The protagonist enters the frame, first gently sprinkles salt into the flour, then stirs evenly with hands, then pours in the right amount of water, cracks an egg, and starts kneading the dough.

---

### Prompt 6: Talking Head / Lip-Sync Video

**Chinese:**
```
@图片1 作为角色形象,面对镜头说话,口型与 @音频1 同步, 表情自然亲切,
背景为简洁的书房环境,镜头稳定。
```

**English:**
@Image1 as character appearance, speaking toward the camera, lip-sync with @Audio1, natural and friendly expression, simple study background, stable camera.

---

### Prompt 7: Dance Transfer (Choreography)

**Chinese (reference from the ifanr community):**
```
@video1的编舞替换为@image1的两个机器人；保持@image1的场景设置；
参考@video1的运镜和转场
```

**English:**
Replace the choreography from @video1 with the two robots from @image1; maintain the scene setup from @image1; reference the camera movements and transitions from @video1.

---

### Prompt 8: Warm Healing Style (Douyin/TikTok)

**Chinese (Doubao template):**
```
主体+温馨治愈风格，缓慢动作，自然光，柔和光影，细腻画质，1080P，竖屏9:16，
10秒，无模糊卡顿，画面干净清晰
```

**English:**
Subject + warm healing style, slow action, natural light, soft lighting, detailed quality, 1080P, vertical 9:16, 10 seconds, no blur or stuttering, clean and clear image.

---

### Prompt 9: High-Quality Cinematic

**Chinese (Doubao template):**
```
唯美电影质感，慢镜头，运镜流畅，氛围感拉满，高清细节，2K，横屏16:9，
10秒，画面稳定不抖动
```

**English:**
Beautiful cinematic texture, slow motion, fluid camera, atmosphere maxed out, HD details, 2K, horizontal 16:9, 10 seconds, stable image without shaking.

---

### Prompt 10: Universal Walk (Replaceable Template)

**Chinese:**
```
一位年轻女生在[场景]中缓慢行走，微风轻拂头发，自然微笑，[光线描述]，中景，
缓慢推镜，画面流畅稳定，4K高清，电影感，面部清晰不变形，人体结构正常，
细节丰富，15秒。
```

**Replaceable variables:**
- **Scene (场景):** 林间 (forest) / 海边 (beach) / 城市街道 (city street) / 咖啡馆 (cafe) / 樱花树下 (under cherry blossoms)
- **Light (光线):** 暖光光影 (warm light) / 逆光剪影 (backlight/silhouette) / 侧光勾勒 (side rim light) / 柔光漫射 (soft ambient light)

---

### Prompt 11: Surreal Ronin Action (from GitHub Repository)

**English (original from the Chinese community):**
```
A masked warrior battles a winged beast on floating islands during a
thunderstorm, with camera dynamics capturing debris effects and cinematic
lighting as the warrior leaps between crumbling platforms.
```

---

### Prompt 12: Live-Action Anime Duel (from GitHub Repository)

**English (original, 15-second video with timestamps):**
```
15-second samurai battle: [0:00-0:05] Close-up of blue water dragon breathing
technique activation. [0:05-0:10] Wide shot clash with golden lightning versus
blue water effects. [0:10-0:15] Slow-motion final strike with particle effects
dissipating.
```

---

### Prompt 13: Animated Chinese Ink (水墨风)

From singer Zhang Jie's performance with "Yu Feng Ge" (驭风歌):
```
让徐悲鸿《六骏图》中的静态水墨骏马跃然而出，在大屏上自由奔腾
```
**English:** The static ink horses from Xu Beihong's "Six Steeds" come to life and gallop freely across the screen.

*This demonstrates that the model excels at traditional Chinese ink style.*

---

## 11. 9-Grid Storyboard Technique (九宫格分镜)

This is an **exclusive technique from the Chinese community** that leverages Seedance 2.0's ability to interpret image grids as storyboards.

### How It Works

1. Create a single image with 9 panels (3x3 grid)
2. Each panel represents a key frame of the sequence
3. Upload the image as reference
4. Write a minimal prompt

> "如果输入一张九宫格的分镜图片，Seedance 2.0 也可以自己串起来"
> *If you upload a 9-grid storyboard image, Seedance 2.0 can automatically connect them into a sequence.*

### Advantages

- Drastically reduces prompt complexity
- Allows precise visual control of the sequence
- Ideal for those who think "visually" rather than "textually"
- A single image + one sentence = complete video

### How to Create the Grid

1. Generate individual images with an AI tool (Seedream 5.0, Midjourney, etc.)
2. Arrange in a 3x3 grid with any editor
3. Upload as a single reference file
4. Add a brief prompt describing the overall action

---

## 12. 10 Detailed Official Use Cases

Based on the Tencent News article analyzing 10 practical scenarios:

### Case 1: Character Consistency
**Capability:** Maintain action and camera, replace the subject
**Use:** Character replacement, IP adaptation
**Technique:** Specify the transfer between characters in the prompt

### Case 2: Product Consistency
**Capability:** Multi-image fusion, separate control of structure and material
**Use:** E-commerce photography
**Technique:** Use separate @Image for product side and surface texture

### Case 3: Dance Replication
**Capability:** Dual replication of action + camera
**Use:** Dance video creation
**Technique:** Reference both body movements and shooting style simultaneously

### Case 4: Combat Replication
**Capability:** Separate multi-video reference
**Use:** Action scenes
**Technique:** Control action and cinematic language separately

### Case 5: Commercial Spot Replication
**Capability:** Replicate classic advertising rhythm
**Use:** Product promotional videos
**Technique:** Reference camera and cutting rhythm from the original video

### Case 6: Video Extension
**Capability:** "Continue shooting" from where it left off
**Key indicator:** Light and action connect naturally
**Technique:** Maintain identical constraints in the extension prompt

### Case 7: Video Editing (Plot Overhaul)
**Capability:** Partial plot rewriting
**Use:** Creative editing, parodies
**Technique:** Redefine the narrative direction of a segment

### Case 8: Subtitle Special Effects
**Capability:** Particle and text control
**Use:** Title/opening animations
**Technique:** Reference particle effects and material from the video

### Case 9: One-Take Shot (一镜到底)
**Capability:** Spatial coherence and physical plausibility
**Importance:** Key indicator of model maturity
**Use:** Complex tracking in elaborate scenes

### Case 10: Musical Rhythm Synchronization
**Capability:** Audio-video synchronization
**Use:** MVs, landscape videos
**Technique:** Multi-image + video rhythm as reference for editing

> **Key insight from the community:** "Seedance 2.0真正提升的，不是'炫技能力'，而是'控制能力'"
> *What Seedance 2.0 has truly improved is not the "ability to show off effects" but the "ability to control".*

---

## 13. Long Video Workflow (over 15 seconds)

### Method 1: Sequential Relay Extension

1. Generate the first segment (10-13 seconds)
2. Use the output as reference for the next segment
3. **Repeat the constraints** in each extension prompt

**Example extension prompt:**
```
将@视频1延长15s，角色从微笑点头直接过渡到举手示意，保持动作连贯流畅
```
*Extend @Video1 by 15s, the character transitions from smiling and nodding to raising their hand to wave, maintaining coherent and fluid action*

**WARNING:** The duration selection = duration of the NEW part, not the total!

### Method 2: Independent Segments + Editing

1. Generate each segment of 10-13 seconds separately
2. Use the same anchor materials for visual consistency
3. Assemble in editing software

**Transition techniques:**
- **B-roll concealment (B-roll遮切法):** Insert 1-2 seconds of external footage at junction points to mask small inconsistencies, while maintaining audio continuity
- Dissolves
- Hard cuts synchronized with continuous audio

### Quality Limit in Extensions

> **From the community:** Continuous extension beyond 3 iterations degrades quality. Recommendation: **export 30-second segments** as new reference material to "start fresh".

### Constraints for Extensions

> "延长段必须重复原始提示词里的约束词（面部不变形、服装一致等），否则后段人物可能'变脸'"
>
> *Extension segments MUST repeat the constraint words from the original prompt (face without deformations, consistent clothing, etc.), otherwise the character might "change face" in later parts.*

---

## 14. Chinese vs English: Which Language to Use for Prompts

### Community Verdict: CHINESE is Generally Better

Seedance 2.0 was trained by ByteDance and has a **native understanding of Chinese**:

> "Seedance 2.0是字节跳动训练的模型，对中文的理解力是原生级别的"
> *Seedance 2.0 is a model trained by ByteDance, its understanding of Chinese is at a native level*

### Test Results

| Scenario | Best Language |
|---|---|
| 国风/日系/写实 (Chinese style/Japanese/Realistic) | **Chinese** by far |
| Cyberpunk, Sci-Fi | Chinese or English similar |
| Technical cinematography terms | Mix of Chinese + English |
| Emotional, atmospheric descriptions | **Chinese** |

### Community Recommendation

1. **Main descriptions:** Use Chinese
2. **Specific technical terms:** Mix in English when useful (bokeh, tilt-shift, cinematic, Hitchcock zoom)
3. **No need to translate:** Chinese is never worse than English on this model
4. **English works:** But it will NEVER be better than Chinese for most scenarios

> "纯中文效果最稳，纯英文也能用，但不会比中文更好，没有必要专门翻译"
> *Pure Chinese is the most stable, pure English also works but will never be better than Chinese, there's no need to specifically translate*

### Rare Exception

A minority of users have reported that for some **very specific** scenarios, English might give slightly better results. If a Chinese prompt doesn't work, trying the English translation can be a last resort.

---

## 15. Common Mistakes Guide and How to Avoid Them (避坑指南)

### Mistake 1: Incomplete Constraints

> "不管什么场景，提示词末尾都要加约束词，这几个词是安全带，不系就等着翻车"
> *In any scene, ALWAYS add constraint words at the end of the prompt. They are the seatbelt -- without them, expect a crash.*

**Solution:** ALWAYS add at the end: `面部稳定不变形，画面稳定，4K高清`

### Mistake 2: Actions Too Fast or Too Wide

The AI model interpolates between frames. The greater the difference between consecutive frames, the higher the probability of error.

**Solution:** Use exclusively slow and continuous actions. Never write: jumps, fast spins, complex dances.

### Mistake 3: Light/Style Conflict

**Wrong example:** "Cyberpunk" style + "warm sunlight" lighting

**Solution:** Consult the Scene x Lighting Table (Section 5).

### Mistake 4: Wrong @ References

> "素材多的时候，一定反复检查每个@引用有没有对上号"
> *When there are many materials, ALWAYS check multiple times that every @ reference is correct*

**Solution:** Verify 2-3 times every @ reference before generating. Use the hover preview.

### Mistake 5: Too Many Movement Verbs in a Single Clip

**Rule:** One shot = one action verb. Multiple verbs = confusion.

### Mistake 6: Too Many Characters

**Rule:** Maximum 1-2 characters. Beyond 2 causes identity confusion and loss of coherence.

### Mistake 7: Too Many Camera Changes in One Clip

> "Seedance 2.0单次4-15秒，一条提示词里超过2-3个镜头变化，模型就容易乱套"
> *With 4-15 seconds per clip, more than 2-3 shot changes in a single prompt and the model gets confused*

### The 5 Most Common Problems and Solutions

| Problem | Solution |
|---|---|
| 口型不准 (Inaccurate lip-sync) | Use clean audio without music, verify MP3 format |
| 表情僵硬 (Stiff expressions) | Add "表情自然" and describe specific emotion |
| 手部变形 (Deformed hands) | Avoid close-ups on hands, use medium shot |
| 画面抖动 (Image shaking) | Add "画面稳定无抖动" and use fixed camera |
| 背景错误 (Wrong background) | Provide specific scene reference image |

### Debug Order (from the Community)

> **排查口诀:** 约束 → 动作 → 主体 → 风格 → 画质 → 引用 → 时长 → 长度
>
> **Verification order:** Constraints -> Action -> Subject -> Style -> Quality -> @ References -> Duration -> Prompt length

**Fundamental rule:** Change ONLY ONE variable at a time to identify the problem.

### Quick Debug Guide

| Symptom | What to Modify |
|---|---|
| Wrong composition, correct action | Camera only |
| Unnatural movement | Change "handheld" to "gimbal"; specify speed |
| Inconsistent style | Replace with a single stronger stylistic anchor |
| Recurring artifacts | Change constraint words or shot size |
| Chaotic angles | Switch to "single tracking shot" |

---

## 16. Access Platforms and Credit-Saving Strategies

### Platform Comparison for Non-Chinese Users

| Platform | Requires China VPN? | Requires +86? | Free Credits | Features |
|---|---|---|---|---|
| Jimeng Web | Yes | Yes (or Douyin) | Limited free with watermark | Full |
| Doubao App | HK VPN recommended | No (Google account) | 10 gen/day | Limited (no image refs) |
| Xiao Yunque App | Yes | Yes | 1200 + 130/day | Full |
| CyberBara | No | No | Few free | Full |
| Volcano Ark API | No | Business account | Pay-per-use | API only |

### Credit-Saving Strategies from the Community

1. **Generate in 1080P first** to test, then regenerate in 2K only if satisfied
2. **Start with 5 seconds** to verify direction, then extend if needed
3. **Use multiple accounts** on different platforms (Jimeng + Xiao Yunque)
4. **Accumulate daily credits** that never expire
5. **Daily login** for bonus credits
6. **Monthly subscription** at 69 RMB/month (1080 credits) = 0.065 RMB/credit for heavy use
7. **Invite friends** for bonus credits on Xiao Yunque

### Hidden Trick

> In Xiao Yunque's Fast mode, credits are occasionally not deducted. Take advantage of time-limited benefits when available.

---

## 17. Automated Tools: Claude Code Skill for Prompts

The Chinese community has developed several **Claude Code Skills** specifically for automatically generating professional Seedance 2.0 prompts.

### Seedance Prompt Skill (by songguoxs)

**Repository:** https://github.com/songguoxs/seedance-prompt-skill

**Capabilities:**
- Pure text generation
- Consistency control via references
- Camera/movement replication
- VFX replication
- Story completion
- Video extension
- Sound design
- One-take sequences
- Video editing
- Musical synchronization

**4-step workflow:**
1. Describe your idea in natural language
2. Claude confirms parameters (duration, aspect ratio, references, style)
3. Claude generates 2-3 versions of the prompt
4. Iteration to refine

**Includes built-in libraries for:**
- Cinematic language (shot types, movements, angles)
- Visual styles (film grain, color palettes, artistic movements, lighting)

### Seedance 2.0 Storyboard Generator (by liangdabiao)

**Repository:** https://github.com/liangdabiao/Seedance2-Storyboard-Generator

Converts novels/stories into multi-episode screenplays optimized for Seedance 2.0:
1. Conceive the theme
2. Write the screenplay
3. Generate material descriptions
4. Generate images
5. Write storyboard scripts
6. Generate video episode by episode

### Availability on Coze

The Seedance 2.0 Claude Agent Skill is also available for free in the Coze skills store for immediate use without setup.

---

## 18. API and Developer Access via Volcano Engine

### API Status (March 2026)

The official Seedance 2.0 API is available through ByteDance's **Volcano Engine (火山引擎)** platform.

**SDK Documentation:** https://www.volcengine.com/docs/82379/1366799

### API Features

- Joint audio-video multi-modal architecture
- Support for text-to-video, image-to-video, video-to-video
- Native 2K resolution
- Multi-shot storytelling
- Multi-image reference input

### How to Access

1. Register at console.volcengine.com
2. Request API permissions for the Seedance 2.0 model
3. Follow the SDK documentation for integration
4. Pay-per-use payment model

### WARNING: Fake APIs

> The community warns about the presence of **fake API services** reselling unauthorized access. Use ONLY the official Volcano Engine channels.

---

## 19. Technical Architecture (for Advanced Users)

### 5-Layer Architecture

1. **Multi-Modal Input Encoding**
2. **Spatio-Temporal Modeling**
3. **Parallel Generation**
4. **Optimization Calibration**
5. **Output Delivery**

### Dual-Branch Diffusion Transformer

The fundamental innovation: generates **images and audio in parallel** through cross-modal attention mechanism (unlike sequential models that cause audio-video misalignment).

> "生成画面与音频并行运算，基于音频-画面跨模态注意力机制"

### Spatio-Temporal Causal Modeling (STCM)

Physics-aware video generation through 3 phases:
1. Causal relationship extraction
2. Physical parameter simulation
3. Inter-frame continuity optimization

The system calculates object trajectories, velocities, and collision physics to ensure logical coherence.

### Intelligent Cinematography Engine

Supports 10+ professional camera modes: tracking, pan, tilt, orbit, overhead, crane, with automatic shot planning and smooth transitions synchronized with audio rhythm.

### Current Technical Limitations

- Resolution: 640x640 up to 834x1112 pixels (for input)
- Historical/specialized knowledge not always accurate
- Facial expressions for complex emotions still stiff
- Maximum 60 seconds of video (with extensions)

---

## 20. Bilibili, GitHub and Community Resources

### Bilibili Tutorials (B站)

| Title | URL | Content |
|---|---|---|
| AI Filmmaking Super Tutorial | https://www.bilibili.com/video/BV1sGcxzPEBj/ | From basics to AI short film creation |
| Most Complete Seedance 2.0 Tutorial | https://www.bilibili.com/video/BV11Dc5zBE7d/ | Full coverage of all features |
| Complete Collection of Practical Uses | https://www.bilibili.com/video/BV1gPZXBCEb9/ | All real use cases |
| 30 Cases with Complete Prompts | https://www.bilibili.com/video/BV1gCcqzkEe7/ | 30 cases + public prompts |
| 3D Rendering Workflow | https://www.bilibili.com/video/BV1AJPxzgEah/ | 3D previz workflow |
| Team Storyboard with AI | https://www.bilibili.com/video/BV153PFzSEku/ | From script to final video |
| 2026 Complete Tutorial (保姆级) | https://www.bilibili.com/video/BV1oUfcByEXD/ | 100 episodes, from beginner to expert |

### GitHub Repositories

| Repository | URL | Content |
|---|---|---|
| awesome-seedance-2-prompts | https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts | 1099+ curated prompts |
| seedance2.0-how-to | https://github.com/ZeroLu/seedance2.0-how-to | Access guide + prompt engineering |
| seedance-prompt-skill | https://github.com/songguoxs/seedance-prompt-skill | Claude Code Skill for prompts |
| Seedance2-Storyboard-Generator | https://github.com/liangdabiao/Seedance2-Storyboard-Generator | Screenplay generator |
| seedance2.0 (Web App) | https://github.com/wwwzhouhui/seedance2.0 | React + Express Web App |
| seedance-prompt-guide | https://github.com/rich5000/seedance-prompt-guide | Prompt guide |
| seedance2.0-prompt-skill | https://github.com/MapleShaw/seedance2.0-prompt-skill | Alternative skill |

### Online Prompt Sites

| Site | URL | Content |
|---|---|---|
| Seedance 2 Prompts (500+) | https://seedance2prompt.org/ | Collection of 500+ prompts |
| YouMind Prompts | https://youmind.com/seedance-2-0-prompts | High-signal prompts |
| Seedance Video Guide | https://seedancevideo.com/prompt-guide/ | Complete guide |
| PromptsRef Library | https://promptsref.com/library/seedance-2.0 | Reference library |
| Dreamina Official | https://dreamina.capcut.com/resource/seedance-2-0-prompt | 18 powerful prompts |

### Key Chinese Articles

| Source | Title | URL |
|---|---|---|
| Zhihu | Seedance 2.0 提示词攻略：10分钟出电影感视频 | https://zhuanlan.zhihu.com/p/2005428746417640272 |
| Zhihu | Seedance 2.0实操教程 | https://zhuanlan.zhihu.com/p/2004523300588643639 |
| Zhihu | 即梦Seedance 2.0喂饭教程 | https://zhuanlan.zhihu.com/p/2004623893273519265 |
| Zhihu | 九宫格分镜+Seedance 2.0 | https://zhuanlan.zhihu.com/p/2004236766274672108 |
| Zhihu | Claude Code 100%出片 | https://zhuanlan.zhihu.com/p/2004270375060661803 |
| Zhihu | 2026 完整版提示词攻略 | https://zhuanlan.zhihu.com/p/2017950956378141300 |
| iFanr | 中国AI视频的"黑神话"时刻 | https://www.ifanr.com/1654856 |
| Tencent News | 10个案例一次讲清楚 | https://news.qq.com/rain/a/20260213A06ETQ00 |
| Tencent News | 通用提示词公式 | https://news.qq.com/rain/a/20260307A04T5A00 |
| Tencent News | 完整操作手册 | https://news.qq.com/rain/a/20260209A044NZ00 |
| CSDN | 全能参考完全指南 | https://blog.csdn.net/u014177256/article/details/158013628 |
| SegmentFault | 技术深度解析 | https://segmentfault.com/a/1190000047604020 |

### Official ByteDance Manual (Feishu/Lark)

**URL:** https://bytedance.larkoffice.com/wiki/A5RHwWhoBiOnjukIIw6cu5ybnXQ

This is the official internal ByteDance document containing the complete guide with all templates and official specifications.

---

## 21. Ready-to-Use Templates by Category

### UGC/Influencer Template

**Chinese:**
```
主体 + 手持手机视角，微微晃动的自然质感，竖屏9:16，10秒，1080P，
自然光，表情生动，画面清晰
```
**English:** Subject + handheld smartphone perspective, natural texture with slight wobble, vertical 9:16, 10 seconds, 1080P, natural light, lively expressions, clear image

### Product Advertisement Template

**Chinese:**
```
产品近景到中近景，柔光灯箱，@图片1为产品正面，缓慢旋转展示，
背景模糊散景，商业质感，画面稳定，4K
```
**English:** Product from close shot to medium close shot, softbox, @Image1 as product front, slow rotation showcase, background with bokeh, commercial texture, stable image, 4K

### Cinematic Scene Template

**Chinese:**
```
云台稳定跟拍，消色调电影色彩，胶片颗粒感，主体在[场景]中[动作]，
16:9横屏，10秒，2K，画面稳定不抖动
```
**English:** Gimbal-stabilized tracking, desaturated cinematic colors, film grain, subject in [scene] doing [action], 16:9 horizontal, 10 seconds, 2K, stable image without shaking

### Talking Head / Presenter Template

**Chinese:**
```
中近景，三脚架锁定，45度柔光主灯，主体面对镜头说话，口型与@音频1同步，
表情自然，背景简洁，1080P，9:16
```
**English:** Medium close shot, tripod locked, 45-degree soft key light, subject speaking to camera, lip-sync with @Audio1, natural expression, simple background, 1080P, 9:16

### Combat Scene Template

**Chinese:**
```
先远景确立场景，然后中景跟拍打斗动作，最后近景冲击特写，
动作力度感强，音效同步，邵氏兄弟武侠电影风格
```
**English:** First long shot to establish the scene, then medium shot tracking for combat action, finally close-up impact shot, strong sense of force in actions, synchronized sound effects, Shaw Brothers wuxia film style

### Music Video Template

**Chinese:**
```
多角度混合镜头，@音频1为背景音乐，画面切换与节拍同步，
灯光效果动态变化，主体@图片1在舞台表演，2K，16:9
```
**English:** Mixed angles multi-shot, @Audio1 as background music, image cuts synced with the beat, dynamically changing light effects, subject @Image1 performing on stage, 2K, 16:9

### Ancient Chinese Style Template (国风/古风)

**Chinese:**
```
水墨画风格，一位古装女子在竹林间缓步行走，长袖飘动，仙气飘渺，
远景缓慢推近，中国传统水墨色调，意境悠远，画面丝滑，4K
```
**English:** Ink painting style, a woman in traditional clothing walks slowly through bamboo groves, long sleeves flowing, ethereal and mystical aura, long shot slowly pushing in, traditional Chinese ink tones, profound and distant atmosphere, silky image, 4K

### Quick Montage Template

**Chinese:**
```
4个节拍，每个约2秒，@图片1-@图片4依次展示，
灯光统一，@音频1卡点切换，节奏感强，1080P
```
**English:** 4 beats, approximately 2 seconds each, @Image1-@Image4 displayed in sequence, uniform lighting, cuts synced with @Audio1, strong sense of rhythm, 1080P

---

## 22. Intensity Words and Degree Adverbs (程度副词)

Intensity words are **critical** for controlling the amplitude and speed of movement. The Chinese community has categorized them:

### Gentle Movement (Recommended to Avoid Artifacts)

| Chinese | English | English |
|---|---|---|
| 缓慢地 | Slowly | Slowly |
| 轻轻地 | Gently | Gently |
| 微微地 | Slightly | Slightly |
| 细微地 | Subtly | Subtly |
| 几乎不可察觉地 | Barely/imperceptibly | Barely/imperceptibly |

### Intense Movement (Use with Caution)

| Chinese | English | English |
|---|---|---|
| 快速地 | Quickly/rapidly | Quickly/rapidly |
| 猛烈地 | Violently/powerfully | Violently/powerfully |
| 大幅度地 | With large amplitude | With large amplitude |
| 疯狂地 | Frantically/crazily | Frantically/crazily |
| 剧烈地 | Dramatically/vigorously | Dramatically/vigorously |

### Rhythmic Movement

| Chinese | English | English |
|---|---|---|
| 有节奏地 | Rhythmically | Rhythmically |
| 平稳地 | Smoothly/steadily | Smoothly/steadily |
| 流畅地 | Fluidly | Fluidly |

### Example of the Difference

**Vague (avoid):**
```
车转弯 (The car turns)
```

**Specific (correct):**
```
轮胎冒烟，车猛烈漂移90度，橡胶在柏油路上尖叫
```
*The tires smoke, the car drifts violently 90 degrees, rubber screaming on the asphalt*

---

## 23. Troubleshooting: Debug Flowchart

### Systematic Verification Order

```
1. CONSTRAINTS (约束) - Are they there? Are they complete?
   ↓ If OK
2. ACTION (动作) - Is it too fast/complex?
   ↓ If OK
3. SUBJECT (主体) - Is the description clear and specific?
   ↓ If OK
4. STYLE (风格) - Is it consistent with the lighting?
   ↓ If OK
5. QUALITY (画质) - Are the parameters appropriate?
   ↓ If OK
6. @ REFERENCES (引用) - Are they correct and not conflicting?
   ↓ If OK
7. DURATION (时长) - Is the duration appropriate for the content?
   ↓ If OK
8. PROMPT LENGTH (长度) - Is the prompt between 30-200 words?
```

### Iteration Strategy

1. **First generation:** Test in 1080P, 5 seconds
2. **If not satisfied:** Modify ONLY ONE variable
3. **If satisfied:** Regenerate in 2K, full duration
4. **Generate 2-4 variants** for comparison

### Platform Limitations to Know

- **Real face restriction:** ByteDance temporarily limited the use of real face photos after launch to prevent deepfakes. Recommended alternatives are animation or AI-generated characters.
- **"Non-compliant content" error:** May appear if the content violates platform rules (real faces, sensitive content).
- **Audio errors:** Occasional voice synchronization issues and incorrect subtitles in spoken content.

---

## 24. Sources and References

### Zhihu Articles (知乎)
- [Seedance 2.0 提示词攻略：掌握这套公式，10分钟出电影感视频](https://zhuanlan.zhihu.com/p/2005428746417640272)
- [Seedance 2.0实操教程](https://zhuanlan.zhihu.com/p/2004523300588643639)
- [即梦Seedance 2.0喂饭教程](https://zhuanlan.zhihu.com/p/2004623893273519265)
- [爆火全网！Seedance 2.0 震撼发布：九宫格分镜](https://zhuanlan.zhihu.com/p/2004236766274672108)
- [别再盲目抽卡了！Claude Code 100%出片](https://zhuanlan.zhihu.com/p/2004270375060661803)
- [Seedance 2.0杀入豆包！附一手实测](https://zhuanlan.zhihu.com/p/2005055167784035723)
- [2026 完整版提示词攻略](https://zhuanlan.zhihu.com/p/2017950956378141300)
- [免费薅字节最强AI视频生成器](https://zhuanlan.zhihu.com/p/2004138628176168008)
- [如何评价即梦新发布的视频模型 Seedance 2.0？](https://www.zhihu.com/question/2003476733446349730)
- [Seedance 2.0 深度拆解](https://zhuanlan.zhihu.com/p/2004687441341215106)

### Tencent News (腾讯新闻)
- [即梦 Seedance 2.0通用提示词公式](https://news.qq.com/rain/a/20260307A04T5A00)
- [即梦Seedance2.0 官方手册](https://news.qq.com/rain/a/20260227A04RFZ00)
- [Seedance 2.0 完整操作手册](https://news.qq.com/rain/a/20260209A044NZ00)
- [即梦 Seedance 2.0 使用教程：10个案例](https://news.qq.com/rain/a/20260213A06ETQ00)
- [Seedance 2.0 最全上手指南](https://news.qq.com/rain/a/20260213A02AB700)

### CSDN and Technical Blogs
- [80+提示词 Seedance 2.0 提示词完全指南](https://blog.csdn.net/mizzlelover/article/details/158040401)
- [字节即梦Seedance 2.0使用手册](https://blog.csdn.net/seoread/article/details/157937583)
- [全能参考完全指南](https://blog.csdn.net/u014177256/article/details/158013628)
- [豆包 Seedance 2.0 入门教程](https://blog.csdn.net/belldeep/article/details/158290740)
- [Seedance 2.0 技术深度解析](https://segmentfault.com/a/1190000047604020)

### International Platforms
- [Dreamina Official Seedance 2.0 Prompts](https://dreamina.capcut.com/resource/seedance-2-0-prompt)
- [Seedance 2.0 Usage Guide (Redreamality)](https://redreamality.com/blog/seedance-2-guide/)
- [Seedance 2 Prompts - 500+ Examples](https://seedance2prompt.org/)
- [Seedance Prompt Guide (SeedanceVideo)](https://seedancevideo.com/prompt-guide/)

### GitHub Repositories
- [awesome-seedance-2-prompts (1099+ prompts)](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts)
- [seedance2.0-how-to](https://github.com/ZeroLu/seedance2.0-how-to)
- [seedance-prompt-skill](https://github.com/songguoxs/seedance-prompt-skill)
- [Seedance2-Storyboard-Generator](https://github.com/liangdabiao/Seedance2-Storyboard-Generator)

### Other Sources
- [iFanr: 即梦 Seedance 2.0 黑神话时刻](https://www.ifanr.com/1654856)
- [苏米客: 创作提示词手册](https://www.xmsumi.com/detail/2432)
- [实在智能: seedance2.0提示词有哪些](https://www.ai-indeed.com/encyclopedia/15752.html)
- [fly63: 提示词超全汇总](https://fly63.com/article/detial/13338)
- [Volcano Engine SDK](https://www.volcengine.com/docs/82379/1366799)
- [Baidu Baike: Seedance2.0](https://baike.baidu.com/item/Seedance2.0/67358557)

### Bilibili Videos
- [即梦Seedance2.0 AI影视创作最细教程](https://www.bilibili.com/video/BV1sGcxzPEBj/)
- [全网最完整Seedance2.0使用教程](https://www.bilibili.com/video/BV11Dc5zBE7d/)
- [Seedance2.0全网最全实战用法合集](https://www.bilibili.com/video/BV1gPZXBCEb9/)
- [30个用法案例+完整提示词](https://www.bilibili.com/video/BV1gCcqzkEe7/)
- [2026最新版即梦SD2保姆级教程](https://www.bilibili.com/video/BV1oUfcByEXD/)

### Official ByteDance Document
- [即梦官方学习手册 (Feishu/Lark)](https://bytedance.larkoffice.com/wiki/A5RHwWhoBiOnjukIIw6cu5ybnXQ)

---

## SUMMARY OF GOLDEN RULES FROM THE CHINESE COMMUNITY

1. **One shot = one verb** -- Never multiple actions in one clip
2. **Maximum 1-2 characters** -- Beyond 2 causes identity confusion
3. **30-200 words** is the optimal prompt length
4. **ALWAYS add constraints** at the end of the prompt
5. **Negative prompts DO NOT work** -- Describe what you WANT
6. **Generate short first (5s)** then extend
7. **One variable at a time** when debugging
8. **Chinese is the best language** for this model
9. **5-8 reference files maximum** -- Too many confuse the model
10. **Light and style must match** -- Conflict is the #1 killer
11. **Slow and continuous movements** -- Fast actions cause artifacts
12. **One strong stylistic anchor** is worth more than six vague adjectives
13. **ALWAYS check @ references** -- One mistake ruins everything
14. **Test in 1080P** before spending credits on 2K

---

*Document compiled from in-depth research on Chinese community platforms: Zhihu, Bilibili, CSDN, Tencent News, iFanr, SegmentFault, GitHub, Baidu Baike, Sohu, Sina, and official ByteDance resources. All Chinese prompts are presented in the original language with English translation.*
