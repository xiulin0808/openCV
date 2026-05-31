import pandas as pd

# 讀取資料
df = pd.read_csv("Dataset.csv")

# =========================
# 1. 檢視資料
# =========================
print("資料筆數：", len(df))
print("\n前五筆資料：")
print(df.head())

# =========================
# 2. 篩選 Catagory = A 開頭 + Supplier_Name = Member（如果沒有就跳過）
# =========================

# 注意：你的資料沒有 Member / Branch，所以這步改成示範 Catagory 篩選
filter_df = df[df["Catagory"].str.startswith("A", na=False)]

print("\nCatagory A開頭資料筆數：", len(filter_df))

# =========================
# 3. 各產品分類：總銷售額 & 平均庫存週轉率
# =========================

df["Total_Sales"] = df["Unit_Price"] * df["Sales_Volume"]

category_summary = (
    df.groupby("Catagory")
      .agg({
          "Total_Sales": "sum",
          "Inventory_Turnover_Rate": "mean"
      })
      .round(2)
)

print("\n各分類統計：")
print(category_summary)

# =========================
# 4. 找出總銷售額最高分類
# =========================

best_category = category_summary["Total_Sales"].idxmax()

print("\n最高銷售分類：", best_category)

# =========================
# 5. 輸出 CSV
# =========================

category_summary.to_csv("0520_pandas_3OK.csv", encoding="utf-8-sig")

print("\n已輸出 0520_pandas_3OK.csv")