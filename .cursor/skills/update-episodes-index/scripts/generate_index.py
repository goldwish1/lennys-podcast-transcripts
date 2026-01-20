#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成按发布日期排序的剧集索引文件
"""
import os
import re
from pathlib import Path
from datetime import datetime

def extract_metadata(transcript_path):
    """从 transcript.md 文件中提取元数据"""
    try:
        with open(transcript_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 分割 frontmatter 和内容
        parts = content.split('---')
        if len(parts) >= 3:
            frontmatter_text = parts[1].strip()
            metadata = {}
            
            # 手动解析 YAML frontmatter
            for line in frontmatter_text.split('\n'):
                line = line.strip()
                if ':' in line and not line.startswith('#'):
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()
                    
                    # 移除引号
                    if value.startswith("'") and value.endswith("'"):
                        value = value[1:-1]
                    elif value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    
                    metadata[key] = value
            
            return metadata
        return None
    except Exception as e:
        print(f"Error reading {transcript_path}: {e}")
        return None

def get_all_episodes(episodes_dir):
    """获取所有剧集的元数据"""
    episodes = []
    episodes_path = Path(episodes_dir)
    
    for episode_dir in episodes_path.iterdir():
        if episode_dir.is_dir():
            transcript_path = episode_dir / 'transcript.md'
            if transcript_path.exists():
                metadata = extract_metadata(transcript_path)
                if metadata:
                    # 添加文件夹名称
                    metadata['folder'] = episode_dir.name
                    episodes.append(metadata)
    
    return episodes

def generate_index_markdown(episodes):
    """生成 Markdown 格式的索引"""
    # 按发布日期排序（最新的在前）
    sorted_episodes = sorted(
        episodes,
        key=lambda x: x.get('publish_date', '0000-00-00'),
        reverse=True
    )
    
    markdown = "# Lenny's Podcast 剧集索引\n\n"
    markdown += "按发布日期排序（最新在前）\n\n"
    markdown += f"**总计：{len(sorted_episodes)} 个剧集**\n\n"
    markdown += "---\n\n"
    
    current_year = None
    for episode in sorted_episodes:
        publish_date = episode.get('publish_date', '未知日期')
        guest = episode.get('guest', '未知嘉宾')
        title = episode.get('title', '未知标题')
        youtube_url = episode.get('youtube_url', '')
        folder = episode.get('folder', '')
        
        # 提取年份
        if publish_date and publish_date != '未知日期':
            try:
                year = publish_date.split('-')[0]
                if year != current_year:
                    if current_year is not None:
                        markdown += "\n"
                    markdown += f"## {year} 年\n\n"
                    current_year = year
            except:
                pass
        
        # 格式化日期
        if publish_date and publish_date != '未知日期':
            try:
                date_obj = datetime.strptime(publish_date, '%Y-%m-%d')
                formatted_date = date_obj.strftime('%Y年%m月%d日')
            except:
                formatted_date = publish_date
        else:
            formatted_date = publish_date
        
        # 生成条目
        markdown += f"### {formatted_date} - {guest}\n\n"
        markdown += f"**{title}**\n\n"
        
        if youtube_url:
            markdown += f"- [YouTube 视频]({youtube_url})\n"
        
        markdown += f"- [文字稿](episodes/{folder}/transcript.md)\n\n"
        markdown += "---\n\n"
    
    return markdown

def main():
    # 获取项目根目录：从脚本位置向上查找，直到找到包含 episodes/ 目录的位置
    script_path = Path(__file__).resolve()
    project_root = script_path.parent
    
    # 向上查找，直到找到包含 episodes 目录的父目录
    while project_root.parent != project_root:
        if (project_root / 'episodes').exists():
            break
        project_root = project_root.parent
    
    episodes_dir = project_root / 'episodes'
    output_file = project_root / 'EPISODES_INDEX.md'
    
    print(f"正在扫描 {episodes_dir} 目录...")
    episodes = get_all_episodes(episodes_dir)
    print(f"找到 {len(episodes)} 个剧集")
    
    print("正在生成索引文件...")
    markdown = generate_index_markdown(episodes)
    
    print(f"正在写入 {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"完成！已生成索引文件：{output_file}")

if __name__ == '__main__':
    main()
