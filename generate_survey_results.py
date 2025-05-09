import pandas as pd

# 创建示例数据
data = {
    "viva_usage": [3.5, 4.0, 3.8, 4.2, 3.7, 4.1, 3.9, 4.3, 3.6, 4.0],
    "performance_transparency": [4.2, 3.8, 4.0, 4.5, 3.9, 4.3, 4.1, 4.4, 3.7, 4.2],
    "digital_literacy": [3.8, 4.5, 4.0, 4.2, 3.6, 4.4, 3.9, 4.3, 3.5, 4.1],
    "work_engagement": [4.0, 4.2, 3.9, 4.5, 3.8, 4.3, 4.0, 4.6, 3.7, 4.1],
}

# 保存为 CSV 文件
df = pd.DataFrame(data)
df.to_csv("survey_results.csv", index=False)

print("survey_results.csv 文件已生成！")