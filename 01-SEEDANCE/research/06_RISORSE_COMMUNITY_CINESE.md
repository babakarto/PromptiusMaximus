# 06 - RISORSE DALLA COMMUNITY CINESE: Seedance 2.0 / Jimeng (即梦) / Dreamina

## Guida Completa dalla Prospettiva della Community Cinese

**Ultima revisione:** 24 Marzo 2026
**Fonti:** Zhihu (知乎), Bilibili (B站), CSDN, Tencent News, iFanr, SegmentFault, GitHub, Xiaohongshu (小红书), WeChat, Sohu, Sina, Baidu Baike, e altre piattaforme cinesi.

---

## INDICE

1. [Panoramica della Piattaforma e Ecosistema Cinese](#1-panoramica-della-piattaforma-e-ecosistema-cinese)
2. [La Formula Universale dei Prompt (万能公式)](#2-la-formula-universale-dei-prompt-万能公式)
3. [Il Framework a 8 Dimensioni (八维度框架)](#3-il-framework-a-8-dimensioni-八维度框架)
4. [Vocabolario Completo dei Movimenti di Camera (运镜词库)](#4-vocabolario-completo-dei-movimenti-di-camera-运镜词库)
5. [Tabella di Riferimento Rapido Illuminazione (光影速查表)](#5-tabella-di-riferimento-rapido-illuminazione-光影速查表)
6. [Parole Chiave di Stile (风格关键词)](#6-parole-chiave-di-stile-风格关键词)
7. [Parole di Vincolo e Anti-Deformazione (约束词)](#7-parole-di-vincolo-e-anti-deformazione-约束词)
8. [Sistema di Riferimento Multimodale con Sintassi @](#8-sistema-di-riferimento-multimodale-con-sintassi-)
9. [Modalita di Creazione: Primo/Ultimo Frame vs Riferimento Completo](#9-modalita-di-creazione-primoul-timo-frame-vs-riferimento-completo)
10. [Prompt Completi dalla Community Cinese (con Traduzione)](#10-prompt-completi-dalla-community-cinese-con-traduzione)
11. [Tecnica della Griglia 9 Riquadri (九宫格分镜)](#11-tecnica-della-griglia-9-riquadri-九宫格分镜)
12. [10 Casi d'Uso Ufficiali Dettagliati](#12-10-casi-duso-ufficiali-dettagliati)
13. [Workflow per Video Lunghi (oltre 15 secondi)](#13-workflow-per-video-lunghi-oltre-15-secondi)
14. [Cinese vs Inglese: Quale Lingua Usare per i Prompt](#14-cinese-vs-inglese-quale-lingua-usare-per-i-prompt)
15. [Guida agli Errori Comuni e Come Evitarli (避坑指南)](#15-guida-agli-errori-comuni-e-come-evitarli-避坑指南)
16. [Piattaforme di Accesso e Strategie di Risparmio Crediti](#16-piattaforme-di-accesso-e-strategie-di-risparmio-crediti)
17. [Strumenti Automatici: Claude Code Skill per Prompt](#17-strumenti-automatici-claude-code-skill-per-prompt)
18. [API e Accesso Sviluppatori via Volcano Engine](#18-api-e-accesso-sviluppatori-via-volcano-engine)
19. [Architettura Tecnica (per Utenti Avanzati)](#19-architettura-tecnica-per-utenti-avanzati)
20. [Risorse Bilibili, GitHub e Community](#20-risorse-bilibili-github-e-community)
21. [Template Pronti all'Uso per Categoria](#21-template-pronti-alluso-per-categoria)
22. [Parole di Intensita e Avverbi di Grado (程度副词)](#22-parole-di-intensita-e-avverbi-di-grado-程度副词)
23. [Risoluzione Problemi: Flowchart di Debug](#23-risoluzione-problemi-flowchart-di-debug)
24. [Fonti e Riferimenti](#24-fonti-e-riferimenti)

---

## 1. Panoramica della Piattaforma e Ecosistema Cinese

### Cos'e Seedance 2.0

Seedance 2.0 e il modello di generazione video AI di nuova generazione sviluppato dal team Seed di ByteDance, lanciato ufficialmente il **7 febbraio 2026** sulla piattaforma **Jimeng (即梦)**. E stato descritto dalla community cinese come il **"momento Black Myth: Wukong" dell'AI video** -- un prodotto cinese che ha stupito il mondo intero.

### Caratteristiche Principali

- **Input quad-modale**: testo + immagini + video + audio contemporaneamente
- **Risoluzione nativa 2K** con generazione in ~60 secondi
- **Durata output**: 4-15 secondi per clip
- **Audio nativo**: effetti sonori e colonna sonora generati automaticamente
- **Lip-sync**: errore inferiore a 1 frame, supporto per 8 lingue
- **Tasso di successo**: 90%+ (vs. media del settore ~20%)
- **Fino a 12 file di riferimento**: max 9 immagini + 3 video + 3 audio

### Punti di Accesso nell'Ecosistema ByteDance

| Piattaforma | URL / App | Note |
|---|---|---|
| **Jimeng (即梦)** Web | https://jimeng.jianying.com | Accesso completo, tutte le funzionalita |
| **Jimeng (即梦)** App | App Store cinese | Versione mobile completa |
| **Doubao (豆包)** | https://doubao.com + App | 10 generazioni/giorno GRATIS, no input immagine |
| **Xiao Yunque (小云雀)** | App Store cinese | 1200 crediti alla registrazione, scelta top |
| **Dreamina** | https://dreamina.capcut.com | Versione internazionale (Seedance 2.0 non ancora disponibile a marzo 2026) |
| **Volcano Ark** | console.volcengine.com | API per sviluppatori |

### Sistema Crediti

| Piattaforma | Crediti Gratuiti | Costo per Video |
|---|---|---|
| Doubao | 10 tentativi/giorno | 5s = 1 tentativo, 10s = 2 tentativi |
| Xiao Yunque | 1200 alla registrazione + 130/giorno login | 8 crediti/secondo |
| Jimeng | Accesso gratuito limitato (con watermark) | Variabile per durata |

**Trucco risparmio dalla community cinese**: Xiao Yunque e Jimeng usano sistemi di crediti separati. Si puo registrare un account su entrambe con lo stesso numero di telefono per raddoppiare i benefici.

---

## 2. La Formula Universale dei Prompt (万能公式)

La community cinese ha sviluppato una **formula universale** (万能公式, wanneng gongshi) che rappresenta la struttura base per ogni prompt efficace:

### Formula Base

```
主体 + 动作 + 场景 + 运镜 + 风格 + 画质
Soggetto + Azione + Scena + Movimento Camera + Stile + Qualita
```

### Formula Completa (Raccomandata)

```
主体 + 动作 + 场景 + 光影 + 镜头语言 + 风格 + 画质 + 约束
Soggetto + Azione + Scena + Illuminazione + Linguaggio Cinematografico + Stile + Qualita + Vincoli
```

### Formula S-A-C-S-C (per Video Commerciali)

Il metodo a 5 passaggi **S-A-C-S-C** (Subject-Action-Camera-Style-Constraint) e ideale per video commerciali che richiedono controllo preciso dell'inquadratura:

1. **S (Subject/主体)**: Chi o cosa appare -- dettagli specifici
2. **A (Action/动作)**: Cosa fa -- verbo al presente, una singola azione
3. **C (Camera/镜头)**: Dimensione inquadratura + movimento + angolo + focale
4. **S (Style/风格)**: Ancoraggio visivo, illuminazione, trattamento colore
5. **C (Constraint/约束)**: Esclusioni, tempistica, regole di coerenza

### Esempio Pratico della Formula

**Cinese:**
```
动漫少女在樱花树下慢走，微风拂发，微笑看镜头，黄昏暖光，电影感，稳定跟拍，2K高清
```

**Italiano:**
```
Ragazza anime cammina lentamente sotto un ciliegio in fiore, brezza leggera
tra i capelli, sorride verso la camera, luce calda del tramonto, stile
cinematografico, tracking stabile, 2K HD
```

---

## 3. Il Framework a 8 Dimensioni (八维度框架)

La community cinese ha sviluppato un framework strutturato a **8 dimensioni** che copre ogni aspetto di un prompt perfetto:

### Dimensione 1: Soggetto (主体描述)

Descrizione chiara del personaggio: aspetto fisico, abbigliamento, capelli, eta, espressione.

**Esempio cinese:**
```
一位穿白色亚麻连衣裙的年轻女生，长发微卷自然垂落
```
**Traduzione:** Una giovane donna con un vestito di lino bianco, capelli lunghi leggermente ricci che cadono naturalmente

### Dimensione 2: Azione (动作描述)

Descrivere azioni **lente e continue**. Mai piu di 1-2 azioni per clip.

**Esempio cinese (scena caffe):**
```
坐在咖啡馆靠窗座位，缓慢端起一杯拿铁，轻轻吹了一口热气，抿了一小口，然后抬眼看向窗外
```
**Traduzione:** Seduta al posto vicino alla finestra del caffe, solleva lentamente una tazza di latte, soffia delicatamente sul vapore, prende un piccolo sorso, poi alza gli occhi guardando fuori dalla finestra

### Dimensione 3: Scena (场景)

Ambiente specifico con dettagli atmosferici.

**Esempio cinese:**
```
站在【春日午后】的【日式庭院木廊】上，樱花花瓣缓缓飘落在肩头和发间
```
**Traduzione:** In piedi sulla veranda di legno di un giardino giapponese in un pomeriggio primaverile, petali di ciliegio che cadono lentamente sulle spalle e tra i capelli

### Dimensione 4: Illuminazione (光影)

Colore, direzione della luce, temperatura, effetti specifici.

**Esempio cinese:**
```
暖光从侧面洒入，柔光散射，日系清新暖色调
```
**Traduzione:** Luce calda che entra dal lato, luce diffusa morbida, tonalita calda in stile giapponese fresco

### Dimensione 5: Linguaggio Cinematografico (镜头语言)

Tipo di inquadratura e movimento della camera.

**Esempio cinese:**
```
近景，缓慢推镜
```
**Traduzione:** Primo piano, dolly-in lento

### Dimensione 6: Stile e Atmosfera (风格与氛围)

Posizionamento dello stile visivo complessivo.

**Esempio cinese:**
```
日系清新暖色调，电影质感
```
**Traduzione:** Tonalita calda giapponese fresca, texture cinematografica

### Dimensione 7: Qualita (画质)

Risoluzione e requisiti di texture.

**Esempio cinese:**
```
4K超高清，细节丰富
```
**Traduzione:** 4K ultra HD, ricco di dettagli

### Dimensione 8: Vincoli (约束条件)

Prevenzione deformazioni e artefatti.

**Esempio cinese:**
```
面部清晰不变形，五官自然，画面稳定无抖动
```
**Traduzione:** Volto chiaro senza deformazioni, lineamenti naturali, immagine stabile senza tremolii

### Prompt Completo con Tutte le 8 Dimensioni

**Cinese:**
```
一位穿白色亚麻连衣裙的年轻女生，长发微卷自然垂落，站在【春日午后】的
【日式庭院木廊】上，樱花花瓣缓缓飘落在肩头和发间。近景，缓慢推镜，暖光
从侧面洒入，柔光散射，日系清新暖色调，画面稳定无抖动，4K超高清，面部清晰
不变形，五官自然，细节丰富，电影质感。
```

**Italiano:**
```
Una giovane donna con un vestito di lino bianco, capelli lunghi leggermente
ricci che cadono naturalmente, in piedi sulla veranda di legno di un giardino
giapponese in un pomeriggio primaverile, petali di ciliegio che cadono
lentamente sulle spalle e tra i capelli. Primo piano, dolly-in lento, luce
calda che entra dal lato, luce diffusa morbida, tonalita calda in stile
giapponese fresco, immagine stabile senza tremolii, 4K ultra HD, volto chiaro
senza deformazioni, lineamenti naturali, ricco di dettagli, texture cinematografica.
```

---

## 4. Vocabolario Completo dei Movimenti di Camera (运镜词库)

La community cinese sottolinea che Seedance 2.0 ha un'**eccellente comprensione dei movimenti di camera in cinese** -- non serve tradurre in inglese.

### Tipo di Inquadratura (景别)

| Cinese | Pinyin | Italiano | Inglese |
|---|---|---|---|
| 特写 | texi | Primo piano stretto | Close-up |
| 近景 | jinjing | Primo piano | Close shot |
| 中景 | zhongjing | Piano medio | Medium shot |
| 全景 | quanjing | Piano totale | Full/Wide shot |
| 远景 | yuanjing | Campo lungo | Long shot |
| 超远景 | chaoyuanjing | Campo lunghissimo | Extreme long shot |

### Movimenti di Camera (运镜方式)

| Cinese | Pinyin | Italiano | Inglese |
|---|---|---|---|
| 缓慢推镜 | huanman tuijing | Dolly-in lento | Slow dolly in |
| 轻微拉远 | qingwei layuan | Zoom-out leggero | Slight zoom out |
| 平稳横移 | pingwen hengyi | Carrellata orizzontale stabile | Smooth truck |
| 环绕半圈 | huanrao banquan | Orbita semicircolare | Half orbit |
| 固定镜头 | guding jingtou | Inquadratura fissa | Static/locked shot |
| 手持稳定 | shochi wending | Handheld stabilizzato | Steady handheld |
| 跟拍 | genpai | Tracking/seguimento | Follow shot |
| 俯拍 | fupai | Dall'alto / plongee | High angle / overhead |
| 仰拍 | yangpai | Dal basso / contre-plongee | Low angle |
| 环绕拍摄 | huanrao paishe | Ripresa orbitale | Orbit shot |
| 一镜到底 | yijing daodi | Piano sequenza | One-take/continuous shot |
| 旋转跟随 | xuanzhuan gensui | Rotazione con seguimento | Rotating follow |
| 缓慢下摇 | huanman xiayao | Tilt-down lento | Slow tilt down |
| 缓慢上摇 | huanman shangyao | Tilt-up lento | Slow tilt up |
| 镜头从下往上慢慢抬起 | jingtou cong xia wang shang manman taiqi | Camera che si alza lentamente dal basso | Slow crane up |

### Modificatori di Velocita

| Cinese | Italiano |
|---|---|
| 缓慢 | Lento |
| 轻微 | Leggero |
| 平稳 | Stabile |
| 丝滑 | Setoso/fluido |
| 快速 | Rapido |

### Suffissi Universali per la Camera

```
无抖动、丝滑流畅
Senza tremolii, setosamente fluido
```

### Esempio Comparativo dalla Community

**Versione con push-in lento:**
```
中景，镜头从街道远处缓慢推近到女生面部特写
```
*Piano medio, la camera si avvicina lentamente dalla strada fino al primo piano del volto della ragazza*

**Versione con orbita:**
```
中景，镜头从女生正面缓慢环绕到侧面
```
*Piano medio, la camera ruota lentamente dal fronte al lato della ragazza*

**Versione statica:**
```
中景，固定机位，画面静止只有人物微微动
```
*Piano medio, camera fissa, immagine statica con solo leggeri movimenti del personaggio*

---

## 5. Tabella di Riferimento Rapido Illuminazione (光影速查表)

La community cinese ha creato una **tabella di associazione Scena x Illuminazione** per evitare conflitti tra stile e luce -- uno degli errori piu comuni.

### Parole Chiave di Illuminazione

| Cinese | Pinyin | Italiano | Inglese | Uso Tipico |
|---|---|---|---|---|
| 暖黄阳光 | nuanhuang yangguang | Luce solare calda gialla | Warm yellow sunlight | Scene rilassanti/guarigione |
| 柔光散射 | rouguang sanshe | Luce morbida diffusa | Soft diffused light | Ritratti, beauty |
| 霓虹灯光 | nihong dengguang | Luce al neon | Neon light | Cyberpunk, notturno |
| 逆光剪影 | niguang jianying | Controluce/silhouette | Backlight silhouette | Drammatico, artistico |
| 伦勃朗光 | Lunbolang guang | Luce Rembrandt | Rembrandt lighting | Ritratti classici |
| 次表面散射 | ci biaomian sanshe | Subsurface scattering | SSS lighting | Pelle realistica |
| 体积光 | tiji guang | Luce volumetrica | Volumetric/god rays | Atmosferico, magico |
| 冷蓝紫色调 | leng lan zi sediao | Tonalita fredda blu-viola | Cool blue-purple tone | Sci-fi, cyberpunk |
| 黄昏暖光 | huanghun nuanguang | Luce calda del tramonto | Golden hour warm light | Romantico, cinematografico |
| 侧光勾勒 | ceguang goule | Luce laterale di contorno | Side rim light | Moda, drammatico |
| 柔光漫射 | rouguang manshe | Luce morbida diffusa | Soft ambient light | Generale, quotidiano |

### REGOLA FONDAMENTALE: Associare Luce e Stile

| Stile (风格) | Illuminazione Corretta (光影) | Illuminazione SBAGLIATA |
|---|---|---|
| 赛博朋克 (Cyberpunk) | 霓虹灯光 + 冷蓝紫色调 | 暖黄阳光 |
| 治愈清新 (Healing/Fresh) | 暖黄阳光 + 柔光散射 | 霓虹灯光 |
| 电影感 (Cinematografico) | 逆光剪影 + 伦勃朗光 | 柔光漫射 piatto |
| 日系清新 (Giapponese fresco) | 暖光 + 柔光散射 | 冷蓝紫色调 |
| 写实纪录片 (Documentario) | 自然光 + 侧光 | 霓虹灯光 |

> **Nota dalla community:** "光影和风格打架是最常见的翻车原因之一" -- Il conflitto tra illuminazione e stile e una delle cause piu comuni di fallimento.

---

## 6. Parole Chiave di Stile (风格关键词)

### Stili Preimpostati nella Piattaforma

Seedance 2.0 offre 4 stili principali nelle impostazioni:
- **写实** (Realistico)
- **电影** (Cinematografico)
- **动漫** (Anime)
- **赛博朋克** (Cyberpunk)

### Vocabolario Stili dalla Community Cinese

#### Quotidiano / Vlog
| Cinese | Italiano |
|---|---|
| 治愈清新 | Guarigione/fresco |
| 日系清新 | Stile giapponese fresco |
| 韩系氛围感 | Atmosfera coreana |
| 暖色调 | Tonalita calda |

#### Sci-Fi / Futuristico
| Cinese | Italiano |
|---|---|
| 赛博朋克 | Cyberpunk |
| 暗调高级 | Dark premium |
| 科技未来感 | Sensazione tecnologica futuristica |
| 复古胶片 | Film retrò |

#### Cinematografico
| Cinese | Italiano |
|---|---|
| 电影质感 | Texture cinematografica |
| 电影感 | Sensazione cinematografica |
| 胶片颗粒感 | Grana della pellicola |
| 变形镜头光晕 | Lens flare anamorfico |

#### Stili Specifici Cinesi (Esclusivi)
| Cinese | Italiano |
|---|---|
| 国风 | Stile nazionale cinese |
| 古风 | Stile antico/classico cinese |
| 水墨 | Inchiostro e acquerello cinese |
| 武侠 | Arti marziali wuxia |
| 邵氏兄弟武侠电影风格 | Stile film wuxia Shaw Brothers |

### REGOLA D'ORO: Un Ancoraggio Stilistico Vale Sei Aggettivi

La community cinese enfatizza: **non scrivere "唯美" (bello)**, ma piuttosto scrivi specificamente cosa intendi:

| NON scrivere (Vago) | Scrivi QUESTO (Specifico) |
|---|---|
| 唯美 (bello) | 治愈清新、日系暖色调、柔光散射 |
| 高级 (di alta qualita) | 赛博朋克、暗调、极简干净 |
| 大片感 (effetto blockbuster) | 电影质感、逆光、IMAX画幅比 |

### Ancoraggi Stilistici in Inglese (Utili Anche in Prompt Cinesi)

La community suggerisce che alcuni termini inglesi possono essere mescolati nei prompt cinesi per maggiore precisione:
- "Blade Runner color grade"
- "Studio Ghibli watercolor"
- "Kodak Portra 400 film"
- "Wes Anderson symmetrical framing"
- "bokeh"
- "tilt-shift"
- "cinematic"

---

## 7. Parole di Vincolo e Anti-Deformazione (约束词)

### IMPORTANTISSIMO: Seedance 2.0 NON Supporta Prompt Negativi

> **Dalla community:** "Seedance 2.0 的模型不会读负面提示词，即使你写了，它也会当没看见"
> *Il modello di Seedance 2.0 non legge i prompt negativi. Anche se li scrivi, li ignora completamente.*

Quindi: **usare descrizioni positive specifiche** al posto di dire "non fare X".

### Parole di Vincolo Essenziali (Aggiungere SEMPRE)

**Cinese:**
```
面部稳定不变形，五官清晰，人体结构正常，比例自然，画面稳定，无抖动，
4K高清，电影质感
```

**Italiano:**
```
Volto stabile senza deformazioni, lineamenti chiari, struttura corporea
normale, proporzioni naturali, immagine stabile, senza tremolii, 4K HD,
texture cinematografica
```

### Vocabolario Anti-Deformazione per le Azioni

Azioni veloci e ampie = piu probabilita di errori. Usare questi termini:

| Cinese | Italiano | Funzione |
|---|---|---|
| 缓慢 | Lento | Riduce errori tra i frame |
| 轻柔 | Delicato | Movimenti morbidi |
| 连贯 | Coerente | Transizioni fluide |
| 自然 | Naturale | Aspetto realistico |
| 流畅 | Fluido | Senza interruzioni |
| 不僵硬 | Non rigido | Previene movimenti robotici |

### Template Vincoli per Categoria

**Per video con persone:**
```
面部清晰不变形，五官自然，人体结构正常，比例自然，动作自然流畅不僵硬
```

**Per video di prodotto:**
```
产品细节清晰，材质质感真实，光影自然，无模糊无重影
```

**Per paesaggi:**
```
画面丝滑，无闪烁无重影，色彩自然，细节丰富
```

---

## 8. Sistema di Riferimento Multimodale con Sintassi @

### Regole di Upload

| Tipo | Massimo | Limiti |
|---|---|---|
| Immagini | 9 file | - |
| Video | 3 file | Durata totale max 15 secondi |
| Audio | 3 file | MP3/WAV, durata totale max 15 secondi |
| **Totale** | **12 file** | - |

### Sintassi @ di Base

La sintassi @ e il cuore del sistema multimodale. Si usa per **assegnare un ruolo specifico a ogni file caricato**.

**Formula base:**
```
@图片1 作为角色参考 @图片2 作为场景参考 @视频1 参考运镜和动作节奏
```
**Traduzione:**
```
@Immagine1 come riferimento personaggio, @Immagine2 come riferimento scena,
@Video1 come riferimento per camera e ritmo delle azioni
```

### Allocazione Ottimale dei File

La guida della community consiglia: **5-8 file massimo, non di piu!**

> "3-5张图片足够。1-2张锁角色，1-2张定场景"
> *3-5 immagini sono sufficienti. 1-2 per bloccare il personaggio, 1-2 per definire la scena.*

**Allocazione raccomandata:**
- 2 immagini personaggio (角色)
- 1 immagine scena (场景)
- 1 video di riferimento (运镜)
- 1 traccia audio (音频)
- + prompt testuale

> **Avvertimento:** Troppi materiali confondono il modello anziche migliorare l'output!

### Pattern di Utilizzo @ Avanzati

**Primo frame + riferimento movimento:**
```
@图1为首帧，参考@视频1的打斗动作
```
*@Immagine1 come primo frame, riferimento alle azioni di combattimento di @Video1*

**Estensione video:**
```
将@视频1延长5s
```
*Estendi @Video1 di 5 secondi* (selezionare durata 5s)

**Inserimento scena:**
```
在@视频1和@视频2之间加一个场景，内容为xxx
```
*Aggiungi una scena tra @Video1 e @Video2, il contenuto e xxx*

**Coerenza personaggio:**
```
男人@图片1 下班后疲惫地走在走廊……
```
*L'uomo @Immagine1 cammina stancamente nel corridoio dopo il lavoro...*

**Video promozionale multi-materiale:**
```
帮我做一个春节快闪类的视频，图片1、图片2、图片3、图片4、图片5、图片6、
图片7、图片8、视频1中的图片和视频，根据音频1进行卡点，运镜风格参考视频2，
使画面中的人物更有过年的喜庆欢乐的氛围，视频最后出现"团圆才是年"的大字结尾
```
*Crea un video flash per il Capodanno Cinese. Usa immagini 1-8, video 1, sincronizza con Audio 1 sui beat, riferisci lo stile di ripresa dal Video 2, rendi l'atmosfera festiva e gioiosa, termina con il testo grande "La riunione e il vero Capodanno"*

**Video lip-sync/parlato:**
```
@图片1 作为角色形象,面对镜头说话,口型与 @音频1 同步, 表情自然亲切,
背景为简洁的书房环境,镜头稳定
```
*@Immagine1 come aspetto del personaggio, parla verso la camera, lip-sync con @Audio1, espressione naturale e amichevole, sfondo di uno studio semplice, camera stabile*

### Priorita Audio

> **Regola dalla community:** "干声优先" (Priorita alla voce pulita)
>
> Per video parlati, usare audio senza musica di sottofondo per garantire la corretta sincronizzazione labiale.

---

## 9. Modalita di Creazione: Primo/Ultimo Frame vs Riferimento Completo

### Modalita Primo/Ultimo Frame (首尾帧模式)

**Quando usarla:** Per principianti o generazione rapida con una sola immagine.

**Workflow:**
1. Caricare 1 immagine HD come primo frame
2. Scrivere il prompt
3. Impostare parametri: 9:16 (TikTok/Douyin), 5-8 secondi, 1080P, stile cinematografico
4. Generare

**Ideale per:** Animazione di una singola immagine, test rapidi, principianti.

### Modalita Riferimento Completo (全能参考模式) -- RACCOMANDATA

**Quando usarla:** Per ogni progetto che richiede controllo preciso.

**Workflow:**
1. Definire l'obiettivo creativo
2. Organizzare i materiali per ruolo funzionale (personaggio/scena/camera/audio)
3. Caricare i file (controllare max 5-8)
4. Usare la sintassi @ per assegnare il ruolo di ogni materiale
5. Scrivere il prompt con la formula a 8 dimensioni
6. Generare
7. Valutare -> Modificare prompt o sostituire materiali -> Rigenerare

**Regola della community:**
> "单图+文字 → 首尾帧；多素材 → 全能参考"
> *Singola immagine + testo -> Primo/Ultimo frame; Multi-materiale -> Riferimento Completo*

---

## 10. Prompt Completi dalla Community Cinese (con Traduzione)

### Prompt 1: Ritratto Cinematografico Giapponese

**Cinese:**
```
一位穿白色亚麻连衣裙的年轻女生，长发微卷自然垂落，站在春日午后的日式庭院
木廊上，樱花花瓣缓缓飘落在肩头和发间。近景，缓慢推镜，暖光从侧面洒入，
柔光散射，日系清新暖色调，画面稳定无抖动，4K超高清，面部清晰不变形，五官自然，
细节丰富，电影质感。
```

**Italiano:**
Giovane donna con vestito di lino bianco, capelli lunghi leggermente mossi che cadono naturalmente, in piedi sulla veranda di legno di un giardino giapponese in un pomeriggio primaverile, petali di ciliegio che cadono lentamente sulle spalle e tra i capelli. Primo piano, dolly-in lento, luce calda dal lato, luce diffusa morbida, tonalita calda giapponese fresca, immagine stabile senza tremolii, 4K ultra HD, volto chiaro senza deformazioni, lineamenti naturali, ricco di dettagli, texture cinematografica.

---

### Prompt 2: Tramonto al Mare (Paesaggio)

**Cinese:**
```
海边日落，海浪轻拍沙滩，镜头缓慢横移，暖橙色调，治愈清新，画面丝滑，
4K超高清，无闪烁无重影
```

**Italiano:**
Tramonto al mare, onde che accarezzano dolcemente la spiaggia, carrellata orizzontale lenta, tonalita arancione calda, fresco e rilassante, immagine setosa, 4K ultra HD, senza sfarfallio senza ghosting.

---

### Prompt 3: Immagine-a-Video con Primo Frame

**Cinese:**
```
基于参考图保持人物样貌与服装一致，动作缓慢抬手转身，自然流畅，不僵硬不变形，
稳定运镜，高清细节，电影质感
```

**Italiano:**
Basandosi sull'immagine di riferimento, mantenere aspetto e abbigliamento del personaggio coerenti, azione di alzare lentamente la mano e girarsi, naturale e fluida, non rigida e senza deformazioni, camera stabile, dettagli HD, texture cinematografica.

---

### Prompt 4: Scena di Combattimento Wuxia

**Cinese:**
```
这两张图片是一段悬崖对手戏的两个女主，请围绕两个女主，生成一段流畅的红衣
女子东方不败与黑衣女刺客二人对手戏的画面，需要运用到分镜和不同视角切换，
让整个画面更有节奏感和电影感。仅生成打斗音效和环境的音效，不要配背景音乐
```

**Italiano:**
Queste due immagini sono le due protagoniste di una scena di combattimento sulla scogliera. Genera una scena fluida di combattimento tra la donna in rosso "Dongfang Bubai" e l'assassina in nero, utilizzando storyboarding e cambio di prospettive diverse, rendendo l'intera scena piu ritmica e cinematografica. Genera solo effetti sonori di combattimento e ambientali, senza musica di sottofondo.

---

### Prompt 5: Preparazione Cibo (Cucina)

**Cinese:**
```
主角进入画面，先往面粉里轻轻撒入盐，然后用手搅拌均匀，接着倒入适量的水，
打入一个鸡蛋，开始揉面团。
```

**Italiano:**
Il protagonista entra nell'inquadratura, prima sparge delicatamente sale nella farina, poi mescola uniformemente con le mani, poi versa la giusta quantita d'acqua, rompe un uovo, e inizia a impastare.

---

### Prompt 6: Video Parlato / Lip-Sync

**Cinese:**
```
@图片1 作为角色形象,面对镜头说话,口型与 @音频1 同步, 表情自然亲切,
背景为简洁的书房环境,镜头稳定。
```

**Italiano:**
@Immagine1 come aspetto del personaggio, parla verso la camera, lip-sync con @Audio1, espressione naturale e amichevole, sfondo studio semplice, camera stabile.

---

### Prompt 7: Coreografia di Trasferimento (Danza)

**Cinese (riferimento dalla community ifanr):**
```
@video1的编舞替换为@image1的两个机器人；保持@image1的场景设置；
参考@video1的运镜和转场
```

**Italiano:**
La coreografia di @video1 sostituita con i due robot di @immagine1; mantenere l'ambientazione di @immagine1; riferire i movimenti di camera e le transizioni di @video1.

---

### Prompt 8: Stile Guarigione Caldo (Douyin/TikTok)

**Cinese (template Doubao):**
```
主体+温馨治愈风格，缓慢动作，自然光，柔和光影，细腻画质，1080P，竖屏9:16，
10秒，无模糊卡顿，画面干净清晰
```

**Italiano:**
Soggetto + stile caldo e rilassante, azione lenta, luce naturale, illuminazione morbida, qualita dettagliata, 1080P, verticale 9:16, 10 secondi, senza sfocatura o scatti, immagine pulita e chiara.

---

### Prompt 9: Alta Qualita Cinematografica

**Cinese (template Doubao):**
```
唯美电影质感，慢镜头，运镜流畅，氛围感拉满，高清细节，2K，横屏16:9，
10秒，画面稳定不抖动
```

**Italiano:**
Bella texture cinematografica, slow motion, camera fluida, atmosfera al massimo, dettagli HD, 2K, orizzontale 16:9, 10 secondi, immagine stabile senza tremolii.

---

### Prompt 10: Passeggiata Universale (Template Sostituibile)

**Cinese:**
```
一位年轻女生在[场景]中缓慢行走，微风轻拂头发，自然微笑，[光线描述]，中景，
缓慢推镜，画面流畅稳定，4K高清，电影感，面部清晰不变形，人体结构正常，
细节丰富，15秒。
```

**Variabili sostituibili:**
- **Scena (场景):** 林间 (foresta) / 海边 (spiaggia) / 城市街道 (strada urbana) / 咖啡馆 (caffe) / 樱花树下 (sotto i ciliegi)
- **Luce (光线):** 暖光光影 (luce calda) / 逆光剪影 (controluce/silhouette) / 侧光勾勒 (luce laterale di contorno) / 柔光漫射 (luce morbida diffusa)

---

### Prompt 11: Azione Ronin Surreale (dalla Repository GitHub)

**Inglese (originale dalla community cinese):**
```
A masked warrior battles a winged beast on floating islands during a
thunderstorm, with camera dynamics capturing debris effects and cinematic
lighting as the warrior leaps between crumbling platforms.
```

---

### Prompt 12: Duello Anime Live-Action (dalla Repository GitHub)

**Inglese (originale, video 15 secondi con timestamp):**
```
15-second samurai battle: [0:00-0:05] Close-up of blue water dragon breathing
technique activation. [0:05-0:10] Wide shot clash with golden lightning versus
blue water effects. [0:10-0:15] Slow-motion final strike with particle effects
dissipating.
```

---

### Prompt 13: Inchiostro Cinese Animato (水墨风)

Dalla performance del cantante Zhang Jie con "Yu Feng Ge" (驭风歌):
```
让徐悲鸿《六骏图》中的静态水墨骏马跃然而出，在大屏上自由奔腾
```
**Italiano:** I cavalli a inchiostro statici de "I Sei Destrieri" di Xu Beihong prendono vita e galoppano liberamente sullo schermo.

*Questo dimostra che il modello eccelle nello stile tradizionale cinese a inchiostro.*

---

## 11. Tecnica della Griglia 9 Riquadri (九宫格分镜)

Questa e una **tecnica esclusiva della community cinese** che sfrutta la capacita di Seedance 2.0 di interpretare griglie di immagini come storyboard.

### Come Funziona

1. Creare una singola immagine con 9 riquadri (griglia 3x3)
2. Ogni riquadro rappresenta un frame chiave della sequenza
3. Caricare l'immagine come riferimento
4. Scrivere un prompt minimo

> "如果输入一张九宫格的分镜图片，Seedance 2.0 也可以自己串起来"
> *Se carichi un'immagine a griglia 9 riquadri, Seedance 2.0 puo collegarli automaticamente in sequenza.*

### Vantaggi

- Riduce drasticamente la complessita del prompt
- Permette controllo visivo preciso della sequenza
- Ideale per chi pensa "visivamente" piuttosto che "testualmente"
- Una sola immagine + una frase = video completo

### Come Creare la Griglia

1. Generare le immagini singole con un tool AI (Seedream 5.0, Midjourney, etc.)
2. Arrangiare in griglia 3x3 con qualsiasi editor
3. Caricare come singolo file di riferimento
4. Aggiungere un prompt breve che descrive l'azione generale

---

## 12. 10 Casi d'Uso Ufficiali Dettagliati

Basati sull'articolo della Tencent News che analizza 10 scenari pratici:

### Caso 1: Coerenza Personaggio
**Capacita:** Mantenere azione e camera, sostituire il soggetto
**Uso:** Sostituzione personaggio, adattamento IP
**Tecnica:** Specificare nel prompt il trasferimento tra personaggi

### Caso 2: Coerenza Prodotto
**Capacita:** Fusione multi-immagine, controllo separato struttura e materiale
**Uso:** Fotografia e-commerce
**Tecnica:** Usare @Immagine separate per lato prodotto e texture superficiale

### Caso 3: Replica Danza
**Capacita:** Doppia replica azione + camera
**Uso:** Creazione video di danza
**Tecnica:** Riferire contemporaneamente movimenti del corpo e stile di ripresa

### Caso 4: Replica Combattimento
**Capacita:** Riferimento multi-video separato
**Uso:** Scene d'azione
**Tecnica:** Controllare azione e linguaggio cinematografico separatamente

### Caso 5: Replica Spot Commerciale
**Capacita:** Replica ritmo pubblicitario classico
**Uso:** Video promozionali prodotto
**Tecnica:** Riferire camera e ritmo dei tagli dal video originale

### Caso 6: Estensione Video
**Capacita:** "Continuare a filmare" da dove si era interrotto
**Indicatore chiave:** Luce e azione si collegano naturalmente
**Tecnica:** Mantenere vincoli identici nel prompt di estensione

### Caso 7: Editing Video (Stravolgere la Trama)
**Capacita:** Riscrittura parziale della trama
**Uso:** Editing creativo, parodie
**Tecnica:** Ridefinire la direzione narrativa di un segmento

### Caso 8: Effetti Speciali Sottotitoli
**Capacita:** Controllo particelle e testo
**Uso:** Animazioni titolo/apertura
**Tecnica:** Riferire effetti particellari e materiale dal video

### Caso 9: Piano Sequenza (一镜到底)
**Capacita:** Coerenza spaziale e plausibilita fisica
**Importanza:** Indicatore chiave della maturita del modello
**Uso:** Tracking complessi in scene elaborate

### Caso 10: Sincronizzazione Ritmo Musicale
**Capacita:** Sincronizzazione audio-video
**Uso:** MV, video paesaggistici
**Tecnica:** Multi-immagine + ritmo video come riferimento per il montaggio

> **Insight chiave dalla community:** "Seedance 2.0真正提升的，不是'炫技能力'，而是'控制能力'"
> *Cio che Seedance 2.0 ha realmente migliorato non e la "capacita di fare effetti speciali" ma la "capacita di controllo".*

---

## 13. Workflow per Video Lunghi (oltre 15 secondi)

### Metodo 1: Estensione Relay Sequenziale

1. Generare il primo segmento (10-13 secondi)
2. Usare l'output come riferimento per il segmento successivo
3. **Ripetere i vincoli** nel prompt di ogni estensione

**Prompt esempio per estensione:**
```
将@视频1延长15s，角色从微笑点头直接过渡到举手示意，保持动作连贯流畅
```
*Estendi @Video1 di 15s, il personaggio passa dal sorridere e annuire ad alzare la mano per salutare, mantenendo l'azione coerente e fluida*

**ATTENZIONE:** La selezione durata = durata della NUOVA parte, non del totale!

### Metodo 2: Segmenti Indipendenti + Montaggio

1. Generare ogni segmento di 10-13 secondi separatamente
2. Usare gli stessi materiali di ancoraggio per coerenza visiva
3. Assemblare in software di editing

**Tecniche di transizione:**
- **B-roll concealment (B-roll遮切法):** Inserire 1-2 secondi di footage esterno nei punti di giunzione per mascherare piccole incoerenze, mantenendo la continuita audio
- Dissolvenze
- Tagli netti sincronizzati con l'audio continuo

### Limite di Qualita nelle Estensioni

> **Dalla community:** L'estensione continua oltre 3 iterazioni degrada la qualita. Raccomandazione: **esportare segmenti da 30 secondi** come nuovo materiale di riferimento per "ricominciare".

### Vincoli per le Estensioni

> "延长段必须重复原始提示词里的约束词（面部不变形、服装一致等），否则后段人物可能'变脸'"
>
> *I segmenti di estensione DEVONO ripetere le parole di vincolo del prompt originale (volto senza deformazioni, abbigliamento coerente, ecc.), altrimenti il personaggio potrebbe "cambiare faccia" nelle parti successive.*

---

## 14. Cinese vs Inglese: Quale Lingua Usare per i Prompt

### Verdetto della Community: Il CINESE e Generalmente Migliore

Seedance 2.0 e stato addestrato da ByteDance e ha una **comprensione nativa del cinese**:

> "Seedance 2.0是字节跳动训练的模型，对中文的理解力是原生级别的"
> *Seedance 2.0 e un modello addestrato da ByteDance, la sua comprensione del cinese e a livello nativo*

### Risultati dei Test

| Scenario | Lingua Migliore |
|---|---|
| 国风/日系/写实 (Stile cinese/giapponese/realistico) | **Cinese** nettamente |
| Cyberpunk, Sci-Fi | Cinese o Inglese simili |
| Termini cinematografici tecnici | Mix cinese + inglese |
| Descrizioni emotive, atmosferiche | **Cinese** |

### Raccomandazione della Community

1. **Descrizioni principali:** Usare cinese
2. **Termini tecnici specifici:** Mescolare inglese quando utile (bokeh, tilt-shift, cinematic, Hitchcock zoom)
3. **Non serve tradurre:** Il cinese non e mai peggiore dell'inglese su questo modello
4. **L'inglese funziona:** Ma non sara MAI migliore del cinese per la maggior parte degli scenari

> "纯中文效果最稳，纯英文也能用，但不会比中文更好，没有必要专门翻译"
> *Il cinese puro e il piu stabile, l'inglese puro funziona ma non sara mai migliore del cinese, non c'e bisogno di tradurre appositamente*

### Eccezione Rara

Una minoranza di utenti ha riportato che per alcuni scenari **molto specifici**, l'inglese potrebbe dare risultati leggermente migliori. Se un prompt cinese non funziona, provare la traduzione in inglese puo essere un ultimo tentativo.

---

## 15. Guida agli Errori Comuni e Come Evitarli (避坑指南)

### Errore 1: Vincoli Incompleti

> "不管什么场景，提示词末尾都要加约束词，这几个词是安全带，不系就等着翻车"
> *In qualsiasi scena, aggiungere SEMPRE le parole di vincolo alla fine del prompt. Sono la cintura di sicurezza -- senza, aspettati un incidente.*

**Soluzione:** Aggiungere SEMPRE alla fine: `面部稳定不变形，画面稳定，4K高清`

### Errore 2: Azioni Troppo Veloci o Ampie

Il modello AI interpola tra i frame. Maggiore e la differenza tra frame consecutivi, maggiore la probabilita di errore.

**Soluzione:** Usare esclusivamente azioni lente e continue. Mai scrivere: salti, giri veloci, danze complesse.

### Errore 3: Conflitto Luce/Stile

**Esempio errato:** Stile "cyberpunk" + illuminazione "luce solare calda"

**Soluzione:** Consultare la Tabella Scena x Illuminazione (Sezione 5).

### Errore 4: Riferimenti @ Sbagliati

> "素材多的时候，一定反复检查每个@引用有没有对上号"
> *Quando ci sono molti materiali, controllare SEMPRE piu volte che ogni riferimento @ sia corretto*

**Soluzione:** Verificare 2-3 volte ogni @riferimento prima di generare. Usare l'anteprima hover.

### Errore 5: Troppi Verbi di Movimento in Una Sola Clip

**Regola:** Un'inquadratura = un verbo di azione. Piu verbi = confusione.

### Errore 6: Troppi Personaggi

**Regola:** Massimo 1-2 personaggi. Oltre 2 causa confusione d'identita e perdita di coerenza.

### Errore 7: Troppi Cambi Camera in Una Clip

> "Seedance 2.0单次4-15秒，一条提示词里超过2-3个镜头变化，模型就容易乱套"
> *Con 4-15 secondi per clip, piu di 2-3 cambi di inquadratura in un singolo prompt e il modello va in confusione*

### I 5 Problemi Piu Comuni e Soluzioni

| Problema | Soluzione |
|---|---|
| 口型不准 (Lip-sync errato) | Usare audio pulito senza musica, verificare formato MP3 |
| 表情僵硬 (Espressioni rigide) | Aggiungere "表情自然" e descrivere emozione specifica |
| 手部变形 (Mani deformate) | Evitare close-up sulle mani, usare piano medio |
| 画面抖动 (Tremolii immagine) | Aggiungere "画面稳定无抖动" e usare camera fissa |
| 背景错误 (Sfondo sbagliato) | Fornire immagine di riferimento scena specifica |

### Ordine di Debug (dalla Community)

> **排查口诀:** 约束 → 动作 → 主体 → 风格 → 画质 → 引用 → 时长 → 长度
>
> **Ordine di verifica:** Vincoli -> Azione -> Soggetto -> Stile -> Qualita -> Riferimenti @ -> Durata -> Lunghezza prompt

**Regola fondamentale:** Cambiare UNA SOLA variabile per volta per identificare il problema.

### Guida Rapida al Debug

| Sintomo | Cosa Modificare |
|---|---|
| Composizione sbagliata, azione corretta | Solo la camera |
| Movimento innaturale | Cambiare "handheld" con "gimbal"; specificare velocita |
| Stile incoerente | Sostituire con un singolo ancoraggio stilistico piu forte |
| Artefatti ricorrenti | Cambiare parole di vincolo o dimensione inquadratura |
| Angoli caotici | Passare a "single tracking shot" |

---

## 16. Piattaforme di Accesso e Strategie di Risparmio Crediti

### Confronto Piattaforme per Utenti Non-Cinesi

| Piattaforma | Richiede VPN Cina? | Richiede +86? | Crediti Gratuiti | Funzionalita |
|---|---|---|---|---|
| Jimeng Web | Si | Si (o Douyin) | Gratis limitato con watermark | Completa |
| Doubao App | Consigliato HK VPN | No (account Google) | 10 gen/giorno | Limitata (no ref. immagini) |
| Xiao Yunque App | Si | Si | 1200 + 130/giorno | Completa |
| CyberBara | No | No | Pochi gratuiti | Completa |
| Volcano Ark API | No | Account aziendale | Pay-per-use | Solo API |

### Strategie di Risparmio Crediti dalla Community

1. **Genera prima in 1080P** per testare, poi rigenera in 2K solo se soddisfatto
2. **Inizia con 5 secondi** per verificare la direzione, poi estendi se necessario
3. **Usa account multipli** su piattaforme diverse (Jimeng + Xiao Yunque)
4. **Accumula crediti giornalieri** che non scadono mai
5. **Login giornaliero** per bonus crediti
6. **Abbonamento mensile** a 69 RMB/mese (1080 crediti) = 0.065 RMB/credito per uso intensivo
7. **Invita amici** per crediti bonus su Xiao Yunque

### Trucco Nascosto

> Nella modalita Fast di Xiao Yunque, occasionalmente i crediti non vengono detratti. Sfruttare i benefici a tempo limitato quando disponibili.

---

## 17. Strumenti Automatici: Claude Code Skill per Prompt

La community cinese ha sviluppato diversi **Claude Code Skills** specifici per generare automaticamente prompt Seedance 2.0 professionali.

### Seedance Prompt Skill (di songguoxs)

**Repository:** https://github.com/songguoxs/seedance-prompt-skill

**Capacita:**
- Generazione pura testo
- Controllo coerenza tramite riferimenti
- Replica camera/movimento
- Replica VFX
- Completamento storia
- Estensione video
- Sound design
- Sequenze piano-sequenza
- Editing video
- Sincronizzazione musicale

**Workflow in 4 passaggi:**
1. Descrivi la tua idea in linguaggio naturale
2. Claude conferma i parametri (durata, aspect ratio, riferimenti, stile)
3. Claude genera 2-3 versioni del prompt
4. Iterazione per affinare

**Include librerie integrate di:**
- Linguaggio cinematografico (tipi di inquadratura, movimenti, angoli)
- Stili visivi (grane pellicola, palette colori, movimenti artistici, illuminazione)

### Seedance 2.0 Storyboard Generator (di liangdabiao)

**Repository:** https://github.com/liangdabiao/Seedance2-Storyboard-Generator

Converte romanzi/storie in sceneggiature multi-episodio ottimizzate per Seedance 2.0:
1. Concepire il tema
2. Scrivere la sceneggiatura
3. Generare descrizioni dei materiali
4. Generare immagini
5. Scrivere script di storyboard
6. Generare video episodio per episodio

### Disponibilita su Coze

Il Seedance 2.0 Claude Agent Skill e disponibile gratuitamente anche nel negozio di competenze di Coze per uso immediato senza setup.

---

## 18. API e Accesso Sviluppatori via Volcano Engine

### Stato dell'API (Marzo 2026)

L'API ufficiale Seedance 2.0 e disponibile tramite la piattaforma **Volcano Engine (火山引擎)** di ByteDance.

**Documentazione SDK:** https://www.volcengine.com/docs/82379/1366799

### Caratteristiche API

- Architettura multi-modale audio-video congiunta
- Supporto text-to-video, image-to-video, video-to-video
- Risoluzione nativa 2K
- Storytelling multi-inquadratura
- Input multi-immagine di riferimento

### Come Accedere

1. Registrarsi su console.volcengine.com
2. Richiedere i permessi API per il modello Seedance 2.0
3. Seguire la documentazione SDK per l'integrazione
4. Modello di pagamento pay-per-use

### ATTENZIONE: API False

> La community avverte della presenza di **servizi API falsi** che rivendono accesso non autorizzato. Usare SOLO i canali ufficiali Volcano Engine.

---

## 19. Architettura Tecnica (per Utenti Avanzati)

### Architettura a 5 Livelli

1. **Codifica input multimodale** (Multi-Modal Input Encoding)
2. **Modellazione spazio-temporale** (Spatio-Temporal Modeling)
3. **Generazione parallela** (Parallel Generation)
4. **Calibrazione e ottimizzazione** (Optimization Calibration)
5. **Consegna output** (Output Delivery)

### Dual-Branch Diffusion Transformer

L'innovazione fondamentale: genera **immagini e audio in parallelo** tramite meccanismo di attenzione cross-modale (a differenza dei modelli sequenziali che causano disallineamento audio-video).

> "生成画面与音频并行运算，基于音频-画面跨模态注意力机制"

### Spatio-Temporal Causal Modeling (STCM)

Generazione video consapevole della fisica attraverso 3 fasi:
1. Estrazione relazioni causali
2. Simulazione parametri fisici
3. Ottimizzazione continuita inter-frame

Il sistema calcola traiettorie degli oggetti, velocita e fisica delle collisioni per garantire coerenza logica.

### Motore di Cinematografia Intelligente

Supporta 10+ modalita professionali di camera: tracking, pan, tilt, orbit, overhead, crane, con pianificazione automatica dell'inquadratura e transizioni fluide sincronizzate con il ritmo audio.

### Limiti Tecnici Attuali

- Risoluzione: 640x640 fino a 834x1112 pixel (per input)
- Conoscenza storica/specializzata non sempre accurata
- Espressioni facciali per emozioni complesse ancora rigide
- Massimo 60 secondi di video (con estensioni)

---

## 20. Risorse Bilibili, GitHub e Community

### Tutorial Bilibili (B站)

| Titolo | URL | Contenuto |
|---|---|---|
| AI Filmmaking Super Tutorial | https://www.bilibili.com/video/BV1sGcxzPEBj/ | Dalla base alla creazione di cortometraggi AI |
| Tutorial Piu Completo di Seedance 2.0 | https://www.bilibili.com/video/BV11Dc5zBE7d/ | Copertura completa di tutte le funzionalita |
| Collezione Completa Usi Pratici | https://www.bilibili.com/video/BV1gPZXBCEb9/ | Tutti i casi d'uso reali |
| 30 Casi con Prompt Completi | https://www.bilibili.com/video/BV1gCcqzkEe7/ | 30 casi + prompt pubblici |
| 3D Rendering Workflow | https://www.bilibili.com/video/BV1AJPxzgEah/ | Workflow 3D previz |
| Team Storyboard con AI | https://www.bilibili.com/video/BV153PFzSEku/ | Dal copione al video finale |
| 2026 Tutorial Completo (保姆级) | https://www.bilibili.com/video/BV1oUfcByEXD/ | 100 episodi, dal principiante all'esperto |

### Repository GitHub

| Repository | URL | Contenuto |
|---|---|---|
| awesome-seedance-2-prompts | https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts | 1099+ prompt curati |
| seedance2.0-how-to | https://github.com/ZeroLu/seedance2.0-how-to | Guida accesso + prompt engineering |
| seedance-prompt-skill | https://github.com/songguoxs/seedance-prompt-skill | Claude Code Skill per prompt |
| Seedance2-Storyboard-Generator | https://github.com/liangdabiao/Seedance2-Storyboard-Generator | Generatore sceneggiature |
| seedance2.0 (Web App) | https://github.com/wwwzhouhui/seedance2.0 | App Web React + Express |
| seedance-prompt-guide | https://github.com/rich5000/seedance-prompt-guide | Guida prompt |
| seedance2.0-prompt-skill | https://github.com/MapleShaw/seedance2.0-prompt-skill | Skill alternativo |

### Siti di Prompt Online

| Sito | URL | Contenuto |
|---|---|---|
| Seedance 2 Prompts (500+) | https://seedance2prompt.org/ | Raccolta 500+ prompt |
| YouMind Prompts | https://youmind.com/seedance-2-0-prompts | Prompt ad alto segnale |
| Seedance Video Guide | https://seedancevideo.com/prompt-guide/ | Guida completa |
| PromptsRef Library | https://promptsref.com/library/seedance-2.0 | Libreria di riferimento |
| Dreamina Official | https://dreamina.capcut.com/resource/seedance-2-0-prompt | 18 prompt potenti |

### Articoli Cinesi Chiave

| Fonte | Titolo | URL |
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

### Manuale Ufficiale ByteDance (Feishu/Lark)

**URL:** https://bytedance.larkoffice.com/wiki/A5RHwWhoBiOnjukIIw6cu5ybnXQ

Questo e il documento ufficiale interno di ByteDance che contiene la guida completa con tutti i template e le specifiche ufficiali.

---

## 21. Template Pronti all'Uso per Categoria

### Template UGC/Influencer

**Cinese:**
```
主体 + 手持手机视角，微微晃动的自然质感，竖屏9:16，10秒，1080P，
自然光，表情生动，画面清晰
```
**Italiano:** Soggetto + prospettiva smartphone tenuto in mano, texture naturale con leggero ondeggiamento, verticale 9:16, 10 secondi, 1080P, luce naturale, espressioni vivaci, immagine chiara

### Template Spot Pubblicitario Prodotto

**Cinese:**
```
产品近景到中近景，柔光灯箱，@图片1为产品正面，缓慢旋转展示，
背景模糊散景，商业质感，画面稳定，4K
```
**Italiano:** Prodotto da primo piano a medio primo piano, softbox, @Immagine1 come fronte prodotto, rotazione lenta per mostrare, sfondo con bokeh, texture commerciale, immagine stabile, 4K

### Template Scena Cinematografica

**Cinese:**
```
云台稳定跟拍，消色调电影色彩，胶片颗粒感，主体在[场景]中[动作]，
16:9横屏，10秒，2K，画面稳定不抖动
```
**Italiano:** Tracking stabilizzato da gimbal, colori cinematografici desaturati, grana pellicola, soggetto in [scena] che [azione], 16:9 orizzontale, 10 secondi, 2K, immagine stabile senza tremolii

### Template Talking Head / Presentatore

**Cinese:**
```
中近景，三脚架锁定，45度柔光主灯，主体面对镜头说话，口型与@音频1同步，
表情自然，背景简洁，1080P，9:16
```
**Italiano:** Medio primo piano, treppiede bloccato, luce principale morbida a 45 gradi, soggetto che parla alla camera, lip-sync con @Audio1, espressione naturale, sfondo semplice, 1080P, 9:16

### Template Scena di Combattimento

**Cinese:**
```
先远景确立场景，然后中景跟拍打斗动作，最后近景冲击特写，
动作力度感强，音效同步，邵氏兄弟武侠电影风格
```
**Italiano:** Prima campo lungo per stabilire la scena, poi piano medio tracking per l'azione di combattimento, infine primo piano d'impatto, sensazione di forza nelle azioni, effetti sonori sincronizzati, stile film wuxia Shaw Brothers

### Template Video Musicale

**Cinese:**
```
多角度混合镜头，@音频1为背景音乐，画面切换与节拍同步，
灯光效果动态变化，主体@图片1在舞台表演，2K，16:9
```
**Italiano:** Inquadrature miste da angoli multipli, @Audio1 come musica di sottofondo, cambi immagine sincronizzati con il beat, effetti luce che cambiano dinamicamente, soggetto @Immagine1 in performance sul palco, 2K, 16:9

### Template Stile Antico Cinese (国风/古风)

**Cinese:**
```
水墨画风格，一位古装女子在竹林间缓步行走，长袖飘动，仙气飘渺，
远景缓慢推近，中国传统水墨色调，意境悠远，画面丝滑，4K
```
**Italiano:** Stile pittura a inchiostro, una donna in abiti tradizionali cammina lentamente tra i bambu, maniche lunghe che ondeggiano, aura eterea e mistica, campo lungo che si avvicina lentamente, tonalita tradizionale cinese a inchiostro, atmosfera profonda e distante, immagine setosa, 4K

### Template Montaggio Rapido

**Cinese:**
```
4个节拍，每个约2秒，@图片1-@图片4依次展示，
灯光统一，@音频1卡点切换，节奏感强，1080P
```
**Italiano:** 4 beat, circa 2 secondi ciascuno, @Immagine1-@Immagine4 mostrate in sequenza, illuminazione uniforme, tagli sincronizzati con @Audio1, forte senso del ritmo, 1080P

---

## 22. Parole di Intensita e Avverbi di Grado (程度副词)

Le parole di intensita sono **critiche** per controllare l'ampiezza e la velocita del movimento. La community cinese le ha categorizzate:

### Movimento Delicato (Raccomandato per Evitare Artefatti)

| Cinese | Inglese | Italiano |
|---|---|---|
| 缓慢地 | Slowly | Lentamente |
| 轻轻地 | Gently | Delicatamente |
| 微微地 | Slightly | Leggermente |
| 细微地 | Subtly | Sottilmente |
| 几乎不可察觉地 | Barely/imperceptibly | Quasi impercettibilmente |

### Movimento Intenso (Usare con Cautela)

| Cinese | Inglese | Italiano |
|---|---|---|
| 快速地 | Quickly/rapidly | Rapidamente |
| 猛烈地 | Violently/powerfully | Violentemente |
| 大幅度地 | With large amplitude | Con grande ampiezza |
| 疯狂地 | Frantically/crazily | Freneticamente |
| 剧烈地 | Dramatically/vigorously | Drammaticamente |

### Movimento Ritmico

| Cinese | Inglese | Italiano |
|---|---|---|
| 有节奏地 | Rhythmically | Ritmicamente |
| 平稳地 | Smoothly/steadily | Stabilmente |
| 流畅地 | Fluidly | Fluidamente |

### Esempio di Differenza

**Vago (da evitare):**
```
车转弯 (L'auto gira)
```

**Specifico (corretto):**
```
轮胎冒烟，车猛烈漂移90度，橡胶在柏油路上尖叫
```
*Le gomme fumano, l'auto dritta violentemente di 90 gradi, la gomma strilla sull'asfalto*

---

## 23. Risoluzione Problemi: Flowchart di Debug

### Ordine di Verifica Sistematico

```
1. VINCOLI (约束) - Ci sono? Sono completi?
   ↓ Se OK
2. AZIONE (动作) - E troppo veloce/complessa?
   ↓ Se OK
3. SOGGETTO (主体) - La descrizione e chiara e specifica?
   ↓ Se OK
4. STILE (风格) - E coerente con l'illuminazione?
   ↓ Se OK
5. QUALITA (画质) - I parametri sono appropriati?
   ↓ Se OK
6. RIFERIMENTI @ (引用) - Sono corretti e non in conflitto?
   ↓ Se OK
7. DURATA (时长) - La durata e appropriata per il contenuto?
   ↓ Se OK
8. LUNGHEZZA PROMPT (长度) - Il prompt e tra 30-200 parole?
```

### Strategia di Iterazione

1. **Prima generazione:** Testa in 1080P, 5 secondi
2. **Se non soddisfatto:** Modifica UNA SOLA variabile
3. **Se soddisfatto:** Rigenera in 2K, durata completa
4. **Genera 2-4 varianti** per confronto

### Limiti della Piattaforma da Conoscere

- **Restrizione volti reali:** ByteDance ha temporaneamente limitato l'uso di foto di volti reali dopo il lancio per prevenire deepfake. Le alternative raccomandate sono animazione o personaggi generati da AI.
- **Errore "contenuto non conforme":** Puo apparire se il contenuto viola le regole della piattaforma (volti reali, contenuto sensibile).
- **Audio con errori:** Occasionali problemi di sincronizzazione vocale e sottotitoli errati nei contenuti parlati.

---

## 24. Fonti e Riferimenti

### Articoli Zhihu (知乎)
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

### CSDN e Blog Tecnici
- [80+提示词 Seedance 2.0 提示词完全指南](https://blog.csdn.net/mizzlelover/article/details/158040401)
- [字节即梦Seedance 2.0使用手册](https://blog.csdn.net/seoread/article/details/157937583)
- [全能参考完全指南](https://blog.csdn.net/u014177256/article/details/158013628)
- [豆包 Seedance 2.0 入门教程](https://blog.csdn.net/belldeep/article/details/158290740)
- [Seedance 2.0 技术深度解析](https://segmentfault.com/a/1190000047604020)

### Piattaforme Internazionali
- [Dreamina Official Seedance 2.0 Prompts](https://dreamina.capcut.com/resource/seedance-2-0-prompt)
- [Seedance 2.0 Usage Guide (Redreamality)](https://redreamality.com/blog/seedance-2-guide/)
- [Seedance 2 Prompts - 500+ Examples](https://seedance2prompt.org/)
- [Seedance Prompt Guide (SeedanceVideo)](https://seedancevideo.com/prompt-guide/)

### GitHub Repositories
- [awesome-seedance-2-prompts (1099+ prompts)](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts)
- [seedance2.0-how-to](https://github.com/ZeroLu/seedance2.0-how-to)
- [seedance-prompt-skill](https://github.com/songguoxs/seedance-prompt-skill)
- [Seedance2-Storyboard-Generator](https://github.com/liangdabiao/Seedance2-Storyboard-Generator)

### Altre Fonti
- [iFanr: 即梦 Seedance 2.0 黑神话时刻](https://www.ifanr.com/1654856)
- [苏米客: 创作提示词手册](https://www.xmsumi.com/detail/2432)
- [实在智能: seedance2.0提示词有哪些](https://www.ai-indeed.com/encyclopedia/15752.html)
- [fly63: 提示词超全汇总](https://fly63.com/article/detial/13338)
- [Volcano Engine SDK](https://www.volcengine.com/docs/82379/1366799)
- [Baidu Baike: Seedance2.0](https://baike.baidu.com/item/Seedance2.0/67358557)

### Video Bilibili
- [即梦Seedance2.0 AI影视创作最细教程](https://www.bilibili.com/video/BV1sGcxzPEBj/)
- [全网最完整Seedance2.0使用教程](https://www.bilibili.com/video/BV11Dc5zBE7d/)
- [Seedance2.0全网最全实战用法合集](https://www.bilibili.com/video/BV1gPZXBCEb9/)
- [30个用法案例+完整提示词](https://www.bilibili.com/video/BV1gCcqzkEe7/)
- [2026最新版即梦SD2保姆级教程](https://www.bilibili.com/video/BV1oUfcByEXD/)

### Documento Ufficiale ByteDance
- [即梦官方学习手册 (Feishu/Lark)](https://bytedance.larkoffice.com/wiki/A5RHwWhoBiOnjukIIw6cu5ybnXQ)

---

## RIEPILOGO DELLE REGOLE D'ORO DALLA COMMUNITY CINESE

1. **Un'inquadratura = un verbo** -- Mai piu azioni in una clip
2. **Massimo 1-2 personaggi** -- Oltre 2 causa confusione d'identita
3. **30-200 parole** e la lunghezza ottimale del prompt
4. **SEMPRE aggiungere vincoli** alla fine del prompt
5. **I prompt negativi NON funzionano** -- Descrivi cosa VUOI
6. **Genera prima breve (5s)** poi estendi
7. **Una variabile alla volta** quando fai debug
8. **Cinese e la lingua migliore** per questo modello
9. **5-8 file di riferimento massimo** -- Troppi confondono il modello
10. **Luce e stile devono corrispondere** -- Il conflitto e il killer #1
11. **Movimenti lenti e continui** -- Le azioni veloci causano artefatti
12. **Un ancoraggio stilistico forte** vale piu di sei aggettivi vaghi
13. **Controlla SEMPRE i riferimenti @** -- Un errore rovina tutto
14. **Testa in 1080P** prima di spendere crediti per il 2K

---

*Documento compilato da ricerca approfondita su piattaforme della community cinese: Zhihu, Bilibili, CSDN, Tencent News, iFanr, SegmentFault, GitHub, Baidu Baike, Sohu, Sina, e risorse ufficiali ByteDance. Tutti i prompt cinesi sono presentati nella lingua originale con traduzione italiana.*
