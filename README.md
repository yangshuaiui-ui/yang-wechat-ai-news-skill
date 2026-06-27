# Yang WeChat AI News Skill

这是我给自己公众号工作流搭的 Codex Skill。

它不是一个单纯的“帮我写文章”提示词，而是一套把 AI 热点变成公众号成稿的创作系统：从选题判断、证据截图、原创观点、标题压力、移动端排版，到最后生成微信公众号可复制 HTML。

## Why I Built It

AI 新闻太快了。

如果只是追发布稿，很容易写成新闻搬运；如果只写观点，又容易没有证据支撑。我的公众号需要的是另一种链路：

1. 先判断这个热点值不值得写。
2. 再分清事实、报道、猜测和我的判断。
3. 再把关键证据截图或录屏对应到正文句子。
4. 最后写成产品经理、UXD、AI 产品设计师和老板能看懂的判断。

这套 Skill 就是把这个过程固定下来。

## What It Does

- 搜国内线、国外线 AI 热点，判断是否值得写
- 把新闻热点拆成产品、设计、业务视角的原创判断
- 先做证据包，再写正文，避免先写后补图
- 强制截图/录屏和正文句子对应：句子 -> 素材 -> 图注 -> 来源
- 保留我的表达方式，避免写成通稿、模型说明书或 AI 味总结
- 输出 `.md`、素材文件夹、标题、摘要、可复制 HTML 和自检结果

## Creation Loop

```text
需求/热点
  -> 选题判断
  -> 事实分层
  -> 证据收集
  -> 句子和素材映射
  -> 原创观点
  -> 正文成稿
  -> 标题和首屏
  -> 微信 HTML
  -> 发布前自检
```

这套流程的重点不是把文章写长，而是让每篇文章都有一个清楚的判断：

```text
这件事发生了，它真正改变了什么？
普通人、产品人、设计师和老板应该怎么理解？
```

## Skill Structure

```text
yang-wechat-ai-news/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── account-voice.md
│   ├── creation-system.md
│   ├── evidence-html.md
│   ├── hotspot-scan.md
│   ├── quality-gates.md
│   └── workflow.md
└── scripts/
    └── render_wechat_html.py
```

## Install

安装到本机 Codex：

```bash
mkdir -p ~/.codex/skills
cp -R yang-wechat-ai-news ~/.codex/skills/
```

也可以在 Codex 里让它安装这个仓库里的 Skill：

```text
Install the Codex skill from:
https://github.com/yangshuaiui-ui/yang-wechat-ai-news-skill/tree/main/yang-wechat-ai-news
```

## Example Prompts

```text
用我的公众号 Skill 组处理这个 AI 热点，先判断值不值得写，再给证据包和文章框架。
```

```text
这篇稿子按我的公众号表达方式改一遍，保留核心意思，去掉 AI 味，最后生成微信公众号可复制 HTML。
```

```text
帮我给这篇 AI 新闻稿找截图，要求每张图都和底下文案强对应。
```

## Delivery Standard

一次完整交付必须尽量包含：

- 公众号正文 `.md`
- 素材截图或录屏
- 图文对应关系
- 标题、封面短标题、摘要
- 微信公众号可复制 HTML
- 发布前自检

只写 Markdown 不算真正交付完成。

## Validation

校验 Skill：

```bash
python3 /Users/yangyangshuai/.codex/skills/.system/skill-creator/scripts/quick_validate.py ./yang-wechat-ai-news
```

测试 HTML 生成脚本：

```bash
python3 yang-wechat-ai-news/scripts/render_wechat_html.py \
  draft.md \
  images.json \
  article.html \
  --title "文章标题"
```

## License

MIT
