"""
wa-os Usage Example: Daily Harmony Check
日常の選択が「世界平和（調和）」にどう繋がるかの実例
"""

from protocols.bio_adaptation import HumanSystem

def run_example():
    # 1. システムの起動
    my_os = HumanSystem(user_name="Hiroko")
    print(f"--- {my_os.user_name}'s wa-os Standard Check ---")

    # 2. 昨日のような「調和した食事と交流」のシミュレーション
    # 化学調味料なし、地元の旬の食材、平和への意志
    daily_event = {
        "event_name": "International Investor Meeting & Dinner",
        "artificial_additives": False,  # 化学調味料なしの実践
        "is_local_season": True,        # 土地との調和
        "intent": "World Peace"         # 世界平和への意図
    }

    # 3. 調和スコアの計算
    score = my_os.evaluate_input(daily_event)
    
    print(f"Event: {daily_event['event_name']}")
    print(f"Resulting Harmony Score: {score}")

    if score > 0.8:
        print("Status: High Resonance. Your actions are aligning with the Worldline.")
    else:
        print("Status: Tuning required. Check your input/environment balance.")

if __name__ == "__main__":
    run_example()
