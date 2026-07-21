from ai.client import CampusAI
from documents.rag import RAG
from documents.subject_manager import SubjectManager
from documents.document_manager import DocumentManager


ai = CampusAI()
manager = SubjectManager()
document_manager = DocumentManager()

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
        /help                     コマンド一覧を表示
        /subjects                 利用可能な科目を表示
        /subject <科目名>         科目を選択
        /add <科目名> <PDF名>     PDFを1件登録
        /index <科目名>           未登録PDFを一括登録
        /clear                    会話履歴を削除
        /exit                     CampusAIを終了
        """)
        continue

    # 資料登録
    elif user_input.startswith("/add "):
        parts = user_input.split(maxsplit=2)

        if len(parts) != 3:
            print(
                "CampusAI > "
                "使い方: /add <科目名> <PDF名>\n"
            )
            continue

        subject = parts[1]
        filename = parts[2]

        print("CampusAI > 資料を登録しています...")

        result = document_manager.add_document(
            subject=subject,
            filename=filename
        )

        print(f"CampusAI > {result}\n")

        if manager.current_subject == subject:
            index_files = manager.get_index_files()

            if index_files:
                rag = RAG(index_files)

        continue
        
    elif user_input.startswith("/index "):
        print("DEBUG: /index が呼ばれました")
        parts = user_input.split(maxsplit=1)
        
        if len(parts) != 2:
            print(
                "CampusAI > "
                "使い方: /index <科目名>\n"
                )
            continue
        
        subject = parts[1]

        print(
            f"CampusAI > 「{subject}」の"
        "未登録資料を確認しています...\n"
        )
        
        registered_files = (
            document_manager.index_new_documents(subject)
        )
        
        if registered_files:
            print(
                f"\nCampusAI > {len(registered_files)}件の"
                "新しい資料を登録しました。"
            )
            for filename in registered_files:
                print(f"- {filename}")
                
            print()
            
        else:
            print(
                "CampusAI > 新しく登録する資料は"
                "ありませんでした。\n"
            )
            
        # 現在選択している科目ならRAGを更新
        if manager.current_subject == subject:
            index_files = manager.get_index_files()
            
            if index_files:
                rag = RAG(index_files)
            
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