import pandas as pd

def create_salah_triple_tables():
    print("🚀 جاري إنشاء الجداول الثلاثة بناءً على أرقام الإكسيل الجديدة...")
    
    # 1. البيانات الإجمالية (نفس اللي في صورتك بالظبط)
    # ملاحظة: دي اللي بنطلع منها الإحصائيات العامة (253 هدف)
    total_stats = [
        {'Season': '2017-18', 'Matches': 49, 'Goals': 44, 'Assists': 16, 'Minutes': 3835},
        {'Season': '2018-19', 'Matches': 50, 'Goals': 27, 'Assists': 10, 'Minutes': 4313},
        {'Season': '2019-20', 'Matches': 42, 'Goals': 23, 'Assists': 32, 'Minutes': 3580},
        {'Season': '2020-21', 'Matches': 47, 'Goals': 31, 'Assists': 6,  'Minutes': 3844},
        {'Season': '2021-22', 'Matches': 48, 'Goals': 31, 'Assists': 15, 'Minutes': 3769},
        {'Season': '2022-23', 'Matches': 46, 'Goals': 30, 'Assists': 16, 'Minutes': 3914},
        {'Season': '2023-24', 'Matches': 41, 'Goals': 25, 'Assists': 15, 'Minutes': 2986},
        {'Season': '2024-25', 'Matches': 47, 'Goals': 34, 'Assists': 23, 'Minutes': 4090},
        {'Season': '2025-26*', 'Matches': 31, 'Goals': 8,  'Assists': 8,  'Minutes': 2447}
    ]

    # 2. تقسيم البيانات للدوري والأبطال (بناءً على النسب الحقيقية لأرقامك)
    # جدول الدوري الإنجليزي (Premier League)
    pl_data = [
        {'Season': '2017-18', 'Matches': 36, 'Goals': 32, 'Assists': 10, 'Minutes': 2905},
        {'Season': '2018-19', 'Matches': 38, 'Goals': 22, 'Assists': 8,  'Minutes': 3255},
        {'Season': '2019-20', 'Matches': 34, 'Goals': 19, 'Assists': 10, 'Minutes': 2876},
        {'Season': '2020-21', 'Matches': 37, 'Goals': 22, 'Assists': 5,  'Minutes': 3077},
        {'Season': '2021-22', 'Matches': 35, 'Goals': 23, 'Assists': 13, 'Minutes': 2761},
        {'Season': '2022-23', 'Matches': 38, 'Goals': 19, 'Assists': 12, 'Minutes': 3290},
        {'Season': '2023-24', 'Matches': 32, 'Goals': 18, 'Assists': 10, 'Minutes': 2536},
        {'Season': '2024-25', 'Matches': 38, 'Goals': 29, 'Assists': 18, 'Minutes': 3310},
        {'Season': '2025-26*', 'Matches': 22, 'Goals': 5,  'Assists': 6,  'Minutes': 1819}
    ]

    # جدول البطولات الأوروبية (CL / Europa)
    # الفرق بين الإجمالي والدوري
    cl_data = []
    for i in range(len(total_stats)):
        cl_entry = {
            'Season': total_stats[i]['Season'],
            'Matches': total_stats[i]['Matches'] - pl_data[i]['Matches'],
            'Goals': total_stats[i]['Goals'] - pl_data[i]['Goals'],
            'Assists': total_stats[i]['Assists'] - pl_data[i]['Assists'],
            'Minutes': total_stats[i]['Minutes'] - pl_data[i]['Minutes']
        }
        cl_data.append(cl_entry)

    def finalize_and_save(data_list, filename):
        df = pd.DataFrame(data_list)
        # حساب المعدلات تلقائياً بدقة
        df['Mins_Per_Goal'] = (df['Minutes'] / df['Goals']).replace([float('inf'), 0], 0).round(1)
        df['Mins_Per_Assist'] = (df['Minutes'] / df['Assists']).replace([float('inf'), 0], 0).round(1)
        df.to_csv(filename, index=False)
        return df

    # حفظ الملفات الثلاثة
    finalize_and_save(total_stats, 'salah_total_stats.csv')
    finalize_and_save(pl_data, 'salah_premier_league.csv')
    finalize_and_save(cl_data, 'salah_champions_league.csv')

    print("-" * 30)
    print("✅ تم إنشاء الملفات الثلاثة بنجاح!")
    print(f"📊 إجمالي الأهداف المحسوب: {sum(d['Goals'] for d in total_stats)}")
    print("-" * 30)

if __name__ == "__main__":
    create_salah_triple_tables()