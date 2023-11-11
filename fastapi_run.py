from fastapi import FastAPI, Form, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List
import shutil
from pathlib import Path
from pprint import pprint

import argparse
# 导入argparse模块
import logging
# 导入sys模块



# 导入logging模块
import os
 # 导入os模块
import sys
 # 导入ModelType模块 
root = os.path.dirname(__file__)
# 获取当前文件夹的路径
sys.path.append(root)
from dotenv import load_dotenv
load_dotenv() 
# # 设置环境变量



def get_config(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/

    Returns:
        path to three configuration jsons: [config_path, config_phase_path, config_role_path]
    """
    config_dir = os.path.join(root, "CompanyConfig", company)
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    config_paths = []

    for config_file in config_files:
        company_config_path = os.path.join(config_dir, config_file)
        default_config_path = os.path.join(default_config_dir, config_file)

        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        else:
            config_paths.append(default_config_path)

    return tuple(config_paths)
    


def en_zh(text, to_lang='zh'):
    """
    判断一个字符串是否包含中文
    """
    text_zh = False
    for cha in text:
        if u'\u4e00' <= cha <= u'\u9fff':
            text_zh = True
            break 
    if  to_lang == 'zh' and text_zh:
        return text
    elif to_lang == 'en' and not text_zh:
        return text
    else:
        if  text_zh == 'zh':
            text_to_lang = '英文'
        else:
            text_to_lang = '中文'
        from openai import OpenAI
        # print('OPENAI_API_KEY', os.environ['OPENAI_API_KEY'])
        client = OpenAI(
            organization=os.environ['OPENAI_ORG_ID'],
            api_key=os.environ['OPENAI_API_KEY']
        )
        res_text = client.chat.completions.create(model="gpt-3.5-turbo-1106",
                    messages=[
                        {"role": "system", "content": f"请将内容翻译成{text_to_lang}返回"},
                        {"role": "user", "content": text}
                    ])
        return res_text.choices[0].message.content
    



app = FastAPI()

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logging.error(f"Error occurred: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "An error occurred."},
    )
'''
ChatDev 启动参数

用法： run.py [-h] [-config config] [-org org] [-task task] [-name name] [-model model]

argparse可选参数：
-h, --help 显示此帮助消息并退出
--config CONFIG 配置config的名称，用于加载CompanyConfig/下的CompanyConfig.json；请参阅下面的CompanyConfig部分
--org ORG 组织名称，您的软件将在仓库生成 WareHouse/name_org_timestamp
--task TASK 提示你的想法
 --name NAME 软件的名称，您的软件将在WareHouse/name_org_timestamp中生成
 --model MODEL 选择模型GPT model，从｛'GPT_3_5_TURBO', 'GPT_4', 'GPT_4_32K'}中选择

'''
class PhaseItem(BaseModel):
    mobile: str = Field(..., example="13900011234", min_length=11, max_length=11, description="手机号")
    cfg_name: str = Field(..., example="Company", min_length=3, max_length=50, description="配置名称。用于加载CompanyConfig/下的CompanyConfig.json")
    org: str = Field(..., example="组织代号", min_length=3, max_length=50, description="组织名称。您的软件将在仓库生成 WareHouse/name_org_timestamp")
    task: str = Field(None, example="提示你的想法", min_length=5, max_length=100, description="提示你的想法")
    name: str = Field(None, example="软件的名称", min_length=5, max_length=15, description="软件的名称，您的软件将在WareHouse/name_org_timestamp中生成")
    model: str = Field(None, example="选择模型GPT模型", min_length=5, max_length=15, description="选择模型GPT模型，从｛'GPT_3_5_TURBO', 'GPT_4', 'GPT_4_32K'}")
    

class ChainItem(BaseModel):
    phase: str = Field(..., example="LanguageChoose", min_length=1, max_length=50, description="选择开发语言")
    phaseType: str = Field(..., example="SimplePhase", min_length=3, max_length=50, description="阶段类型")
    max_turn_step: int = Field(..., example=-1, min=-10, max=5, description="最大聊天回合数")
    need_reflect: bool = Field(None, example=False, description="是否需要反思。将开始顾问和CEO之间的聊天，以完善阶段聊天的结论。")
    cycleNum:  int = Field(..., example=2, min=-10, max=5, description="循环次数。在此 ComposedPhase 中执行 SimplePhase 的周期数")
    Composition: list = Field(..., example=[], description="组合")  # 可以有子元素： PhaseItem对象


class CompanyCfgParams(BaseModel):
    chain: List[ChainItem] = Field(..., example=[ChainItem(
        phase="LanguageChoose",
        phaseType="SimplePhase",
        max_turn_step=-1,
        cycleNum=2,
        Composition=[]
    )], description="参数序列")
    recruitments: List[str] = Field(..., example=["Company"], min_length=3, max_length=50, description="团队成员")
    clear_structure: bool = Field(..., example=False, description="是否清理缓存文件夹")
    brainstorming: bool = Field(..., example=False, description="是否进行头脑风暴")
    gui_design: bool = Field(..., example=False, description="是否为软件创建图形用户界面")
    git_management: bool = Field(..., example=False, description="是否在软件项目上打开 Git 管理")
    self_improve: bool = Field(..., example=False, description="用户输入提示的自我改进标志")
    brainstorming: bool = Field(..., example=False, description="是否进行头脑风暴")



class PhasePrompt(BaseModel):
    assistant_role_name: str = Field(..., example="Chief Product Officer")
    user_role_name: str = Field(..., example="Chief Executive Officer")
    phase_prompt: List[str] = Field(..., example=[
        "ChatDev has made products in the following form before:",
        "Image: can present information in line chart, bar chart, flow chart, cloud chart, Gantt chart, etc.",
        "Document: can present information via .docx files.",
        "PowerPoint: can present information via .pptx files.",
        "Excel: can present information via .xlsx files.",
        "PDF: can present information via .pdf files.",
        "Website: can present personal resume, tutorial, products, or ideas, via .html files.",
        "Application: can implement visualized game, software, tool, etc, via python.",
        "Dashboard: can display a panel visualizing real-time information.",
        "Mind Map: can represent ideas, with related concepts arranged around a core concept.",
        "As the {assistant_role}, to satisfy the new user's demand and the product should be realizable, you should keep discussing with me to decide which product modality do we want the product to be?",
        "Note that we must ONLY discuss the product modality and do not discuss anything else! Once we all have expressed our opinion(s) and agree with the results of the discussion unanimously, any of us must actively terminate the discussion by replying with only one line, which starts with a single word <INFO>, followed by our final product modality without any other words, e.g., \"<INFO> PowerPoint\"."
    ])

class PhaseCfgItem(BaseModel):
    phase_name: List[PhasePrompt] = Field(..., example=[PhasePrompt(
        assistant_role_name="Assistant Role",
        user_role_name="User Role",
        phase_prompt=["Prompt 1", "Prompt 2"]
    )], description="阶段名称")

class ProjectItem(BaseModel):
    mobile: str = Field(..., example="13903563281", min_length=11, max_length=11, description="手机号")
    task: str = Field(None, example="提示你的想法: 写一个五子棋程序", min_length=5, max_length=100, description="提示你的想法")
    name: str = Field(None, example="软件的名称(英文)： 创意五子棋", min_length=5, max_length=15, description="软件的名称，您的软件将在WareHouse/name_org_timestamp中生成")
    model: str = Field(None, example="选择模型GPT模型：['GPT_3_5_TURBO', 'GPT_4', 'GPT_4_32K']", min_length=5, max_length=15, description="选择模型GPT模型，从｛'GPT_3_5_TURBO', 'GPT_4', 'GPT_4_32K'}")
    path: str = Field(None, example="", min_length=0, max_length=50, description="您的文件目录，ChatDev将以增量模式在您的软件上构建")
    cfg_name: str = Field(..., example="Company", min_length=3, max_length=50, description="配置名称。用于加载CompanyConfig/下的CompanyConfig.json")
    org: str = Field(..., example="组织代号:org-secwae", min_length=3, max_length=50, description="组织名称。您的软件将在仓库生成 WareHouse/name_org_timestamp")

@app.post("/auto_run/")
async def autorun(project_item: ProjectItem):
    if '13903563281' != project_item.mobile:
        raise HTTPException(status_code=401, detail="Incorrect token")
    from camel.typing import ModelType
    from chatdev.chat_chain import ChatChain

    # Start ChatDev
    # ----------------------------------------
    #          Init ChatChain
    # ----------------------------------------
    project_item.task = en_zh(project_item.task, to_lang='en')
    # print(project_item)
    config_path, config_phase_path, config_role_path = get_config(project_item.cfg_name)
    args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO, 'GPT_4': ModelType.GPT_4, 'GPT_4_32K': ModelType.GPT_4_32k}
    chat_chain = ChatChain(config_path=config_path,
                            config_phase_path=config_phase_path,
                            config_role_path=config_role_path,
                            task_prompt=project_item.task,
                            project_name=project_item.name,
                            org_name=project_item.org,
                            model_type=args2type[project_item.model],
                            code_path=project_item.path)

    # 将当前文件夹的路径添加到sys.path中
    # ----------------------------------------
    #          Init Log
    # ----------------------------------------
    logging.basicConfig(filename=chat_chain.log_filepath, level=logging.INFO,
                    format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%Y-%d-%m %H:%M:%S', encoding="utf-8")
    
    # ----------------------------------------
    #          Pre Processing
    # ----------------------------------------
    chat_chain.pre_processing()

    # ----------------------------------------
    #          Personnel Recruitment
    # ----------------------------------------
    chat_chain.make_recruitment()

    # ----------------------------------------
    #          Chat Chain
    # ----------------------------------------
    chat_chain.execute_chain()

    # ----------------------------------------
    #          Post Processing
    # ----------------------------------------

    chat_chain.post_processing()


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    with Path("your_directory", file.filename).open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

# def main():
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

import uvicorn
from multiprocessing import Process

def run():
    uvicorn.run("fastapi_run:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    Process(target=run).start()