# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 在此代码库中工作时提供指导。

## 项目概述

这是人工智能训练师三级认证考试的题目集合。代码库包含按编号文件夹组织的独立考试题目，每个文件夹代表特定的主题和技能评估。

## 代码库结构

代码库按考试题目类别组织：

- **1.1.x**: 使用pandas/numpy进行数据分析基础，包含CSV数据集
- **1.2.x**: 文档和理论题目（仅Word文档）
- **2.1.x & 2.2.x**: 机器学习任务，包括数据预处理、模型训练和评估
- **3.1.x**: 物联网/智能设备数据分析，使用Excel数据集
- **3.2.x**: 深度学习和ONNX模型推理任务
- **4.1.x & 4.2.x**: 高级理论和文档题目

每个编号文件夹包含：
- `.ipynb` 文件：带有填空编程练习的Jupyter笔记本
- 数据文件：用于练习的CSV、Excel或其他数据集
- 模型文件：用于深度学习任务的ONNX模型（3.2.x系列）
- 文档：包含题目和要求的Word文档

## 开发环境

此项目设计在WSL环境中运行，配合Windows宿主机设置：

### Jupyter Notebook 设置
如果使用Windows miniconda/anaconda，从WSL访问：
```bash
# 将Windows conda添加到PATH
export PATH="/mnt/c/Users/[用户名]/miniconda3/Scripts:$PATH"

# 安装所需包
conda install jupyter notebook pandas numpy matplotlib scikit-learn pillow onnxruntime

# 从项目目录启动Jupyter
jupyter notebook --allow-root --ip=0.0.0.0
```

### 所需Python库
- **数据分析**: pandas, numpy, matplotlib, seaborn
- **机器学习**: scikit-learn
- **深度学习**: onnxruntime, pillow
- **工具库**: scipy

## 考试题目类型

### 1.1.x - 数据分析基础
- 患者/传感器/信贷数据分析
- 统计计算和风险评估
- 数据分类和分组操作
- pandas操作填空题

### 2.1.x & 2.2.x - 机器学习
- 数据预处理和清洗
- 特征工程和标准化
- 训练/测试集划分
- 模型评估和分析
- 典型流程：加载数据 → 清洗 → 预处理 → 划分 → 保存

### 3.2.x - 深度学习/ONNX
- ONNX模型加载和推理
- 图像预处理和分类
- 目标检测工作流
- 计算机视觉工具（用于目标检测的box_utils_numpy.py）

## 处理考试题目

每个考试题目在其文件夹内都是独立的。在帮助解决具体题目时：

1. 阅读 `.ipynb` 文件了解要求
2. 检查提供的数据集了解数据结构
3. 用适当的pandas/sklearn/onnx代码完成填空部分
4. 确保输出与打印语句中显示的预期格式匹配

## 关键文件

- `vision/utils/box_utils_numpy.py`: 目标检测任务的工具函数（边界框操作、NMS、坐标转换）
- 各种数据集：每个题目文件夹包含特定领域的实践数据

## 评估重点

练习测试以下实践技能：
- 使用pandas进行数据操作和分析
- 基础机器学习工作流程
- 计算机视觉和深度学习推理
- 统计分析和数据解释