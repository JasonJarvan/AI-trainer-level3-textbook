# 1.1.3 数据审核与清洗 - 题目解析与答案总结

## 题目概述
本题目是关于信用数据的完整性审核、合理性审核和数据清洗的综合练习。通过pandas和numpy库对credit_data.csv数据集进行处理，包括缺失值检测、重复值检测、数据合理性验证以及异常值处理。

## 题目分解与答案

### Cell 0: 环境准备
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 读取数据集
data = pd.read_csv('credit_data.csv')
```

**解释：**
- 导入必要的数据处理库：pandas用于数据处理，numpy用于数值计算，matplotlib用于可视化
- 读取信用数据集文件

### Cell 1: 数据完整性审核 (4分)

**原题目：**
```python
# 1. 数据完整性审核
missing_values = data._________       #数据缺失值统计 2分
duplicate_values = data._________     #数据重复值统计 2分
```

**答案：**
```python
# 1. 数据完整性审核
missing_values = data.isnull().sum()       #数据缺失值统计 2分
duplicate_values = data.duplicated().sum() #数据重复值统计 2分
```

**详细解释：**
1. **缺失值统计 (2分)**：
   - `data.isnull().sum()` 
   - `isnull()` 方法检查每个单元格是否为缺失值（NaN），返回布尔矩阵
   - `sum()` 方法按列统计True的数量，即缺失值数量
   - 结果：Age列有1个缺失值，Income列有1个缺失值

2. **重复值统计 (2分)**：
   - `data.duplicated().sum()`
   - `duplicated()` 方法检查重复行，返回布尔序列
   - `sum()` 统计重复行的数量
   - 结果：数据集中没有重复行（0个重复值）

### Cell 2: 数据合理性审核 (8分)

**原题目：**
```python
# 2. 数据合理性审核
data['is_age_valid'] = _________._________(18, 70)              #Age数据的合理性审核 2分
data['is_income_valid'] = _________ > _________                 #Income数据的合理性审核 2分
data['is_loan_amount_valid'] = _________ < (_________ * 5)      #LoanAmount数据的合理性审核 2分
data['is_credit_score_valid'] = _________._________(300, 850)   #CreditScore数据的合理性审核 2分
```

**答案：**
```python
# 2. 数据合理性审核
data['is_age_valid'] = data['Age'].between(18, 70)              #Age数据的合理性审核 2分
data['is_income_valid'] = data['Income'] > 0                    #Income数据的合理性审核 2分
data['is_loan_amount_valid'] = data['LoanAmount'] < (data['Income'] * 5)      #LoanAmount数据的合理性审核 2分
data['is_credit_score_valid'] = data['CreditScore'].between(300, 850)   #CreditScore数据的合理性审核 2分
```

**详细解释：**
1. **年龄合理性审核 (2分)**：
   - `data['Age'].between(18, 70)`
   - 检查年龄是否在18-70岁之间（包含边界值）
   - 返回布尔序列，True表示合理，False表示不合理

2. **收入合理性审核 (2分)**：
   - `data['Income'] > 0`
   - 检查收入是否大于0（收入不能为负数或零）
   - 返回布尔序列

3. **贷款金额合理性审核 (2分)**：
   - `data['LoanAmount'] < (data['Income'] * 5)`
   - 检查贷款金额是否小于收入的5倍
   - 这是一个业务规则：贷款金额不应超过年收入的5倍

4. **信用分数合理性审核 (2分)**：
   - `data['CreditScore'].between(300, 850)`
   - 检查信用分数是否在300-850之间
   - 这是常见的信用分数范围

**合理性检查结果分析：**
- 年龄合理性：999个有效，1个无效
- 收入合理性：999个有效，1个无效  
- 贷款金额合理性：796个有效，204个无效
- 信用分数合理性：1000个全部有效
- 总体合理性：795个记录全部合理，205个记录存在至少一个不合理项

### Cell 3: 数据清洗和异常值处理 (2分)

**原题目：**
```python
# 3. 数据清洗和异常值处理
# 标记不合理数据
invalid_rows = data[~data['is_valid']]
# 删除不合理数据行
cleaned_data = data[data['is_valid']]
# 删除标记列
cleaned_data = cleaned_data.drop(columns=['is_age_valid', 'is_income_valid', 'is_loan_amount_valid', 'is_credit_score_valid', 'is_valid'])
# 保存清洗后的数据
_________._________(_________, index=False)
```

**答案：**
```python
# 3. 数据清洗和异常值处理
# 标记不合理数据
invalid_rows = data[~data['is_valid']]
# 删除不合理数据行
cleaned_data = data[data['is_valid']]
# 删除标记列
cleaned_data = cleaned_data.drop(columns=['is_age_valid', 'is_income_valid', 'is_loan_amount_valid', 'is_credit_score_valid', 'is_valid'])
# 保存清洗后的数据
cleaned_data.to_csv('cleaned_credit_data.csv', index=False)
```

**详细解释：**
1. **标记不合理数据**：
   - `invalid_rows = data[~data['is_valid']]`
   - 使用布尔索引选出所有不合理的数据行
   - `~` 操作符对布尔值取反

2. **删除不合理数据行**：
   - `cleaned_data = data[data['is_valid']]`
   - 只保留所有合理性检查都通过的数据行

3. **删除标记列**：
   - `drop(columns=[...])` 删除用于标记合理性的辅助列
   - 保持原始数据的清洁性

4. **保存清洗后的数据 (2分)**：
   - `cleaned_data.to_csv('cleaned_credit_data.csv', index=False)`
   - 将清洗后的数据保存为新的CSV文件
   - `index=False` 不保存行索引

## 用户提问与回答总结

**用户提问：** "@/1.1.3" - 请求解释1.1.3题目的每个小题

**回答要点：**
1. 详细解释了每个Cell的功能和目的
2. 补全了所有空行的代码
3. 解释了每个pandas方法的作用和原理
4. 分析了数据合理性检查的结果
5. 说明了数据清洗的完整流程

**关键知识点：**
- pandas的`isnull()`、`duplicated()`、`between()`方法
- 布尔索引的使用
- 数据合理性审核的业务逻辑
- 数据清洗的标准流程
- CSV文件的读写操作

## 最终结果
- 原始数据：1000条记录
- 清洗后数据：795条记录（删除了205条不合理记录）
- 输出文件：cleaned_credit_data.csv