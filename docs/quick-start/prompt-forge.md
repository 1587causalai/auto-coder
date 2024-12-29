# Prompt 优化

这个项目使用了什么用户 prompt 自动优化技巧？

从代码和文档中，我发现这个项目在 prompt 优化方面主要采用了以下技巧：

1. **基于 RAG 的智能搜索优化**

```yaml
# docs/zh/025-Two_Context_Modes_for_Writing_Code_in_AutoCoder_Knowledge_Base.md

enable_rag_search: | 
   byzerllm  使用 openai_tts模型的 python 代码
collections: byzerllm

query: | 
   我们要在 audio.py 中实现一个新的类叫 PlayStreamAudioFromText...
```

不是简单地把用户的 query 作为搜索条件，而是允许用户明确指定搜索内容，这样可以更精准地找到相关代码示例作为上下文。

2. **迭代式需求拆解**

```text
# docs/zh/015 - AutoCoder 迭代粒度拆解技巧.md

为什么需要拆解到这么细，而不是"Hey, 大模型，给我一个完美的Web网站，支持上传下载，支持实时显示后端信息" 这么一句话？

...如果拆解的过细，可能就有点浪费token和时间。但是如果拆解粒度太粗，就会有很多问题：
- 产出完全不符合预期
- 输入输出过大
- 后续难以人工微调
```

系统鼓励用户将大需求拆分成小的迭代步骤，每个步骤的 prompt 都更加精确和可控。

3. **多维度上下文组合**

```text
# docs/zh/004-AutoCoder 边看代码 边看文档 写代码.md

程序员单纯编程部分，无非是：
1. 理解需求
2. 搜索看别人怎么解决类似问题，理清思路
3. 看已有项目的代码
4. 看要用到的第三方库的源码或者文档
```

系统会自动组合多个维度的上下文：
- 项目现有代码
- 第三方库文档
- 搜索引擎结果
- 用户需求描述

4. **智能代理模式**

```python
# src/autocoder/agent/auto_tool.py

@byzerllm.prompt()
def context() -> str:
    """
    你坚定的相信，一切任务都可以编写  Python 代码来解决...
    你的目标是协助用户执行各种任务，包括但不限于代码生成、修改、测试等。
    """
```

系统为 AI 设定了明确的角色定位和行为准则，使其能更好地理解和执行用户的意图。

5. **自动化的文档引用**

```text
# docs/zh/048_AutoCoder如何辅助项目代码阅读.md

这样我可以人工选一些文件（有的时候系统自动找的文件太多，会导致最后问询失败），然后在 /ask 里让他主动阅读者几个文件的源码来回答我的问题
```

系统支持自动和手动选择相关文档，确保 prompt 中包含最相关的上下文信息。

6. **环境感知提示**

```python
# src/autocoder/agent/auto_tool.py

你当前运行的环境信息:
操作系统: {{ env_info.os_name }} {{ env_info.os_version }}
Python版本: {{ env_info.python_version }}
```

在 prompt 中自动包含环境信息，帮助 AI 生成更符合实际运行环境的代码。

7. **多模态输入支持**

```yaml
# docs/zh/039-AutoCoder_前端开发实战_1.md

/conf image_file:/Users/allwefantasy/projects/auto-coder.example_01/screens/add_example.png
```

支持图片等多模态输入，可以帮助 AI 更好地理解用户意图，特别是在前端开发场景。

这些技巧的组合使得系统能够：
- 更准确地理解用户意图
- 生成更高质量的代码
- 减少不必要的上下文信息
- 提高代码生成的成功率
- 支持更复杂的开发场景
