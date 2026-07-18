from ai.client import CampusAI

ai = CampusAI()

print("=" * 30)
print("      CampusAI v0.6")
print("=" * 30)
print("終了するには /exit と入力してください。")
print("コマンド一覧は /help で確認できます。\n")

while True:
    user_input = input("You > ")

    if user_input == "/exit":
        print("CampusAI > またお会いしましょう！")
        break

    elif user_input == "/help":
        print("""
====================
Commands
====================
/help   コマンド一覧を表示
/clear  会話履歴を削除
/exit   CampusAIを終了
""")
        continue

    elif user_input == "/clear":
        ai.clear_history()
        print("CampusAI > 会話履歴を削除しました。\n")
        continue

    answer = ai.ask(user_input)

    print(f"\nCampusAI > {answer}\n")