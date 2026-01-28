import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)

# プロンプトの読み込み
with open("prompt4.txt", "r", encoding="utf-8") as f:
    base_prompt = f.read()

def chat():
    messages = [{"role": "system", "content": base_prompt}]

    print("対話を開始します。終了したいときは 'exit' と入力してください。")

    first_reply = "システム: こんにちは。初めまして！本日はよろしくお願いします！"
    print(first_reply)
    messages.append({"role": "assistant", "content": "何か悩みはありますか？良ければ私に聞かせてくれませんか？"})

    while True:
        user_input = input("ユーザー: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})


        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.5
        )

        reply = response.choices[0].message.content
        print("システム:", reply)

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    chat()
