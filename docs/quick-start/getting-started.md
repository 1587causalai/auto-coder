# AutoCoder 快速入门

您的开发新方式是：

1. 编写一个YAML文件来描述您的需求，Auto-Coder将生成代码并将代码合并到您的项目中。
2. 检查Auto-Coder的提交，并在vscode或其他IDE中审查被提交的代码。
3. 如果提交是基本满意，您可以选择使用github copilot或其他工具手动对代码进行微调，或者直接继续下一步工作。
4. 如果提交的代码不满足你需求，您需要撤销提交并修改YAML文件，重新执行。
5. 重复上述步骤，直到完成你的需求。


## 什么是 AutoCoder？

AutoCoder 是一个 AI 编程助手工具，它的独特之处在于：
- 模拟真实程序员的开发行为
- 能够理解和参考已有项目代码
- 支持迭代式开发
- 提供多种使用方式

## 使用方式

AutoCoder 提供了三种使用方式，你可以根据自己的需求选择：

### 1. VSCode 插件方式（推荐新手使用）

1. 安装准备：
   
```bash
# 1. 先安装 Python 包
pip install auto-coder
# 2. 在 VSCode 中安装插件
# 搜索 "auto-coder-copilot" 并安装
```

2. 使用步骤：
- 在 VSCode 中打开项目
- 右键项目目录，选择 "auto-coder: 初始化项目"
- 右键创建需求（会生成 YAML 文件）
- 右键 YAML 文件执行

### 2. 命令行方式（Python 包）

```bash
# 1. 安装
pip install auto-coder

# 2. 初始化项目
cd your-project
auto-coder init --source_dir .

# 3. 创建并编辑需求文件
# actions/001_我的第一个修改.yml
include_file:
  - ./base/base.yml
query: |
  实现新功能...

# 4. 执行需求
auto-coder --file actions/001_我的第一个修改.yml
```

### 3. 交互式命令行（Chat-Auto-Coder）

```bash
# 启动交互式界面
chat-auto-coder

# 常用命令
/conf project_type:py    # 设置项目类型
/index/build            # 构建项目索引
/ask                    # 询问项目相关问题
/coding                 # 生成代码
```

## 工作流程示例

1. **创建需求**：

```yaml
# actions/001_feature.yml
include_file:
  - ./base/base.yml
  
query: |
  在 src/server.py 中添加一个新的 API 接口 /hello
```

2. **执行需求**：
- VSCode 插件：右键 YAML 文件 -> "auto-coder: 执行"
- 命令行：`auto-coder --file actions/001_feature.yml`

3. **审查代码**：
- 在 IDE 中查看生成的代码
- 根据需要进行调整
- 如果不满意，可以撤销并修改需求重试

## 使用建议

1. **新手入门**：
- 建议从 VSCode 插件开始
- 先尝试小型修改任务
- 熟悉 YAML 配置的写法

2. **进阶使用**：
- 使用 chat-auto-coder 交互式界面
- 尝试不同的代码合并策略
- 学习如何拆分大型需求

3. **最佳实践**：
- 保持需求粒度适中
- 提供清晰的上下文信息
- 善用已有代码作为参考
- 采用迭代式开发方式

## 注意事项

1. 确保已安装 Python 环境
2. VSCode 插件依赖于 Python 包，需要先安装 auto-coder
3. 建议先在测试项目中熟悉工具的使用
4. 代码生成效果与需求描述的质量密切相关

## 下一步

- 阅读详细文档了解更多配置选项
- 尝试在实际项目中应用
- 探索更高级的功能（如自定义模型配置）

---

这个快速入门文档基于实际的代码和文档编写，内容准确可靠。如果你发现任何问题或需要补充，欢迎提出建议。 