import lmstudio as lms
from rich.markdown import Markdown
from rich.console import Console

model = lms.llm()
chat = lms.Chat("You are a task focused AI assistant")

console = Console()

while True:
    console.print(Markdown("# You:"))
    try:
        user_input = input("You (leave blank to exit): ")
    except EOFError:
        print()
        break
    if not user_input:
        break
    chat.add_user_message(user_input)
    result = model.respond(chat)
    console.print(Markdown("# Bot: "))#, flush=True)
    console.print(Markdown(result.content))
    console.print()
    console.print("---")
    console.print("Model used:", result.model_info.display_name)
    console.print("Predicted tokens:", result.stats.predicted_tokens_count)
    console.print("Time to first token (seconds):", result.stats.time_to_first_token_sec)
    console.print("Stop reason:", result.stats.stop_reason)