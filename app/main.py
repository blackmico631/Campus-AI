from ai.client import CampusAI
from documents.rag import RAG
from documents.subject_manager import SubjectManager


ai = CampusAI()
manager = SubjectManager()
rag = None

print("=" * 40)
print("           CampusAI v0.10")
print("=" * 40)
print("コマンド一覧は /help で確認できます。\n")


while True:
    user_input = input("You > ").strip()

    # 終了
    if user_input == "/exit":
        print("CampusAI > またお会いしましょう！")
        break

    # ヘルプ
    elif user_input == "/help":
        print("""
====================
Commands
====================
/help               コマンド一覧を表示
/subjects           利用可能な科目を表示
/subject <科目名>   科目を選択
/clear              会話履歴を削除
/exit               CampusAIを終了
""")
        continue

    # 科目一覧
    elif user_input == "/subjects":
        subjects = manager.get_subjects()

        if not subjects:
            print("CampusAI > 利用可能な科目がありません。\n")
        else:
            print("\n利用可能な科目:")
            for subject in subjects:
                print(f"- {subject}")
            print()

        continue

    # 科目選択
    elif user_input.startswith("/subject "):
        subject = user_input.split(maxsplit=1)[1]

        if manager.select_subject(subject):
            index_files = manager.get_index_files()

            if index_files:
                rag = RAG(index_files)
                ai.clear_history()

                print(
                    f"CampusAI > 科目を「{subject}」に変更しました。"
                )
                print(
                    f"CampusAI > {len(index_files)}個の資料インデックスを使用します。\n"
                )
            else:
                rag = None
                print(
                    f"CampusAI > 「{subject}」には"
                    "インデックスがありません。\n"
                )

        else:
            print(
                f"CampusAI > 「{subject}」という科目は"
                "見つかりませんでした。\n"
            )

        continue

    # 会話履歴リセット
    elif user_input == "/clear":
        ai.clear_history()
        print("CampusAI > 会話履歴を削除しました。\n")
        continue

    # 科目未選択
    if rag is None:
        print(
            "CampusAI > 先に科目を選択してください。"
            "「/subjects」で一覧を確認できます。\n"
        )
        continue

    # RAG検索
    context = rag.retrieve(user_input)

    # 資料を使って回答
    answer = ai.ask_with_context(
        question=user_input,
        context=context
    )

    print(f"\nCampusAI > {answer}\n")