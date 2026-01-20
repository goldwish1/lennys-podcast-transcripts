---
name: update-episodes-index
description: 扫描 episodes/ 目录下的所有剧集，提取 transcript.md 文件元数据，并按发布日期排序，自动生成 EPISODES_INDEX.md（总剧集数、按年分组、倒序排序）。当新增剧集、用户要求更新或目录结构变化时使用。
---

# 更新剧集索引

## 快速开始

当你需要重新生成剧集索引时，执行以下脚本：

```bash
python3 .cursor/skills/update-episodes-index/scripts/generate_index.py
```

此脚本会自动完成以下操作：
- 自动查找项目根目录（通过定位 `episodes/` 目录）
- 扫描所有剧集子目录
- 提取每个剧集下 `transcript.md` 的元数据
- 在项目根目录生成并写入 `EPISODES_INDEX.md`

## 功能说明

- 扫描 `episodes/` 下的所有子目录
- 提取每个 `transcript.md` 文件中的元数据（guest, title, publish_date, youtube_url）
- 按发布日期倒序排序（最新在前）
- 按年份分组
- 生成格式化的 Markdown 索引文件

## 使用方法

**运行脚本：**
```bash
python3 .cursor/skills/update-episodes-index/scripts/generate_index.py
```

脚本将会：
- 扫描 `episodes/` 目录
- 查找所有 `transcript.md` 文件
- 提取 YAML frontmatter 元数据
- 按 `publish_date` 倒序排序
- 写入项目根目录下的 `EPISODES_INDEX.md`

## 输出格式

生成的索引文件包括：
- 总剧集数量
- 按年份分组的剧集列表
- 每条记录包含：
  - 格式化日期（YYYY年MM月DD日）
  - 嘉宾姓名
  - 节目标题
  - YouTube 视频链接
  - transcript 文件链接

## 适用场景

在以下情况下使用本技能：
- 新剧集添加至 `episodes/` 目录
- 用户要求“更新索引”或“重新生成索引”
- 用户指出剧集顺序有误
- 批量新增或修改剧集后
