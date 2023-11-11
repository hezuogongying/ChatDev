维基
快速入门分步
1. 安装：ChatDev
有关安装说明，请访问自述文件的快速入门部分。
2. 通过一个命令开始构建软件：
构建您的软件：使用以下命令启动软件的构建， 替换为您的想法描述和您想要的项目 名字：[description_of_your_idea][project_name]

python3 run.py --task "[description_of_your_idea]" --name "[project_name]"
以下是 run.py 的完整参数

usage: run.py [-h] [--config CONFIG] [--org ORG] [--task TASK] [--name NAME] [--model MODEL]

argparse

optional arguments:
  -h, --help       show this help message and exit
  --config CONFIG  Name of config, which is used to load configuration under CompanyConfig/; Please see CompanyConfig Section below
  --org ORG        Name of organization, your software will be generated in WareHouse/name_org_timestamp
  --task TASK      Prompt of your idea
  --name NAME      Name of software, your software will be generated in WareHouse/name_org_timestamp
  --model MODEL    GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K'}
3. 检查您的软件
生成的软件位于 下，包括：WareHouse/NAME_ORG_timestamp
该软件的所有文件和手册
制作该软件的公司的配置文件，包括三个配置 JSON 文件
软件构建过程的完整日志
提示制作本软件
todo软件的一个案例如下，它位于/WareHouse/todo_THUNLP_20230822165503
.
├── 20230822165503.log # log file
├── ChatChainConfig.json # Configuration
├── PhaseConfig.json # Configuration
├── RoleConfig.json # Configuration
├── todo.prompt # User query prompt
├── meta.txt # Software building meta information
├── main.py # Generated Software Files
├── manual.md # Generated Software Files
├── todo_app.py # Generated Software Files
├── task.py # Generated Software Files
└── requirements.txt # Generated Software Files
通常，您只需要安装需求并运行 main.py 即可使用您的软件
cd WareHouse/project_name_DefaultOrganization_timestamp
pip3 install -r requirements.txt
python3 main.py
本地演示
您可以先启动 Flask 应用获取本地 Demo，包括增强的可视化日志、回放 Demo 和简单的 ChatChain 可视化工具。
python3 online_log/app.py
然后前往本地演示网站，查看日志的在线可视化版本，例如

演示

您也可以转到此页面上的ChatChain可视化工具，然后 上传任何 under 以获得此链上的可视化效果，例如：ChatChainConfig.jsonCompanyConfig/
ChatChain可视化工具

您也可以转到聊天回放页面以重播软件文件夹中的日志文件
点击底部上传日志，然后点击File UploadReplay
重播仅显示代理之间自然语言的对话，不包含调试日志。


Docker 启动
您可以使用 docker 快速安全地使用 ChatDev。您将需要一些额外的步骤来允许在 docker 中执行 GUI 程序，因为 ChatDev 经常使用 GUI 创建软件并在测试阶段执行它们。
安装 Docker
请参考 Docker 官网安装 Docker。
准备 Host 和 Docker 之间的 GUI 连接
以macOS为例，
安装 Socat 和 Xquartz，安装 Xquartz 后可能需要重启电脑
brew install socat xquartz
打开XQquartz并进入设置，允许来自网络客户端的连接
Xquartz（石英）
在主机上运行以下命令并保留它。
 socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
在主机上运行以下命令以检查您的 IP（INET 的地址）。
ifconfig en0
构建 Docker 镜像
在 ChatDev 文件夹下，运行它将生成一个名为 chatdev 的 400MB+ docker 镜像。
docker build -t chatdev:latest .
运行 Docker
运行以下命令以创建并进入容器
docker run -it -p 8000:8000 -e OPENAI_API_KEY=YOUR_OPENAI_KEY -e DISPLAY=YOUR_IP:0 chatdev:latest
⚠️您需要替换为您的密钥并替换为您的 inet 地址。YOUR_OPENAI_KEYYOUR_IP
然后你就可以玩ChatDev运行了。python3 run.py
您可以先运行以启动后台程序，以便可以将在线日志与 WebUI 一起使用。python3 online_log/app.py &
将生成的软件从 Docker 中复制出来
跑
docker cp container_id:/path/in/container /path/on/host
官方 Docker 镜像
准备中
定制
您可以按三种粒度自定义您的公司：
自定义ChatChain
自定义阶段
自定义角色
下面是 ChatDev 的概述架构，它说明了上述三个类之间的关系：
拱

所有与 ChatDev 相关的配置内容（例如代理员工的后台提示、每个 Phase 的工作内容、Phase 如何组合成一个 ChatChain），都称为 CompanyConfig（因为 ChatDev 就像一个虚拟软件公司）。这些 CompanyConfig 位于 ChatDev 项目的 Under 下。您可以检查此目录。在此目录中，您将看到不同的 CompanyConfig（例如 Default、Art、Human）。一般来说，每个 CompanyConfig 将包含 3 个配置文件。CompanyConfig/
ChatChainConfig.json，控制 ChatDev 的整体开发过程，包括每一步是哪个 Phase、每个 Phase 需要循环多少次、是否需要 reflect 等。
PhaseConfig.json，用于控制每个阶段，对应于 ChatDev 项目或位于 ChatDev 项目中。Python文件实现了每个阶段的具体工作逻辑。这里的json文件包含了每个阶段的配置，比如后台提示，哪些员工参与了这个阶段等。chatdev/phase.pychatdev/composed_phase.py
RoleConfig.json 包含每个员工（代理）的配置。目前，它只包含每个员工的背景提示，这是一堆包含占位符的文本。
如果一个 CompanyConfig 不包含所有三个配置文件（如 Art 和 Human），则表示此 CompanyConfig 中缺少的配置文件是按照 Default 设置的。目前提供的官方 CompanyConfigs 包括：
默认，默认配置
Art，允许 ChatDev 根据需要创建图片文件，自动生成图片描述提示并调用 openai 文生图 API 生成图片
Human，允许人类用户参与 ChatDev 的代码审查过程
自定义ChatChain
看CompanyConfig/Default/ChatChainConfig.json
您可以轻松地选择和组织阶段，以从所有阶段（从 或 ） 中制定 ChatChain 通过修改 JSON 文件chatdev/phase.pychatdev/composed_phase.py
自定义阶段
这是唯一需要修改代码的部分，它为自定义带来了很大的灵活性。
你只需要
实现 Phase 类（在最简单的情况下，只需要修改一个函数）扩展类Phase
配置此阶段，包括编写阶段提示和为此阶段分配角色PhaseConfig.json
自定义 SimplePhase
有关配置，请参阅有关实现 自有阶段CompanyConfig/Default/PhaseConfig.jsonchatdev/phase.py
每个阶段包含三个步骤：
从整个chatchain环境中生成阶段环境
使用阶段环境来控制阶段提示，并执行此阶段中角色之间的聊天（其中 通常不需要修改）
从聊天中获取研讨会结论，并用它来更新整个聊天链环境
以下是选择软件编程语言的简单示例阶段：
生成阶段环境：我们从聊天链环境中选择任务、模式和想法
执行 phase：无需实现，在 Phase 类中定义
更新聊天链环境：我们得到研讨会结论（哪种语言）并更新 chatchain环境 此阶段的配置如下：
class LanguageChoose(Phase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_phase_env(self, chat_env):
        self.phase_env.update({"task": chat_env.env_dict['task_prompt'],
                               "modality": chat_env.env_dict['modality'],
                               "ideas": chat_env.env_dict['ideas']})

    def update_chat_env(self, chat_env) -> ChatEnv:
        if len(self.seminar_conclusion) > 0 and "<INFO>" in self.seminar_conclusion:
            chat_env.env_dict['language'] = self.seminar_conclusion.split("<INFO>")[-1].lower().replace(".", "").strip()
        elif len(self.seminar_conclusion) > 0:
            chat_env.env_dict['language'] = self.seminar_conclusion
        else:
            chat_env.env_dict['language'] = "Python"
        return chat_env
"LanguageChoose": {
  "assistant_role_name": "Chief Technology Officer",
  "user_role_name": "Chief Executive Officer",
  "phase_prompt": [
    "According to the new user's task and some creative brainstorm ideas listed below: ",
    "Task: \"{task}\".",
    "Modality: \"{modality}\".",
    "Ideas: \"{ideas}\".",
    "We have decided to complete the task through an executable software implemented via a programming language. ",
    "As the {assistant_role}, to satisfy the new user's demand and make the software realizable, you should propose a concrete programming language. If python can complete this task via Python, please answer Python; otherwise, answer another programming language (e.g., Java, C++, etc,).",
    "Note that we must ONLY discuss the target programming language and do not discuss anything else! Once we all have expressed our opinion(s) and agree with the results of the discussion unanimously, any of us must actively terminate the discussion and conclude the best programming language we have discussed without any other words or reasons, using the format: \"<INFO> *\" where \"*\" represents a programming language."
  ]
}
自定义 ComposePhase
请参阅配置和查看 实现。CompanyConfig/Default/ChatChainConfig.jsonchatdev/composed_phase.py
⚠️注意力我们还不支持嵌套组合，因此不要将 ComposePhase 放在 ComposePhase 中。
ComposePhase 包含多个 SimplePhase，可以循环进行。
ComposePhase 没有 Phase json，但在聊天链 json 文件中，您可以定义其中的 SimplePhase ComposePhase，例如：
  {
    "phase": "CodeReview",
    "phaseType": "ComposedPhase",
    "cycleNum": 2,
    "Composition": [
      {
        "phase": "CodeReviewComment",
        "phaseType": "SimplePhase",
        "max_turn_step": -1,
        "need_reflect": "False"
      },
      {
        "phase": "CodeReviewModification",
        "phaseType": "SimplePhase",
        "max_turn_step": -1,
        "need_reflect": "False"
      }
    ]
  }
您还需要实现自己的 ComposePhase 类，您需要该类来决定phase_env更新和 chat_env更新（与 SimplePhase 相同，但适用于整个 ComposePhase）和停止 循环（可选）：
class Test(ComposedPhase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_phase_env(self, chat_env):
        self.phase_env = dict()

    def update_chat_env(self, chat_env):
        return chat_env

    def break_cycle(self, phase_env) -> bool:
        if not phase_env['exist_bugs_flag']:
            log_and_print_online(f"**[Test Info]**\n\nAI User (Software Test Engineer):\nTest Pass!\n")
            return True
        else:
            return False
自定义角色
看CompanyConfig/Default/RoleConfig.json
可以使用占位符来使用 phase 环境，这与 PhaseConfig.json 相同
⚠️注意力你至少需要保留“首席执行官”和“顾问”才能使 Reflection 发挥作用。RoleConfig.json
ChatChain参数
clear_structure：清理缓存文件夹。
头脑风暴：待定
gui_design：是否为软件创建图形用户界面。
git_management：是否在软件项目上打开 Git 管理。
self_improve：用户输入提示的自我改进标志。LLM作为提示播放的特殊聊天 工程师改进用户输入提示。⚠️注意力模型生成的提示包含不确定性，并且可能存在 与原始提示中包含的要求含义存在偏差。
SimplePhase 中的参数：
max_turn_step：最大聊天回合数。您可以增加max_turn_step以获得更好的性能，但它会 需要更长的时间才能完成该阶段。
need_reflect：反射标志。反射是一个特殊的阶段，在一个阶段之后自动执行。它 将开始顾问和CEO之间的聊天，以完善阶段聊天的结论。
ComposedPhase 中的参数
cycleNum：在此 ComposedPhase 中执行 SimplePhase 的周期数。
项目结构
├── CompanyConfig # Configuration Files for ChatDev, including ChatChain, Phase and Role config json.
├── WareHouse # Folder for generated software
├── camel # Camel RolePlay component
├── chatdev # ChatDev core code
├── misc # assets of example and demo
├── online_log # Demo Folder
├── run.py # Entry of ChatDev
├── requirements.txt
├── README.md
└── wiki.md
公司配置
违约
演示

如默认设置的ChatChain可视化所示，ChatDev将按以下顺序生成软件：
需求分析：决定软件的模式
语言选择：决定编程语言
编码：编写代码
CodeCompleteAll：完成缺少的函数/类
CodeReview：查看和修改代码
测试：运行软件，根据测试报告修改代码
EnvironmentDoc：编写环境文档
手册：编写手册
您可以使用默认设置。python3 run.py --config "Default"
艺术
演示

与“默认”相比，“艺术”设置在 CodeCompleteAll 之前添加了一个名为“艺术”的阶段
艺术阶段将首先讨论图像资产的名称和描述，然后用于根据描述生成图像。openai.Image.create
您可以使用默认设置，使用或忽略 config 参数。python3 run.py --config "Art"
人机交互
演示

与 Default 相比，在 Human-Agent-Interaction 模式下，您可以扮演审阅者，并要求程序员代理根据您的评论修改代码。
它在 dCodeReview 阶段之后添加了一个名为 HumanAgentInteraction 的阶段。
您可以使用 Human-Agent-Interaction 设置。python3 run.py --config "Human"
当 chatdev 执行到此阶段时，在命令界面上，您将看到一个要求输入的提示。
您可以在其中运行您的软件，看看它是否满足您的需求。然后，您可以在命令界面中键入所需的任何内容（错误修复或新功能），然后按Enter键：WareHouse/Human_command
例如
我们首先运行带有任务“设计五子棋游戏”的 ChatDev
然后，我们在 HumanAgentInteraction 阶段键入“请添加重启按钮”，添加第一个功能
在 HumanAgentInteraction 的第二个循环中，我们通过键入“请添加当前状态栏来显示轮到谁”来添加另一个功能。
最后，我们通过键入“结束”提前退出此模式。
下面显示了所有三个版本。
        
Git 模式
只需设置为 in 即可启用 Git 模式，在该模式下，ChatDev 会将生成的软件文件夹设为 git 存储库并自动进行所有提交。"git_management""True"ChatChainConfig.json
对生成的软件代码所做的每一次更改都将创建一个提交，包括：
初始提交，在阶段完成后创建，带有提交消息。CodingFinish Coding
完成阶段，带有提交消息。ArtIntegrationFinish Art Integration
Complete 阶段，带有提交消息（如果 CodeComplete 在三个循环中执行）。CodeCompleteCode Complete #1/2/3 Finished
完成阶段，并显示提交消息（如果 CodeReviewModification 在三个循环中执行）。CodeReviewModificationReview #1/2/3 Finished
完成阶段，带有提交消息（如果 CodeReviewHuman 在三个循环中执行）。CodeReviewHumanHuman Review #1/2/3 Finished
完成阶段，带有提交消息（如果 TestModification 在三个循环中执行）。TestModificationTest #1/2/3 Finished
所有阶段均已完成，并显示提交消息。Final Version
在终端和在线日志 UI 上，您可以在流程结束时看到 git 摘要。
    
您还可以在日志文件中搜索以查看提交发生的时间。git Information
⚠️关于 Git 模式，有几点值得注意：
ChatDev 是一个 git 项目，我们需要在生成的软件文件夹中创建另一个 git 项目，所以我们用这个“git over git”函数来制作。将创建一个文件。git submodule.gitmodule
在 software 文件夹下，您可以像普通 git 项目一样添加/提交/推送/检出软件项目，并且您的提交不会修改 ChatDev git 历史记录。
在 ChatDev 文件夹下，新软件已作为一个整体添加到 ChatDev 文件夹中。
生成的日志文件不会添加到软件 git 项目中，因为日志在最终提交后会关闭并移动到软件文件夹。我们必须这样做，因为日志应该记录所有 git 提交，包括最后一个。因此，git 操作必须在日志最终确定之前完成。您将始终在软件文件夹中看到要添加和提交的日志文件，例如：
img.png
当你在 ChatDev 项目下执行时，会有这样的信息（以 Gomoku 为例）：如果在 software 文件夹下添加并提交软件日志文件，则不会有git add .
Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
        new file:   .gitmodules
        new file:   WareHouse/Gomoku_GitMode_20231025184031

Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
    (commit or discard the untracked or modified content in submodules)
        modified:   WareHouse/Gomoku_GitMode_20231025184031 (untracked content)
Changes not staged for commit:
某些阶段执行可能不会更改代码，因此不会提交。例如，软件的测试没有问题，也没有修改，因此测试阶段不会留下任何提交。