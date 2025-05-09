import pandas as pd
import numpy as np

# 原始样本数据
original_data = {
    'viva_usage': [3.5, 4.2, 3.8, 4.0, 3.9, 4.1, 3.7, 4.3, 3.6, 4.0],
    'performance_transparency': [4.0, 3.8, 4.2, 4.1, 3.9, 4.3, 4.0, 3.7, 4.1, 3.8],
    'digital_literacy': [3.8, 4.0, 3.9, 4.1, 3.7, 4.2, 3.6, 4.0, 3.8, 4.1],
    'work_engagement': [4.2, 4.5, 4.3, 4.4, 4.1, 4.6, 4.0, 4.7, 4.2, 4.3]
}

# 转换为 DataFrame
df = pd.DataFrame(original_data)

# 生成额外的 10 个样本
np.random.seed(42)  # 固定随机种子以确保结果可重复
additional_data = {
    'viva_usage': np.random.uniform(3.5, 4.5, 10),
    'performance_transparency': np.random.uniform(3.5, 4.5, 10),
    'digital_literacy': np.random.uniform(3.5, 4.5, 10),
    'work_engagement': np.random.uniform(4.0, 4.7, 10)
}

# 转换为 DataFrame
additional_df = pd.DataFrame(additional_data)

# 合并原始数据和新增数据
combined_df = pd.concat([df, additional_df], ignore_index=True)

# 保存为 CSV 文件
combined_df.to_csv('survey_results.csv', index=False)

print("虚拟数据已生成并保存为 'survey_results.csv'")