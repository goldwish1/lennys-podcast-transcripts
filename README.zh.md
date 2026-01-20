# Lenny 播客文字稿归档

一个全面的 [Lenny's Podcast](https://www.youtube.com/@LennysPodcast) 文字稿归档，专为 AI 编程助手和语言模型使用而组织。

## 关于 Lenny's Podcast

Lenny's Podcast 采访世界级的产品领导者和增长专家，提供具体、可操作和战术性的建议，帮助您构建、发布和发展自己的产品。

## 快速开始

**按主题浏览：** 从 [index/README.md](index/README.md) 开始，按主题探索剧集。

**搜索文字稿：**
```bash
grep -r "product-market fit" episodes/
```

## 仓库结构

```
├── episodes/                    # 269 个剧集文字稿
│   └── {guest-name}/
│       └── transcript.md
├── index/                       # AI 生成的主题索引
│   ├── README.md                # 主入口点
│   ├── product-management.md    # 关于产品管理的剧集
│   ├── leadership.md            # 关于领导力的剧集
│   └── ...                      # 50+ 个主题文件
└── scripts/
    └── build-index.sh           # 重新生成索引的脚本
```

## 剧集格式

每个剧集都有自己的文件夹，以嘉宾姓名命名，包含一个 `transcript.md` 文件，其中包含：

1. **YAML Frontmatter** - 结构化元数据，包括：
   - `guest`: 嘉宾姓名
   - `title`: 完整剧集标题
   - `youtube_url`: YouTube 视频链接
   - `video_id`: YouTube 视频 ID
   - `publish_date`: 发布日期 (YYYY-MM-DD)
   - `description`: 剧集描述
   - `duration_seconds`: 剧集时长（秒）
   - `duration`: 人类可读的时长
   - `view_count`: 归档时的观看次数
   - `channel`: 频道名称

2. **文字稿内容** - 剧集的完整文字稿

## 主题索引

`index/` 文件夹包含每个剧集的 AI 生成关键词标签，按主题组织：

| 主题 | 描述 |
|-------|-------------|
| [产品管理](index/product-management.md) | 57+ 个关于 PM 技能和实践的剧集 |
| [领导力](index/leadership.md) | 关于管理和领导力的剧集 |
| [增长策略](index/growth-strategy.md) | 增长战术和框架 |
| [产品市场契合](index/product-market-fit.md) | 寻找和衡量 PMF |

查看 [index/README.md](index/README.md) 获取完整的 50 个主题列表。

## 重建索引

索引使用 Claude CLI 生成。要重新生成：

```bash
./scripts/build-index.sh
```

这将通过 Claude 处理文字稿以生成关键词标签。脚本是幂等的 - 它会跳过已存在于关键词文件中的剧集，因此可以安全地多次运行。

## 与 AI 一起使用

### 加载文字稿

每个文字稿都是一个独立的 markdown 文件，可以轻松被 AI 系统解析。YAML frontmatter 提供了可以程序化提取的结构化元数据。

### 示例：读取文字稿

```python
import yaml

def read_transcript(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # 分割 frontmatter 和内容
    parts = content.split('---')
    if len(parts) >= 3:
        frontmatter = yaml.safe_load(parts[1])
        transcript = '---'.join(parts[2:])
        return frontmatter, transcript
    return None, content

# 使用示例
metadata, transcript = read_transcript('episodes/brian-chesky/transcript.md')
print(f"Guest: {metadata['guest']}")
print(f"Title: {metadata['title']}")
```

## 剧集数量

此归档包含来自 Lenny's Podcast 的 **269 个文字稿**。

## 数据来源

- **文字稿**：来自 Lenny's Podcast 文字稿归档
- **元数据**：从 [Lenny's Podcast YouTube 频道](https://www.youtube.com/@LennysPodcast) 提取

## 贡献

如果您发现文字稿或元数据有任何问题，请提交 issue 或 pull request。

## 使用这些文字稿构建的项目

以下是一些使用此文字稿归档构建的项目：

**[Lenny Playbook](https://lilys.ai/collections/141200?s=1)** by LilysAI – 将 Lenny Podcast 文字稿转换为结构化笔记、可视化信息图和聊天界面，以探索想法并获得可操作的答案。

**[Learn from Lenny](https://x.com/learnfromlenny)** by [@IamAdiG](https://x.com/IamAdiG) - X 上的 AI 代理，基于 Lenny 的播客提供可信的产品建议。标记它以获得准确且无废话的建议。

**[Lenny Skills Database](https://refoundai.com/lenny-skills/)** by Refound AI - 从 297 个播客剧集中提取的 86 个可操作技能的可搜索数据库。了解最佳产品团队的实际工作方式。

**[Lenny MCP](https://github.com/akshayvkt/lenny-mcp)** by [Akshay Chintalapati](https://x.com/akshayvkt) - 一个模型上下文协议服务器，为 AI 应用程序提供对 Lenny 播客内容的访问。

**[Recapio - Lenny's Podcast Summaries](https://recapio.com/channel/lennyspodcast)** - Lenny's Podcast 剧集的 AI 生成摘要、文字稿、关键见解和聊天界面。

**[Lenny's Frameworks](https://lennys-frameworks.vercel.app/)** - 从 Lenny's Podcast 剧集中提取的框架和心智模型集合。

**[Lenny Listens](https://lenny-listens.vercel.app/)** - 使用 Lenny 的采访方法论生成 AI 主导的采访，您可以与真实客户一起运行。

**[Lenny's Advice Arena](https://lennysadvicearena.lovable.app/)** - 探索 Lenny's Podcast 产品建议的交互式体验。

**[Lenny Gallery](https://lennygallery.manus.space/)** by Alan Chan - 一个信息图库，包含关键剧集的可视化摘要，使用 Manus AI 构建。

**[Lenny's Friends in Notion](https://lnkd.in/gtEdP5ew)** by Saya Iwasaki - 将 Lenny 的嘉宾转变为 Notion 导师，现在您可以在 Notion 工作区中询问任何问题并从他们那里获得反馈。每个嘉宾都设置了包含心智模型、框架和沟通风格的角色；您也可以按公司查询。

**[Lenny Distilled](https://lennydistilled.com)** by [Harsh Nene](https://www.linkedin.com/in/harshnene/) - 精选的 PM 智慧集合，可随时浏览...每次访问发现新见解，追溯到源引用和 YouTube 时刻。映射到 PM 工艺的 6 个维度，极简设计，多种语言。

**[Lenny's Library in Radia.io](https://getradia.io/resources/lennys-library)** by Kas Eelman - 利用文字稿为 Radia 用户的产品能力评估提供额外见解，包括引用、元数据和原始剧集。

**[Lenny for Claude](https://github.com/arjunlall/lenny-for-claude)** by [Arjun Lall](https://x.com/_arjun) - 在 Claude Code 和 Claude Desktop 中展示播客建议的 MCP 服务器。包括 /lenny 斜杠命令和可选的计划模式钩子。

**[Lennyhub RAG](https://github.com/traversaal-ai/lennyhub-rag)** by Hamza Farooq - 一个生产级知识图谱 RAG，支持多轮问题

**[Lenny Ideation Constellation & Search](https://lennys-search.vercel.app/)** - Lenny's Podcast 的语义搜索引擎和想法探索器。准确找到嘉宾所说的内容，或可视化发现他们的想法如何在剧集中连接、聚类和矛盾。

**[LennySan RAG-o-Matic](https://github.com/deanpeters/lennysan-rag-o-matic)** by Dean Peters - 一个低门槛、边学边做的 PM 研究工具，用于从 CLI 探索 Lenny Rachitsky 的 320+ 播客剧集，使用 AI 和 RAG，未来支持 Jupyter notebooks、时间序列探索等。

**[Ask Lenny](https://ask-lenny.vercel.app/)** by Prayerson Christian - 使用 Lenny 播客的真实引用回答问题的 AI 研究助手。

**[Lenny's Wisdom Wall](https://lennys-wisdom-wall.vercel.app)** by Shrikant Kadu - 一个交互式探索，展示来自 Lenny 播客嘉宾的有趣见解和精选矛盾。

**[Time Capsule](https://sameerbajaj.com/tools/timecapsule)** by [@sameerbajaj](https://x.com/sameerbajaj) - 描述您的情况，获得来自产品领导者的个性化建议信，他们曾处于您的确切时刻。

您是否使用这些文字稿构建了某些内容？提交 PR 将您的项目添加到此列表！

## 免责声明

此归档仅用于教育和研究目的。所有内容属于 Lenny's Podcast 和相应的嘉宾。请访问官方 YouTube 频道以支持创作者。

## 许可

文字稿仅供个人和教育使用。请尊重原始内容创作者的权利。
