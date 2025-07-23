# 1.1.4 用户行为数据分析 - 题目解答

## 题目概述
本题目主要考察Python数据分析的基本技能，包括数据采集、数据清洗与预处理、数据统计等核心知识点。

## 完整代码答案

### 1. 数据采集

```python
import pandas
import numpy as np
import matplotlib.pyplot as plt

# 1. 数据采集
# 从本地文件中读取数据  2分
# data =  _______________________________  # 原题目空行
data = pandas.read_csv('user_behavior_data.csv')  # 答案：用pandas读取csv文件
print("数据采集完成，已加载到DataFrame中")

# 打印数据的前5条记录  2分
# print(________________________________)  # 原题目空行
print(data.head())  # 答案：用head()查看前5条数据
```

**讲解：**
- `pandas.read_csv('user_behavior_data.csv')`：使用pandas库读取本地的CSV文件，返回一个DataFrame对象，这是数据分析的基础数据结构
- `data.head()`：显示DataFrame的前5行数据，帮助快速了解数据结构和内容，是数据探索的常用方法

### 2. 数据清洗与预处理

```python
# 2. 数据清洗与预处理
# 处理缺失值（删除）  2分
# data = ________________________________  # 原题目空行
data = data.dropna()  # 答案：删除所有含有缺失值的行

# 数据类型转换
# data________________ = ________________(int)   # Age数据类型转换为int 2分
data['Age'] = data['Age'].astype(int)  # 答案：将Age列转换为int类型
# data________________ = ________________(float) # PurchaseAmount数据类型转换为float  2分
data['PurchaseAmount'] = data['PurchaseAmount'].astype(float)  # 答案：将PurchaseAmount列转换为float类型
# data________________ = ________________(int)   # ReviewScore数据类型转换为int 2分
data['ReviewScore'] = data['ReviewScore'].astype(int)  # 答案：将ReviewScore列转换为int类型

# 处理异常值  2分
# data = data[(________________.________________(18, 70)) & 
#             (data['PurchaseAmount'] > 0) & 
#             (________________.________________(1, 5))]  # 原题目空行
data = data[(data['Age'].between(18, 70)) & 
            (data['PurchaseAmount'] > 0) & 
            (data['ReviewScore'].between(1, 5))]  # 答案：筛选合理范围的数据

# 数据标准化
# data['PurchaseAmount'] = (data['PurchaseAmount'] - ________________) / ________________  # PurchaseAmount数据标准化 2分
data['PurchaseAmount'] = (data['PurchaseAmount'] - data['PurchaseAmount'].mean()) / data['PurchaseAmount'].std()  # 答案：标准化
# data['ReviewScore'] = (data['ReviewScore'] - ________________) / ________________        # ReviewScore数据标准化 2分
data['ReviewScore'] = (data['ReviewScore'] - data['ReviewScore'].mean()) / data['ReviewScore'].std()  # 答案：标准化

# 保存清洗后的数据  1分
# ________________('cleaned_user_behavior_data.csv', index=False)  # 原题目空行
data.to_csv('cleaned_user_behavior_data.csv', index=False)  # 答案：保存为csv
print("数据清洗完成，已保存为 'cleaned_user_behavior_data.csv'")
```

**讲解：**

1. **缺失值处理**：
   - `data.dropna()`：删除所有包含缺失值的行，确保数据完整性

2. **数据类型转换**：
   - `astype(int/float)`：将数据转换为合适的数值类型，便于后续计算
   - Age转为int：年龄应该是整数
   - PurchaseAmount转为float：购买金额需要保留小数
   - ReviewScore转为int：评分通常是整数

3. **异常值处理**：
   - `between(a, b)`：筛选在指定区间内的数据
   - 年龄限制在18-70岁：合理的年龄范围
   - 购买金额大于0：排除无效数据
   - 评分在1-5分：合理的评分范围

4. **数据标准化**：
   - 公式：(x - 均值) / 标准差
   - 使数据均值为0，标准差为1
   - 便于不同量纲数据的比较和建模

5. **数据保存**：
   - `to_csv()`：将处理后的数据保存为CSV文件
   - `index=False`：不保存行索引

### 3. 数据统计

```python
# 3. 数据统计
# 统计每个购买类别的用户数 2分
# purchase_category_counts = ________________.________________  # 原题目空行
purchase_category_counts = data['PurchaseCategory'].value_counts()  # 答案：统计每个类别数量
print("每个购买类别的用户数:\n", purchase_category_counts)

# 统计不同性别的平均购买金额 2分
# gender_purchase_amount_mean = ________________(________________)['PurchaseAmount'].mean()  # 原题目空行
gender_purchase_amount_mean = data.groupby('Gender')['PurchaseAmount'].mean()  # 答案：按性别分组求均值
print("不同性别的平均购买金额:\n", gender_purchase_amount_mean)

# 统计不同年龄段的用户数 2分
bins = [18, 26, 36, 46, 56, 66, np.inf]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
# data['AgeGroup'] = pandas.________________(________________, right=False)  # 原题目空行
data['AgeGroup'] = pandas.cut(data['Age'], bins=bins, labels=labels, right=False)  # 答案：分年龄段
age_group_counts = data['AgeGroup'].value_counts().sort_index()
print("不同年龄段的用户数:\n", age_group_counts)
```

**讲解：**

1. **类别统计**：
   - `value_counts()`：统计分类变量中每个类别的频数
   - 常用于了解数据分布情况

2. **分组统计**：
   - `groupby('Gender')`：按性别分组
   - `['PurchaseAmount'].mean()`：计算每组的平均购买金额
   - 用于比较不同群体的特征差异

3. **年龄段分析**：
   - `pandas.cut()`：将连续变量（年龄）分割为离散区间
   - `bins`：定义分割点
   - `labels`：定义区间标签
   - `right=False`：左闭右开区间
   - `sort_index()`：按区间顺序排序

## 知识点总结

### 核心技能
1. **数据读取**：pandas.read_csv()
2. **数据查看**：head(), info(), describe()
3. **数据清洗**：dropna(), astype(), between()
4. **数据转换**：标准化处理
5. **数据统计**：value_counts(), groupby(), cut()

### 考试要点
- 总分：25分
- 数据采集：4分
- 数据清洗：15分
- 数据统计：6分

### 常见错误
1. 忘记导入必要的库
2. 数据类型转换错误
3. 异常值处理范围不合理
4. 标准化公式写错
5. 分组统计语法错误

## 用户提问与回答总结

**用户问题**：请讲解题目中的每个小题，解释为什么这样编写代码

**回答要点**：
1. 详细解释了每个代码块的作用和原理
2. 说明了为什么选择特定的函数和方法
3. 强调了数据清洗的重要性
4. 解释了标准化的意义
5. 说明了分组统计的应用场景

**用户反馈**：要求将解释和问答总结写入answer.md文件

**处理方式**：创建了完整的答案文档，包含代码、讲解和知识点总结