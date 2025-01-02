import time
from typing import List, Dict, Tuple
from autocoder.common.types import Mode, CodeGenerateResult
from autocoder.common import AutoCoderArgs
import byzerllm
from autocoder.utils.queue_communicate import queue_communicate, CommunicateEvent, CommunicateEventType
from autocoder.common import sys_prompt
from concurrent.futures import ThreadPoolExecutor
import json


class CodeAutoGenerateDiff:
    def __init__(
        self, llm: byzerllm.ByzerLLM, args: AutoCoderArgs, action=None
    ) -> None:
        self.llm = llm
        self.args = args
        self.action = action
        self.llms = []
        self.generate_times_same_model = args.generate_times_same_model
        if not self.llm:
            raise ValueError(
                "Please provide a valid model instance to use for code diff generation."
            )
        self.llms = self.llm.get_sub_client("code_model") or [self.llm]
        if not isinstance(self.llms, list):
            self.llms = [self.llms]

    @byzerllm.prompt(llm=lambda self: self.llm)
    def multi_round_instruction(
        self, instruction: str, content: str, context: str = ""
    ) -> str:
        """
        如果你需要生成代码，对于每个需要更改的文件，写出类似于 unified diff 的更改，就像`diff -U0`会产生的那样。
        下面是一些生成diff的要求：
        Make sure you include the first 2 lines with the file paths.
        Don't include timestamps with the file paths.

        Start each hunk of changes with a `@@ ... @@` line.
        Don't include line numbers like `diff -U0` does.
        The user's patch tool doesn't need them.

        The user's patch tool needs CORRECT patches that apply cleanly against the current contents of the file!
        Think carefully and make sure you include and mark all lines that need to be removed or changed as `-` lines.
        Make sure you mark all new or modified lines with `+`.
        Don't leave out any lines or the diff patch won't apply correctly.

        Indentation matters in the diffs!

        Start a new hunk for each section of the file that needs changes.

        Only output hunks that specify changes with `+` or `-` lines.
        Skip any hunks that are entirely unchanging ` ` lines.

        Output hunks in whatever order makes the most sense.
        Hunks don't need to be in any particular order.

        When editing a function, method, loop, etc use a hunk to replace the *entire* code block.
        Delete the entire existing version with `-` lines and then add a new, updated version with `+` lines.
        This will help you generate correct code and correct diffs.

        To move code within a file, use 2 hunks: 1 to delete it from its current location, 1 to insert it in the new location.

        To make a new file, show a diff from `--- /dev/null` to `+++ path/to/new/file.ext`.

        The path start with `---` or `+++` should be the absolute path of the file or relative path from the project root.

        下面我们来看一个例子：

        当前项目目录结构：
        1. 项目根目录： /tmp/projects/mathweb
        2. 项目子目录/文件列表(类似tree 命令输出)
        flask/
            app.py
            templates/
                index.html
            static/
                style.css

        用户需求： 请将下面的代码中的is_prime()函数替换为sympy。
        回答：
        好的，我会先罗列出需要的修改步骤，然后再列出diff。
        修改步骤：
        1. 添加sympy的import 语句。
        2. 删除is_prime()函数。
        3. 将现有对is_prime()的调用替换为sympy.isprime()。

        下面是这些变更的diff：

        ```diff
        --- /tmp/projects/mathweb/flask/app.py
        +++ /tmp/projects/mathweb/flask/app.py
        @@ ... @@
        -class MathWeb:
        +import sympy
        +
        +class MathWeb:
        @@ ... @@
        -def is_prime(x):
        -    if x < 2:
        -        return False
        -    for i in range(2, int(math.sqrt(x)) + 1):
        -        if x % i == 0:
        -            return False
        -    return True
        @@ ... @@
        -@app.route('/prime/<int:n>')
        -def nth_prime(n):
        -    count = 0
        -    num = 1
        -    while count < n:
        -        num += 1
        -        if is_prime(num):
        -            count += 1
        -    return str(num)
        +@app.route('/prime/<int:n>')
        +def nth_prime(n):
        +    count = 0
        +    num = 1
        +    while count < n:
        +        num += 1
        +        if sympy.isprime(num):
        +            count += 1
        +    return str(num)
        ```

        现在让我们开始一个新的任务:

        {%- if structure %}
        {{ structure }}
        {%- endif %}

        {%- if content %}
        下面是一些文件路径以及每个文件对应的源码：

        {{ content }}
        {%- endif %}

        {%- if context %}
        {{ context }}
        {%- endif %}

        下面是用户的需求：

        {{ instruction }}

        每次生成一个文件的diff，然后询问我是否继续，当我回复继续，继续生成下一个文件的diff。当没有后续任务时，请回复 "__完成__" 或者 "__EOF__"。
        """

        if not self.args.include_project_structure:
            return {
                "structure": ""
            }

        return {
            "structure": (
                self.action.pp.get_tree_like_directory_structure()
                if self.action
                else ""
            )
        }

    @byzerllm.prompt(llm=lambda self: self.llm)
    def single_round_instruction(
        self, instruction: str, content: str, context: str = ""
    ) -> str:
        """
        如果你需要生成代码，对于每个需要更改的文件，写出类似于 unified diff 的更改，就像`diff -U0`会产生的那样。
        下面是一些生成diff的要求：
        Make sure you include the first 2 lines with the file paths.
        Don't include timestamps with the file paths.

        Start each hunk of changes with a `@@ ... @@` line.
        Don't include line numbers like `diff -U0` does.
        The user's patch tool doesn't need them.

        The user's patch tool needs CORRECT patches that apply cleanly against the current contents of the file!
        Think carefully and make sure you include and mark all lines that need to be removed or changed as `-` lines.
        Make sure you mark all new or modified lines with `+`.
        Don't leave out any lines or the diff patch won't apply correctly.

        Indentation matters in the diffs!

        Start a new hunk for each section of the file that needs changes.

        Only output hunks that specify changes with `+` or `-` lines.
        Skip any hunks that are entirely unchanging ` ` lines.

        Output hunks in whatever order makes the most sense.
        Hunks don't need to be in any particular order.

        When editing a function, method, loop, etc use a hunk to replace the *entire* code block.
        Delete the entire existing version with `-` lines and then add a new, updated version with `+` lines.
        This will help you generate correct code and correct diffs.

        To move code within a file, use 2 hunks: 1 to delete it from its current location, 1 to insert it in the new location.

        To make a new file, show a diff from `--- /dev/null` to `+++ path/to/new/file.ext`.

        The path start with `---` or `+++` should be the absolute path of the file or relative path from the project root.

        下面我们来看一个例子：

        当前项目目录结构：
        1. 项目根目录： /tmp/projects/mathweb
        2. 项目子目录/文件列表(类似tree 命令输出)
        flask/
            app.py
            templates/
                index.html
            static/
                style.css

        用户需求： 请将下面的代码中的is_prime()函数替换为sympy。
        回答：
        好的，我会先罗列出需要的修改步骤，然后再列出diff。
        修改步骤：
        1. 添加sympy的import 语句。
        2. 删除is_prime()函数。
        3. 将现有对is_prime()的调用替换为sympy.isprime()。

        下面是这些变更的diff：

        ```diff
        --- /tmp/projects/mathweb/flask/app.py
        +++ /tmp/projects/mathweb/flask/app.py
        @@ ... @@
        -class MathWeb:
        +import sympy
        +
        +class MathWeb:
        @@ ... @@
        -def is_prime(x):
        -    if x < 2:
        -        return False
        -    for i in range(2, int(math.sqrt(x)) + 1):
        -        if x % i == 0:
        -            return False
        -    return True
        @@ ... @@
        -@app.route('/prime/<int:n>')
        -def nth_prime(n):
        -    count = 0
        -    num = 1
        -    while count < n:
        -        num += 1
        -        if is_prime(num):
        -            count += 1
        -    return str(num)
        +@app.route('/prime/<int:n>')
        +def nth_prime(n):
        +    count = 0
        +    num = 1
        +    while count < n:
        +        num += 1
        +        if sympy.isprime(num):
        +            count += 1
        +    return str(num)
        ```

        现在让我们开始一个新的任务:

        {%- if structure %}
        {{ structure }}
        {%- endif %}

        {%- if content %}
        下面是一些文件路径以及每个文件对应的源码：

        {{ content }}
        {%- endif %}

        {%- if context %}
        {{ context }}
        {%- endif %}

        下面是用户的需求：

        {{ instruction }}
        """

        if not self.args.include_project_structure:
            return {
                "structure": ""
            }

        return {
            "structure": (
                self.action.pp.get_tree_like_directory_structure()
                if self.action
                else ""
            )
        }

    def single_round_run(
        self, query: str, source_content: str
    ) -> CodeGenerateResult:
        llm_config = {"human_as_model": self.args.human_as_model}

        if self.args.template == "common":
            init_prompt = self.single_round_instruction.prompt(
                instruction=query, content=source_content, context=self.args.context
            )
        elif self.args.template == "auto_implement":
            init_prompt = self.auto_implement_function.prompt(
                instruction=query, content=source_content
            )

        with open(self.args.target_file, "w") as file:
            file.write(init_prompt)

        conversations = []

        if self.args.system_prompt and self.args.system_prompt.strip() == "claude":
            conversations.append(
                {"role": "system", "content": sys_prompt.claude_sys_prompt.prompt()})
        elif self.args.system_prompt:
            conversations.append(
                {"role": "system", "content": self.args.system_prompt})

        conversations.append({"role": "user", "content": init_prompt})

        if self.args.request_id and not self.args.skip_events:
            _ = queue_communicate.send_event(
                request_id=self.args.request_id,
                event=CommunicateEvent(
                    event_type=CommunicateEventType.CODE_GENERATE_START.value,
                    data=json.dumps({}, ensure_ascii=False),
                ),
            )

        conversations_list = []
        results = []
        if not self.args.human_as_model:
            with ThreadPoolExecutor(max_workers=len(self.llms) * self.generate_times_same_model) as executor:
                futures = []
                for llm in self.llms:
                    for _ in range(self.generate_times_same_model):
                        futures.append(executor.submit(
                            llm.chat_oai, conversations=conversations, llm_config=llm_config))
                results = [future.result()[0].output for future in futures]
            for result in results:
            for result in results:
                conversations_list.append(
                    conversations + [{"role": "assistant", "content": result}])
            print(f"Code generation time cost: {time.monotonic() - start_time} seconds")
        else:
            results = []
            conversations_list = []
            for _ in range(self.args.human_model_num):
                v = self.llms[0].chat_oai(
                    conversations=conversations, llm_config=llm_config)
                results.append(v[0].output)
                conversations_list.append(conversations + [{"role": "assistant", "content": v[0].output}])
            print(f"Code generation time cost: {time.monotonic() - start_time} seconds")

        if self.args.request_id and not self.args.skip_events:
            _ = queue_communicate.send_event(
                request_id=self.args.request_id,
                event=CommunicateEvent(
                    event_type=CommunicateEventType.CODE_GENERATE_END.value,
                    data=json.dumps({}, ensure_ascii=False),
                ),
            )

        return CodeGenerateResult(contents=results, conversations=conversations_list)

    def multi_round_run(
        self, query: str, source_content: str, max_steps: int = 10
    ) -> CodeGenerateResult:
        llm_config = {"human_as_model": self.args.human_as_model}
        result = []

        if self.args.template == "common":
            init_prompt = self.multi_round_instruction.prompt(
                instruction=query, content=source_content, context=self.args.context
            )
        elif self.args.template == "auto_implement":
            init_prompt = self.auto_implement_function.prompt(
                instruction=query, content=source_content
            )

        conversations = []
        # conversations.append({"role": "system", "content": sys_prompt.prompt()})
        conversations.append({"role": "user", "content": init_prompt})

        with open(self.args.target_file, "w") as file:
            file.write(init_prompt)

        code_llm = self.llms[0]
        t = code_llm.chat_oai(conversations=conversations,
                              llm_config=llm_config)

        result.append(t[0].output)

        conversations.append({"role": "assistant", "content": t[0].output})

        if "__完成__" in t[0].output or "/done" in t[0].output or "__EOF__" in t[0].output:
            return CodeGenerateResult(contents=["\n\n".join(result)], conversations=[conversations])

        current_step = 0

        while current_step < max_steps:

            conversations.append({"role": "user", "content": "继续"})

            with open(self.args.target_file, "w") as file:
                file.write("继续")

            t = code_llm.chat_oai(
                conversations=conversations, llm_config=llm_config)

            result.append(t[0].output)
            conversations.append({"role": "assistant", "content": t[0].output})
            current_step += 1

            if "__完成__" in t[0].output or "/done" in t[0].output or "__EOF__" in t[0].output:
                return CodeGenerateResult(contents=["\n\n".join(result)], conversations=[conversations])

        return CodeGenerateResult(contents=["\n\n".join(result)], conversations=[conversations])
