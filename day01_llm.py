import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
    api_key=os.getenv("DEEPSEEK_API_KEY")
)
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-flash")

def call_llm(prompt: str) -> str:
    response = client.responses.create(
        model=MODEL,
        input=prompt
    )
    return response.output_text

def main():
    print("Mini LLM CLI started. 输入 exit 退出。")

    while True:
        question = input("请输入您的问题 (输入 'exit' 退出): ").strip()

        if question.lower() in ('exit', "quit"):
            print("再见！")
            break

        elif not question:
            continue

        try:
            answer = call_llm(question)
            print("LLM:", answer)
        except Exception as e:
            print("调用失败：", e)

if __name__ == "__main__":
    main()
    print("yes")