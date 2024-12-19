import locale

MESSAGES = {
    "en": {
        "initializing": "🚀 Initializing system...",
        "not_initialized": "The current directory is not initialized as an auto-coder project.",
        "init_prompt": "Do you want to initialize the project now? (y/n): ",
        "init_success": "Project initialized successfully.",
        "init_fail": "Failed to initialize the project.",
        "init_manual": "Please try manually: auto-coder init --source_dir .",
        "exit_no_init": "Exiting without initialization.",
        "created_dir": "Created directory: {}",
        "init_complete": "Project initialization completed.",
        "checking_ray": "Checking Ray status...",
        "ray_not_running": "Ray is not running. Starting Ray...",
        "ray_start_success": "Ray started successfully.",
        "ray_start_fail": "Failed to start Ray. Please start it manually.",
        "ray_running": "Ray is already running.",
        "checking_model": "Checking deepseek_chat model availability...",
        "model_available": "deepseek_chat model is available.",
        "model_timeout": "Command timed out. deepseek_chat model might not be available.",
        "model_error": "Error occurred while checking deepseek_chat model.",
        "model_not_available": "deepseek_chat model is not available. Please choose a provider:",
        "provider_selection": "Select a provider for deepseek_chat model:",
        "no_provider": "No provider selected. Exiting initialization.",
        "enter_api_key": "Please enter your API key: ",
        "deploying_model": "Deploying deepseek_chat model using {}...",
        "deploy_complete": "Deployment completed.",
        "deploy_fail": "Deployment failed. Please try again or deploy manually.",
        "validating_deploy": "Validating the deployment...",
        "validation_success": "Validation successful. deepseek_chat model is now available.",
        "validation_fail": "Validation failed. The model might not be deployed correctly.",
        "manual_start": "Please try to start the model manually using:",
        "init_complete_final": "Initialization completed.",
        "project_type_config": "Project Type Configuration",
        "project_type_supports": "The project_type supports:",
        "language_suffixes": "  - Language suffixes (e.g., .py, .java, .ts)",
        "predefined_types": "  - Predefined types: py (Python), ts (TypeScript/JavaScript)",
        "mixed_projects": "For mixed language projects, use comma-separated values.",
        "examples": "Examples: '.java,.scala' or '.py,.ts'",
        "default_type": "Default is 'py' if left empty.",
        "enter_project_type": "Enter the project type: ",
        "project_type_set": "Project type set to:",
        "using_default_type": "Using default project type: py",
        "change_setting_later": "You can change this setting later using",
        "supported_commands": "Supported commands:",
        "commands": "Commands",
        "description": "Description",
        "add_files_desc": "Add files to the current session",
        "remove_files_desc": "Remove files from the current session",
        "chat_desc": "Chat with the AI about the current active files to get insights",
        "coding_desc": "Request the AI to modify code based on requirements",
        "ask_desc": "Ask the AI any questions or get insights about the current project, without modifying code",
        "summon_desc": "Summon the AI to perform complex tasks using the auto_tool agent",
        "revert_desc": "Revert commits from last coding chat",
        "conf_desc": "Set configuration. Use /conf project_type:<type> to set project type for indexing",
        "index_query_desc": "Query the project index",
        "index_build_desc": "Trigger building the project index",
        "list_files_desc": "List all active files in the current session",
        "help_desc": "Show this help message",
        "exclude_dirs_desc": "Add directories to exclude from project",
        "shell_desc": "Execute a shell command",
        "voice_input_desc": "Convert voice input to text",
        "mode_desc": "Switch input mode",
        "lib_desc": "Manage libraries",
        "exit_desc": "Exit the program",
        "design_desc": "Generate SVG image based on the provided description",
        "commit_desc": "Auto generate yaml file and commit changes based on user's manual changes",
    },
    "zh": {
        "initializing": "🚀 正在初始化系统...",
        "not_initialized": "当前目录未初始化为auto-coder项目。",
        "init_prompt": "是否现在初始化项目？(y/n): ",
        "init_success": "项目初始化成功。",
        "init_fail": "项目初始化失败。",
        "init_manual": "请尝试手动初始化：auto-coder init --source_dir .",
        "exit_no_init": "退出而不初始化。",
        "created_dir": "创建目录：{}",
        "init_complete": "项目初始化完成。",
        "checking_ray": "正在检查Ray状态...",
        "ray_not_running": "Ray未运行。正在启动Ray...",
        "ray_start_success": "Ray启动成功。",
        "ray_start_fail": "Ray启动失败。请手动启动。",
        "ray_running": "Ray已经在运行。",
        "checking_model": "正在检查deepseek_chat模型可用性...",
        "model_available": "deepseek_chat模型可用。",
        "model_timeout": "命令超时。deepseek_chat模型可能不可用。",
        "model_error": "检查deepseek_chat模型时出错。",
        "model_not_available": "deepseek_chat模型不可用。请选择一个提供商：",
        "provider_selection": "为deepseek_chat模型选择一个提供商：",
        "no_provider": "未选择提供商。退出初始化。",
        "enter_api_key": "请输入您的API密钥：",
        "deploying_model": "正在使用{}部署deepseek_chat模型...",
        "deploy_complete": "部署完成。",
        "deploy_fail": "部署失败。请重试或手动部署。",
        "validating_deploy": "正在验证部署...",
        "validation_success": "验证成功。deepseek_chat模型现在可用。",
        "validation_fail": "验证失败。模型可能未正确部署。",
        "manual_start": "请尝试使用以下命令手动启动模型：",
        "init_complete_final": "初始化完成。",
        "project_type_config": "项目类型配置",
        "project_type_supports": "项目类型支持：",
        "language_suffixes": "  - 语言后缀（例如：.py, .java, .ts）",
        "predefined_types": "  - 预定义类型：py（Python）, ts（TypeScript/JavaScript）",
        "mixed_projects": "对于混合语言项目，使用逗号分隔的值。",
        "examples": "示例：'.java,.scala' 或 '.py,.ts'",
        "default_type": "如果留空，默认为 'py'。",
        "enter_project_type": "请输入项目类型：",
        "project_type_set": "项目类型设置为：",
        "using_default_type": "使用默认项目类型：py",
        "change_setting_later": "您可以稍后使用以下命令更改此设置",
        "supported_commands": "支持的命令：",
        "commands": "命令",
        "description": "描述",
        "add_files_desc": "将文件添加到当前会话",
        "remove_files_desc": "从当前会话中移除文件",
        "chat_desc": "与AI聊天，获取关于当前活动文件的见解",
        "coding_desc": "根据需求请求AI修改代码",
        "ask_desc": "向AI提问或获取关于当前项目的见解，不修改代码",
        "summon_desc": "召唤AI使用auto_tool代理执行复杂任务",
        "revert_desc": "撤销上次代码聊天的提交",
        "conf_desc": "设置配置。使用 /conf project_type:<type> 设置索引的项目类型",
        "index_query_desc": "查询项目索引",
        "index_build_desc": "触发构建项目索引",
        "list_files_desc": "列出当前会话中的所有活动文件",
        "help_desc": "显示此帮助消息",
        "exclude_dirs_desc": "添加要从项目中排除的目录",
        "shell_desc": "执行shell命令",
        "voice_input_desc": "将语音输入转换为文本",
        "mode_desc": "切换输入模式",
        "lib_desc": "管理库",
        "exit_desc": "退出程序",
        "design_desc": "根据需求设计SVG图片",
        "commit_desc": "根据用户人工修改的代码自动生成yaml文件并提交更改",

    }
}


def get_system_language():
    try:
        return locale.getdefaultlocale()[0][:2]
    except:
        return 'en'


def get_message(key):
    lang = get_system_language()
    return MESSAGES.get(lang, MESSAGES['en']).get(key, MESSAGES['en'][key])
