#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df_1 = pd.read_csv("Electric_Vehicle_Population_Data.csv")


print(df_1.head())
print(df_1.info())

chinese_col = {
    "VIN (1-10)": "車輛識別號碼 (前 10 位)",
    "County": "縣",
    "City": "市",
    "State": "州",
    "Postal Code": "郵遞區號",
    "Model Year": "車型年份",
    "Make": "製造商",
    "Model": "車型",
    "Electric Vehicle Type": "電動車類型",
    "Clean Alternative Fuel Vehicle (CAFV) Eligibility": "清淨替代燃料車資格",
    "Electric Range": "電動續航里程",
    "Base MSRP": "基本建議零售價",
    "Legislative District": "立法區",
    "DOL Vehicle ID": "車輛識別號碼 (交通部)",
    "Vehicle Location": "車輛地點",
    "Electric Utility": "電力公司",
    "2020 Census Tract": "2020 年人口普查區"
}

# 把對應的欄位名稱，做替換
df_1.rename(columns = chinese_col, inplace=True)
# 更換欄位檢查
print(df_1.info())

# 州翻譯
state_translate = {
    "AL": "阿拉巴馬州",
    "AK": "阿拉斯加州",
    "AZ": "亞利桑那州",
    "AR": "阿肯色州",
    "CA": "加利福尼亞州",
    "CO": "科羅拉多州",
    "CT": "康乃狄克州",
    "DE": "德拉瓦州",
    "FL": "佛羅里達州",
    "GA": "喬治亞州",
    "HI": "夏威夷州",
    "ID": "愛達荷州",
    "IL": "伊利諾州",
    "IN": "印第安納州",
    "IA": "愛荷華州",
    "KS": "堪薩斯州",
    "KY": "肯塔基州",
    "LA": "路易斯安那州",
    "ME": "緬因州",
    "MD": "馬里蘭州",
    "MA": "麻薩諸塞州",
    "MI": "密西根州",
    "MN": "明尼蘇達州",
    "MS": "密西西比州",
    "MO": "密蘇里州",
    "MT": "蒙大拿州",
    "NE": "內布拉斯加州",
    "NV": "內華達州",
    "NH": "新罕布夏州",
    "NJ": "新澤西州",
    "NM": "新墨西哥州",
    "NY": "紐約州",
    "NC": "北卡羅來納州",
    "ND": "北達科他州",
    "OH": "俄亥俄州",
    "OK": "奧克拉荷馬州",
    "OR": "俄勒岡州",
    "PA": "賓夕法尼亞州",
    "RI": "羅得島州",
    "SC": "南卡羅來納州",
    "SD": "南達科他州",
    "TN": "田納西州",
    "TX": "德克薩斯州",
    "UT": "猶他州",
    "VT": "佛蒙特州",
    "VA": "維吉尼亞州",
    "WA": "華盛頓州",
    "WV": "西維吉尼亞州",
    "WI": "威斯康辛州",
    "WY": "懷俄明州",
    "DC": "華盛頓特區",
    "AE": "駐外美軍",
    "AP": "駐外美軍",
    "AA": "駐外美軍",
    "BC": "不列顛哥倫比亞省"  # 加拿大的省份，可能有跨境記錄
}

# 直接對 df_1 的 "州" 欄位進行替換
df_1["州"] = df_1["州"].replace(state_translate)

# 翻譯結果
print(df_1[["州"]])




# 只抓 1997 ~ 2023 的資料
df = df_1[(df_1["車型年份"] <= 2023)]
print(df)
#%% 更換內容
import pandas as pd

# print(type(df["電動車類型"]))
# print(df["電動車類型"].dtype)

df.loc[:, "電動車類型"] = df["電動車類型"].replace("Battery Electric Vehicle (BEV)", "電動車")
df.loc[:, "電動車類型"] = df["電動車類型"].replace("Plug-in Hybrid Electric Vehicle (PHEV)", "插電式油電車")

# 印出修改後的 DataFrame
print(df["電動車類型"])


#%%
# 查看缺失值
print(df.isnull().sum())
# 縣、市、郵遞區號、電力公司 和 2020 年人口普查區各有 4 筆缺失值，且都出現在相同的行中，這些無法填補缺失值進而刪掉。
cy_nan = df[df["縣"].isnull()]

# 車輛地點的缺失值在其他資料上很完整就不進行刪除，因不會使用車輛地點
vl_nan = df[df["車輛地點"].isnull()]

# 立法區的缺失值在其他資料上很完整就不進行刪除，因不會使用立法區
ld_nan = df[df["立法區"].isnull()] 

# 直接對缺失值做更改
# 不使用 inplace=True，將結果重新賦值給原始 DataFrame
df = df.dropna(subset=["縣", "市", "郵遞區號", "電力公司", "2020 年人口普查區"])

# "立法區", "車輛地點"
print(df.isnull().sum())
print("因「立法區」、「車輛地點」，其他資料完整，不會使用到這兩個欄位，所以不做變動。")
#%% 創建資料庫
# import MySQLdb

# # 建立資料庫連線（不指定資料庫）
# try:
#     conn = MySQLdb.connect(
#         host="127.0.0.1",
#         user="root",
#         password="rdfg3428",
#         port=3306,
#         charset="utf8"
#     )

#     # 使用 cursor() 方法操作資料庫
#     cursor = conn.cursor()

#     # 創建資料庫
#     cursor.execute("CREATE DATABASE IF NOT EXISTS work_test;")
#     print("資料庫創建成功或已存在")

#     cursor.close()
#     conn.close()

# except Exception as e:
#     print("資料庫創建失敗:", e)

#%% 創建資料表
# try:
#     conn = MySQLdb.connect(
#         host="127.0.0.1",
#         user="root",
#         password="rdfg3428",
#         database="work_test",
#         port=3306,
#         charset="utf8"
#     )

#     # 使用 cursor() 方法操作資料庫
#     cursor = conn.cursor()

#     # 創建資料表
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS project_test (
#             縣 VARCHAR(20),
#             市 VARCHAR(50),
#             州 VARCHAR(10),
#             車型年份 INT,
#             製造商 VARCHAR(20),
#             車型 VARCHAR(30),
#             電動車類型 VARCHAR(30)
#         );
#     """)
#     print("資料表創建成功或已存在")

#     cursor.close()
#     conn.close()

# except Exception as e:
#     print("資料表創建失敗:", e)
#%% (已寫入資料庫)
# 寫入 SQL
# import MySQLdb
# import pandas as pd


# # 建立資料庫連線
# try:
#     conn = MySQLdb.connect(
#         host="127.0.0.1",  # 主機名稱
#         user="root",        # 帳號
#         password="rdfg3428",  # 密碼
#         database="work_test",  # 資料庫名稱
#         port=3306,          # 端口
#         charset="utf8"     # 資料庫編碼
#     )

#     # 使用遊標操作資料庫
#     cursor = conn.cursor()

# # 將資料data寫入資料庫中
#     try:
#         for i in range(len(df)):

# # 直接新創一個資料庫跟資料表要給它限制 INT 跟 char
# # sql = """INSERT INTO 資料表名稱 (欄位名稱, site, people_total, area, population)VALUES (%s, %s, %s, %s, %s)
# # (縣,市, 州, 車型年份,製造商,車型,電動車類型)
#             sql = """INSERT INTO project_test 
#                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
#             var = (df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 5], df.iloc[i, 6], df.iloc[i, 7], df.iloc[i, 8])
#             cursor.execute(sql, var)

#         conn.commit()  # 提交資料
#         print("資料寫入完成")

#         cursor.close()
#         conn.close()

#     except Exception as e:
#         print("資料寫入錯誤:", e)

# except Exception as e:
#     print("資料庫連線發生錯誤:", e)

# finally:
#     print("資料庫連線結束")

#%% 拉資料
import MySQLdb
import pandas as pd

# ======================
# 資料庫連接取得 data
# ======================
try:
    # 開啟資料庫連接
    conn = MySQLdb.connect(host="127.0.0.1",     # 主機名稱
                            user="root",          # 帳號
                            password="rdfg3428",  # 密碼
                            database="work_test",      # 資料庫
                            port=3306,            # port
                            charset="utf8")       # 資料庫編碼
    
    # 使用 cursor() 方法操作資料庫
    cursor = conn.cursor()

    try:
        sql_query = "SELECT * FROM project_test ;"
        cursor.execute(sql_query)
        data = cursor.fetchall()
        
        # 獲取欄位名稱
        column_names = [i[0] for i in cursor.description]
        
        # 將查詢結果存入 DataFrame
        car_df = pd.DataFrame(data, columns = column_names)
        print(car_df)

        # 關閉 cursor 和連接
        cursor.close()
        conn.close()

    except Exception as e:
        print("錯誤訊息：", e)

except Exception as e:
    print("資料庫連接失敗：", e)

# SQL 抓資料出來放到 DataFrame 裡 命名 car_df

#%% 指選取車型
# import MySQLdb
# import pandas as pd

# # ======================
# # 資料庫連接取得 data
# # ======================
# try:
#     # 開啟資料庫連接
#     conn = MySQLdb.connect(host="127.0.0.1",     # 主機名稱
#                             user="root",          # 帳號
#                             password="rdfg3428",  # 密碼
#                             database="work",      # 資料庫
#                             port=3306,            # port
#                             charset="utf8")       # 資料庫編碼
    
#     # 使用 cursor() 方法操作資料庫
#     cursor = conn.cursor()

#     try:
#         # 使用 SELECT * 抓取所有欄位的前十筆資料
#         sql_query = "SELECT 車型 FROM project ;"
#         cursor.execute(sql_query)
#         data = cursor.fetchall()
        
#         # 獲取欄位名稱
#         column_names = ["車型"]
        
#         # 將查詢結果存入 DataFrame
#         style_df = pd.DataFrame(data, columns = column_names)
#         print(style_df)

#         # 關閉 cursor 和連接
#         cursor.close()
#         conn.close()

#     except Exception as e:
#         print("錯誤訊息：", e)

# except Exception as e:
#     print("資料庫連接失敗：", e)

#%% 題目範圍大到小
# 1. 電車跟油電車的銷售量 直方圖
# 2. 電動車 銷售量 插電式油電車 銷售量
# 3. 各品牌電動車的佔比 圓餅圖
# 4. 電車最大佔比的品牌逐年銷售量 直方圖
# 5. 各品牌插電式油電車的佔比 圓餅圖
# 6. 插電式油電車最大的佔比品牌逐年銷售量 直方圖
#%% 電車跟油電車的銷售量 直方圖
# 電車銷售量
# 計算每年電動車和插電式油電車的銷售量
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 篩選電動車和油電混合車數據
bev_df = car_df[car_df["電動車類型"] == "電動車"]
phev_df = car_df[car_df["電動車類型"] == "插電式油電車"]


# 計算1997到2012年(從頭到 2012)的電動車和油電混合車總銷量
# shape[0] 計算DataFrame row 的個數
# shape[1] 計算DataFrame column 的個數
# 把車型年份做計算每一行都是一台車 把2012 前的行做相加 就是2012 前的車子的數量
bev_1997to2012 = bev_df[(bev_df["車型年份"] <= 2012)].shape[0] # 小於等於 2012
phev_1997to2012 = phev_df[(phev_df["車型年份"] <= 2012)].shape[0]

# 計算2012年之後的銷售數量
# size 所有的數量 DataFrame 可以使用
# 使用 groupby 對車型年份進行分組
# size 方法計算每個分組中的元素數量，也就是每個年份中車型的數量。這樣你就可以知道每一年賣出了多少電動車或插電式油電車。
# 這個是以年份做分組把每一年的數量加總起來
bev_2013to2023 = bev_df[bev_df["車型年份"] > 2012].groupby("車型年份").size() # 大於 2012
phev_2013to2023 = phev_df[phev_df["車型年份"] > 2012].groupby("車型年份").size()

# shape[0]：計算資料列數
# size：計算所有元素總數
# groupby().size()：計算每個分組的元素數量


# 合併所有年份銷售數據
# 索引的欄位
years = ["1997~2012"] + list(bev_2013to2023.index) 
# 電動車 1997~2012 相加 因資料量太少，跟2013、2014....每年的合併畫一張圖
bev_sales = [bev_1997to2012] + list(bev_2013to2023)  
# 油電車 1997~2012 相加 因資料量太少，跟2013、2014....每年的合併畫一張圖
phev_sales = [phev_1997to2012] + list(phev_2013to2023) 

# 建立 DataFrame 方便繪圖
sales_df = pd.DataFrame({
    "插電式油電車": phev_sales, # 油電車的銷售
    "電動車": bev_sales # 電車的銷售
}, index = years) # 合併的索引值


# 畫圖 直方圖
# 設定中文
plt.rcParams["font.family"] = "Microsoft Yahei"
# 字型大小
plt.rcParams["font.size"] = 14

sales_df.plot(kind="bar", figsize=(12, 6), color=["#FF9933", "#3455b9"], width=0.75,edgecolor = "black")
# edgecolor = "black" 圖的邊框顏色

# 設定圖表標題和標籤
plt.title("1997 ~ 2023 年電動車與插電式油電車的銷售量", fontsize=20)
plt.xlabel("車型年份", fontsize=18)
plt.ylabel("銷售量", fontsize=18)

# rotation 角度
plt.xticks(rotation=30, fontsize=15)

# 手動設定圖例順序，使「電動車」在右側
# 是函數plt.gca().get_legend_handles_labels()
# plt.gca 函數是 matplotlib
# get_legend 抓資料
# handles 抓顏色
# labels 類別名稱
# 控制圖例透明度 framealpha 
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend([handles[1], handles[0]], ["電動車", "插電式油電車"], title="車型類型", fontsize=15,framealpha = 0.2)


# plt.tight_layout() 是 Matplotlib 函數，用來自動調整子圖參數，讓子圖不重疊，從而使整個圖表布局更加美觀和緊湊。
plt.tight_layout()
plt.savefig("專題圖/第一題每年電動車和插電式油電車的銷售量更改標題.png", transparent=True)
plt.show()

#%%
# 電動車 銷售量
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 篩選電動車和油電混合車數據
bev_df = car_df[car_df["電動車類型"] == "電動車"]
phev_df = car_df[car_df["電動車類型"] == "插電式油電車"]



bev_1997to2012 = bev_df[(bev_df["車型年份"] <= 2012)].shape[0] # 小於等於 2012
phev_1997to2012 = phev_df[(phev_df["車型年份"] <= 2012)].shape[0]


bev_2013to2023 = bev_df[bev_df["車型年份"] > 2012].groupby("車型年份").size() # 大於 2012
phev_2013to2023 = phev_df[phev_df["車型年份"] > 2012].groupby("車型年份").size()


# 合併所有年份銷售數據
# 索引的欄位
years = ["1997~2012"] + list(bev_2013to2023.index) 

bev_sales = [bev_1997to2012] + list(bev_2013to2023)  
bev_df = pd.DataFrame({# 油電車的銷售
    "電動車": bev_sales # 電車的銷售
}, index = years) # 合併的索引值

bev_df.plot(kind="bar", figsize=(12, 7), color=["#3455b9"], width=0.75,edgecolor = "black")
plt.legend(framealpha = 0.2)
# 設定圖表標題和標籤
plt.title("1997 ~ 2023 年電動車銷售量", fontsize=20)
plt.xlabel("車型年份", fontsize=18)
plt.ylabel("銷售量", fontsize=18)

# rotation 角度
plt.xticks(rotation=30, fontsize=15)
plt.savefig("專題圖/第一題每年電動車銷售量更改標題.png", transparent=True)
plt.show()


#%%
# 油電車 銷售量
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 篩選油電混合車數據
phev_df = car_df[car_df["電動車類型"] == "插電式油電車"]

phev_1997to2012 = phev_df[(phev_df["車型年份"] <= 2012)].shape[0]
phev_2013to2023 = phev_df[phev_df["車型年份"] > 2012].groupby("車型年份").size()

# 合併所有年份銷售數據
# 索引的欄位
years = ["1997~2012"] + list(phev_2013to2023.index) 

phev_sales = [phev_1997to2012] + list(phev_2013to2023)  
phev_df = pd.DataFrame({# 油電車的銷售
    "插電式油電車": phev_sales # 電車的銷售
}, index = years) # 合併的索引值

phev_df.plot(kind="bar", figsize=(12, 7), color=["#FF9933"], width=0.75,edgecolor = "black")
plt.legend(framealpha = 0.2)

# 設定圖表標題和標籤
plt.title("1997 ~ 2023 年插電式油電車銷售量", fontsize=20)
plt.xlabel("車型年份", fontsize=18)
plt.ylabel("銷售量", fontsize=18)

# rotation 角度
plt.xticks(rotation=30, fontsize=15)
plt.savefig("專題圖/第一題每年插電式油電車銷售量更改標題.png", transparent=True)
plt.show()

#%%# 2. 各品牌電車的銷售量 圓餅圖
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 設定中文
plt.rcParams["font.family"] = "Microsoft Yahei"
# 字型大小
plt.rcParams["font.size"] = 27

# 篩選電動車並按品牌分組計算銷售量
bev_df = car_df[car_df["電動車類型"] == "電動車"]
# 電動車製造商make計算
bev_make = bev_df["製造商"].value_counts(ascending = False)

# 取前五名品牌
top5_make = bev_make[:5] # 0 ~ 4
# 前五之後的合併再一起資料量太少
other_maketotal= bev_make[5:].sum() # 5 ~ 最後

# 新增一欄將其餘品牌合併為 "其他"
top5_make["其他"] = other_maketotal  

# color 顏色
colors = ["#3455b9","#4869cc","#6782d4","#869bdd","#b4c1ea","#e2e7f7"]

# 圓餅圖 (長 寬)
plt.figure(figsize=(18, 12))
plt.pie(
    top5_make,  # 圓餅圖顯示的數據。
    labels = top5_make.index,  # 顯示的標籤。
    autopct="%1.1f%%", # 顯示百分比。
    startangle= 95,  # 起始角度。
    pctdistance= 0.7,   # 百分比與圓心的距離，靠近圓餅內部
    labeldistance= 1.06, # 標籤與圓心的距離，超過1.0會在圓餅外圍
    colors = colors
)
# loc 圖例位置 ncol 調整圖利有幾行
plt.legend(title ="品牌",loc = (0.92,0.01),ncol =1,fontsize = 20,framealpha = 0.2) 

plt.title("各品牌電動車累積銷售量佔比 (資料截至2023年)",fontsize = 30)
plt.axis("equal")  # 確保圓餅圖示圓形 不會因為比例跑掉
plt.savefig("專題圖/第二題電動車並按品牌分組計算銷售量.png", transparent=True)
plt.show()

#%% 
# 從 2017 年對電動車有一個轉捩點特別從 2017 年開始看
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 3. 電車最大占比的品牌做逐年的銷售量 直方圖
# Tesla
# 抓出特斯拉
tesla_df = car_df[car_df["製造商"] == "TESLA"]
tesla_df["車型年份"] = tesla_df["車型年份"].astype(int)

# 設定中文
plt.rcParams["font.family"] = "Microsoft Yahei"
# 字型大小
plt.rcParams["font.size"] = 14

# 計算每年 TESLA 銷售量 (從 2017 年起)
Tesla_year_sales = tesla_df[tesla_df["車型年份"] >= 2017]["車型年份"].value_counts().sort_index()
print(Tesla_year_sales)

# 直方圖
# edgecolor = "black" 圖的邊框顏色
plt.figure(figsize=(12, 8))
plt.bar(Tesla_year_sales.index, Tesla_year_sales.values, color="#3455b9", width=0.75, label="Tesla 銷售量", edgecolor="black")

# 添加散點圖和連接線 要不要留待考慮
# plt.plot(Tesla_year_sales.index, Tesla_year_sales.values, color="red", marker="o", linestyle="--", linewidth=3, markersize=10)

plt.xlabel("年份", fontsize=20)
plt.ylabel("銷售量", fontsize=20)
plt.title("2017年~2023年 Tesla 電動車銷售量", fontsize=22)
plt.legend(framealpha=0.2)  # 顯示圖例  loc=(0.01, 0.94) # 調整圖例位置
plt.tight_layout()

# 保存圖表
plt.savefig("專題圖/第三題Tesla2017年後銷售量直方圖.png", transparent=True)
plt.show()

#%%
# 5. 各品牌油點車的占比 圓餅圖
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 設定中文
plt.rcParams["font.family"] = "Microsoft Yahei"
# 字型大小
plt.rcParams["font.size"] = 27

# 篩選插電式油電車並按品牌分組計算銷售量
phev_df = car_df[car_df["電動車類型"] == "插電式油電車"]
# 插電式油電車製造商make計算
phev_make = phev_df["製造商"].value_counts(ascending = False)

# 因為都很接近 取3%以上的
top8_phevmake = phev_make[:8] # 0 ~ 7

other_phevmaketotal= phev_make[8:].sum() # 8 ~ 最後

# 新增一欄將其餘品牌合併為 "其他"
top8_phevmake ["其他"] = other_phevmaketotal

# color 顏色
colors = ["#CC5500", "#FF6600", "#FF7F00", "#FF9933", "#FFB347", "#FFC069", "#FFD699", "#FFE5B4","#ffeed4"]


# 圓餅圖
plt.figure(figsize=(18, 12))
plt.pie(
    top8_phevmake,  # 圓餅圖顯示的數據。
    labels = top8_phevmake.index,  # 顯示的標籤。
    autopct="%1.1f%%", # 顯示百分比。
    startangle=90,  #起始角度。
    pctdistance=0.7,   # 百分比與圓心的距離，靠近圓餅內部
    labeldistance=1.07, # 標籤與圓心的距離，超過1.0會在圓餅外圍
    colors = colors
)
# loc 圖例位置 ncol 調整圖利有幾行 loc (橫,直)
# 慢慢調整
plt.legend(title ="品牌",loc = (0.92,0.01),ncol =1,fontsize = 20,framealpha = 0.2) 

plt.title("各品牌插電式油電車銷售量佔比 (資料截至2023年)",fontsize = 30)
plt.axis("equal")  
plt.savefig("專題圖/第五題插電式油電車並按品牌分組計算銷售量.png", transparent=True)
plt.show()

# 挑出比7%以上的品牌
#%%
# 6. 油電混和最大的占比品牌逐年銷售量 直方圖
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 設定中文
plt.rcParams["font.family"] = "Microsoft Yahei"
# 字型大小
plt.rcParams["font.size"] = 14

toyota_df = car_df[(car_df["製造商"] == "TOYOTA") & (car_df["電動車類型"] == "插電式油電車")]

# 將年份轉換為整數
toyota_df["車型年份"] = toyota_df["車型年份"].astype(int)


# 計算每年 TOYOTA 銷售量
toyota_year_sales = toyota_df[toyota_df["車型年份"] >= 2017]["車型年份"].value_counts().sort_index()
# 從這得知 toyota 從 2012 有資料
print(toyota_year_sales)

# edgecolor = "black" 圖的邊框顏色
plt.figure(figsize=(12, 8))
plt.bar(toyota_year_sales.index, toyota_year_sales.values, color="#FFB347",width = 0.7,label = "Toyota 銷售量",edgecolor = "black")

# 添加散點圖和連接線
# plt.plot(toyota_year_sales.index, toyota_year_sales.values, color="red", marker="o", linestyle="--", linewidth=3, markersize=10)

# 設置標題和軸標籤
plt.title("Toyota 插電式油電車逐年銷售量", fontsize = 22)
plt.xlabel("年份", fontsize= 20)
plt.ylabel("銷售量", fontsize= 20)

# 調整佈局
plt.tight_layout()
plt.legend(framealpha = 0.2, loc=(0.01, 0.93))  
plt.savefig("專題圖/第六題Toyota的銷售量.png", transparent=True)
plt.show()

#%% 電車跟油電車的銷售量 直方圖 錯誤沒 1997 ~ 2012 沒足夠的數量
# 電車銷售量
# 計算每年電動車和插電式油電車的銷售量
import matplotlib.pyplot as plt

# 計算每年純電動車和插電式油電混合車的銷售量
# 純電動車銷售量按年份分組
bev_df = car_df[car_df["電動車類型"] == "電動車"]
bev_yearly_sales = bev_df.groupby("車型年份").size()

# 插電式油電混合車銷售量按年份分組
phev_df = car_df[car_df["電動車類型"] == "插電式油電車"]
phev_yearly_sales = phev_df.groupby("車型年份").size()

# 合併銷售數據
sales_df = pd.DataFrame({
    "電動車": bev_yearly_sales,
    "插電式油電車": phev_yearly_sales
})

# 條形圖
sales_df.plot(kind="bar", figsize=(12, 6), color=["#3455b9", "#FFB347"])

# 設定圖表標題和標籤
plt.title("每年電動車與插電式油電混合車的銷售量")
plt.xlabel("車型年份")
plt.ylabel("銷售量")
plt.legend(title="車型類型",framealpha = 0.2)
plt.tight_layout()
plt.savefig("專題圖/第一題早期數據量少錯誤的圖.png", transparent=True)
plt.show()

#%% # 電動車錯誤圓餅圖
import matplotlib.pyplot as plt

# 篩選純電動車並按品牌分組計算銷售量
bev_df = car_df[car_df["電動車類型"] == "電動車"]
bev_sales_by_brand = bev_df["製造商"].value_counts()

# 圓餅圖
plt.figure(figsize=(8, 8))
plt.pie(bev_sales_by_brand, labels=bev_sales_by_brand.index, autopct='%1.1f%%', startangle=140)
plt.title("各品牌電動車銷售量佔比")
plt.axis("equal")   
plt.legend(title="品牌",framealpha = 0.2)
plt.savefig("專題圖/電動車錯誤圓餅圖.png", transparent=True)
plt.show()


#%% # 插電式油電車錯誤圓餅圖
import matplotlib.pyplot as plt

# 篩選純電動車並按品牌分組計算銷售量
bev_df = car_df[car_df["電動車類型"] == "插電式油電車"]
bev_sales_by_brand = bev_df["製造商"].value_counts()

# 圓餅圖
plt.figure(figsize=(8, 8))
plt.pie(bev_sales_by_brand, labels=bev_sales_by_brand.index, autopct='%1.1f%%', startangle=140)
plt.title("各品牌插電式油電車銷售量佔比")
plt.axis("equal")   
plt.legend(title="品牌",framealpha = 0.2)
plt.savefig("專題圖/插電式油電車錯誤圓餅圖.png", transparent=True)
plt.show()
#%%  # 自行預測(不準) 因素太多不適合
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # 準備數據
# years = toyota_year_sales.index.values.reshape(-1, 1)  # 年份 (X)
# sales = toyota_year_sales.values  # 銷量 (y)

# # 建立線性回歸模型
# model = LinearRegression()
# model.fit(years, sales)

# # 預測 2024 年銷量
# predicted_sales_2024 = model.predict([[2024]])
# toyota_year_sales.loc[2024] = int(predicted_sales_2024)

# # 直方圖
# plt.figure(figsize=(10, 6))
# plt.bar(toyota_year_sales.index, toyota_year_sales.values, color="green")

# # 設置標題和軸標籤
# plt.title("Toyota 插電式油電車逐年銷售量 (2017 - 2024)", fontsize=15)
# plt.xlabel("年份", fontsize=12)
# plt.ylabel("銷售量", fontsize=12)

# # 添加數據標籤
# for i, v in enumerate(toyota_year_sales.values):
#     plt.text(toyota_year_sales.index[i], v, f'{int(v)}', ha='center', va='bottom')

# # 調整佈局
# plt.tight_layout()
# plt.show()



