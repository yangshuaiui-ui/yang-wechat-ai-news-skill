# Yang AI Skills

我自己在公众号和日常 AI 工作流里会用到的一些 Skill，跑通之后放在这里。

不是提示词合集，也不是把工具说明书搬一遍。每个 Skill 都尽量解决一个真实场景：能不能少踩坑，能不能少返工，能不能把 Agent 从“会回答”变成“会按流程交付”。

## Skills

| 名字 | 一句话 | 适合谁 |
|---|---|---|
| [yang-wechat-ai-news](./yang-wechat-ai-news/SKILL.md) | 把 AI 热点跑成公众号成稿，并通过用户终稿对比不断学我的写法 | 公众号作者、AI 内容创作者、产品/设计/老板视角写作者 |
| [mac-storage-doctor](./mac-storage-doctor/SKILL.md) | 给 Mac 做一次只读存储体检，把 AI 工具、缓存、项目文件分成能清、慎动、别动三类 | 天天用 Codex、Claude Code、Cursor、Docker、Node、模型缓存的 Mac 用户 |

## yang-wechat-ai-news

> “我生成一版，用户自己改定终稿，我再把差距沉淀回系统。下一篇，要更像我。”

这是我的公众号 AI 快讯生产系统。

它不只是写文章，而是把每天的公众号工作拆成一条闭环：

```text
热点/素材
  -> 选题判断
  -> 事实分层
  -> 证据截图或录屏
  -> 句子和素材强对应
  -> 生成初稿
  -> 自检闸门
  -> 标题和首屏
  -> 微信 HTML
  -> 用户亲改终稿
  -> 差异对比
  -> 风格台账更新
  -> 下一篇从更高起点开始
```

它最重要的不是“帮我写一篇”，而是后半段：

- 读 `claude1.md` 这类用户亲改风格台账
- 对比“生成稿”和“用户终稿”
- 把每处修改归类成风格倾向、禁忌、证据规则、标题习惯、结构习惯
- 下一篇主动避开旧错，不让同一个问题反复出现

### 适合

- 你每天都要写公众号，想让 Agent 越写越像你
- 你不接受“AI 味通稿”，需要证据、截图、图注、HTML 一起交付
- 你会自己改稿，希望 Agent 能从你的修改里学习

### 不适合

- 只想要通用爆款模板
- 不准备提供自己的改稿样本
- 只要一段 Markdown，不需要证据和交付闭环

### 怎么触发

```text
用我的公众号 Skill 组处理这个 AI 热点，先判断值不值得写，再给证据包和文章框架。
```

```text
这是我改定的用户终稿，和你上一版对比一下，把差距沉淀到我的风格台账里。
```

```text
这篇稿子按我的公众号表达方式改一遍，保留核心意思，去掉 AI 味，最后生成微信公众号可复制 HTML。
```

→ [SKILL.md](./yang-wechat-ai-news/SKILL.md)

## mac-storage-doctor

> “别上来就删。先让 Agent 告诉我，这些东西是什么，删了会怎样，哪些绝对别碰。”

现在很多 Mac 不是被照片塞满的，是被 AI 工作流塞满的。

Codex、Claude Code、Cursor、Docker、Node、Playwright、模型缓存、临时录屏、素材包、浏览器缓存，堆起来很快就是几十 GB。普通清理软件能告诉你“这里有缓存”，但它不一定知道这是不是你正在跑的项目、是不是某个 Agent 的工作目录、是不是删了会让你明天重装半天的东西。

这个 Skill 的目标不是“清出一个夸张数字”，而是让 Agent 先给你一份能看懂的存储体检报告。

### 它会做什么

- 只读扫描 Home 目录和常见 AI 工具缓存位置
- 找出大体积目录、项目依赖、下载、录屏、模型和浏览器缓存
- 给每一项标注路径、大小、可能来源、删除影响、推荐动作
- 用三类决策替代一刀切清理：
  - 绿灯：缓存、临时文件、可再生成内容
  - 黄灯：下载、项目依赖、离线视频、素材包，需要人工确认
  - 红灯：系统、密钥、运行中应用数据、重要项目，不给删除建议
- 输出 Markdown 或 JSON，方便继续让 Agent 解释、整理、生成命令

### 铁律

默认只读，不自动删除。

真正要删的时候，也应该先让用户确认路径、影响和备份状态。这个 Skill 更像一个存储医生，不是一个冲上去乱删的清洁工。

### 怎么触发

```text
帮我给 Mac 做一次存储体检，重点看 AI 工具和项目缓存，先不要删。
```

```text
我的 Mac 空间快满了，帮我判断哪些能清，哪些别碰。
```

→ [SKILL.md](./mac-storage-doctor/SKILL.md)

## Install

在支持 Skill 的 Agent 里，直接安装某一个目录：

```text
Install the Codex skill from:
https://github.com/yangshuaiui-ui/yang-ai-skills/tree/main/yang-wechat-ai-news
```

```text
Install the Codex skill from:
https://github.com/yangshuaiui-ui/yang-ai-skills/tree/main/mac-storage-doctor
```

本地手动安装：

```bash
mkdir -p ~/.codex/skills
cp -R yang-wechat-ai-news ~/.codex/skills/
cp -R mac-storage-doctor ~/.codex/skills/
```

## Validation

```bash
python3 /Users/yangyangshuai/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./yang-wechat-ai-news
python3 /Users/yangyangshuai/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./mac-storage-doctor
```

## License

MIT
