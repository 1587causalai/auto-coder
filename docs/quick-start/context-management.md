# 上下文管理


## 上下文管理的设计

这个项目在上下文管理的过程中，他有什么独特的算法和设计？

根据提供的代码和文档，我可以分析出这个项目在上下文管理方面有以下几个独特的设计和算法：

1. **双模式上下文检索系统**

```text
# docs/zh/025-AutoCoder知识库写代码的两种上下文模式.md

但是对于召回的内容，如何给到大模型参考，实际上  AutoCoder 提供了两种上下文模式：

1. enable_rag_context
2. enable_rag_search

## enable_rag_context

enable_rag_context 会取第一个chunk 对应的文章，作为上下文，这个上下文会被作为一个普通的文件给到大模型。

## enable_rag_search

enable_rag_search 会对 topN 个chunk 根据问题进行回答，把回答结果作为上下文，这个上下文也会被作为一个普通的文件给到大模型。
```


项目提供了两种不同的上下文模式：
- enable_rag_context: 使用第一个chunk对应的完整文章作为上下文
- enable_rag_search: 对topN个chunks进行问题回答，将回答结果作为上下文

2. **三层过滤机制**
```text
# docs/zh/018-AutoCoder 索引过滤经验谈.md

startLine: 22
endLine: 27
```

实现了一个三步过滤算法：
- 精确匹配：根据query中提到的文件名进行匹配
- 语义匹配：对文件内部的符号(symbols)进行语义理解和匹配
- 依赖分析：分析找到文件的依赖关系

3. **相关性评分和智能筛选**

```python
# src/autocoder/rag/long_context_rag.py

# Filter relevant_docs to only include those with is_relevant=True
highly_relevant_docs = [
    doc for doc in relevant_docs if doc.relevance.is_relevant
]

if highly_relevant_docs:
    relevant_docs = highly_relevant_docs
    logger.info(f"Found {len(relevant_docs)} highly relevant documents")
```


系统会对文档进行相关性评分，优先使用高相关性的文档。如果找到高相关性文档，就只使用这些文档；如果没有找到高相关性文档，会添加特殊提示。

4. **可配置的过滤级别**
```text
# docs/zh/018-AutoCoder 索引过滤经验谈.md

startLine: 30
endLine: 32
```

通过 index_filter_level 参数(0-2)来控制过滤的严格程度，让用户可以根据需求调整上下文的范围。

5. **项目规模适应性**
```text
# docs/zh/命令行版Devin 来了_Auto-Coder.md

startLine: 268
endLine: 272
```

系统考虑到了两个核心问题：
- Token成本控制
- 大模型输入长度限制

为了解决这些问题，系统实现了智能索引机制：
```text
# docs/zh/命令行版Devin 来了_Auto-Coder.md

startLine: 294
endLine: 299
```

通过两步筛选过程：
1. 基于需求描述筛选相关源码文件
2. 分析一级依赖关系

这种设计确保了即使在大型项目中，也能保持较小的上下文范围，同时保证上下文的完整性和相关性。这是一个在工程实践中非常实用的平衡方案。
