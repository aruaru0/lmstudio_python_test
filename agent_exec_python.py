import lmstudio as lms
import json
import urllib.parse
import urllib.request
import io
import contextlib

def safe_exec_python(code: str) -> str:
    """
    Tool for executing Python code and returning the output.
    Use this tool whenever the user asks you to write, run, or test Python code.
    Do not simulate the result — always call this tool with actual code.
    """
    buffer = io.StringIO()
    local_vars = {}

    print("*"*80)
    print(f"exec Python Code")
    print(code)
    print("-"*80)

    try:
        with contextlib.redirect_stdout(buffer):
            exec(code, local_vars)
    except Exception as e:
        return f"Error: {e}"

    output = buffer.getvalue()

    print(output)
    print("*"*80)

    return output or "No output"


def print_fragment(fragment, round_index=0):
    # .act() supplies the round index as the second parameter
    # Setting a default value means the callback is also
    # compatible with .complete() and .respond().
    print(fragment.content, end="", flush=True)

model = lms.llm()
chat = lms.Chat("""
You are a task-focused assistant.
If the user asks you to write or execute Python code, use the tool `safe_exec_python`.
Never simulate code execution — always invoke the tool.
""")

while True:
    try:
        user_input = input("You (leave blank to exit): ")
    except EOFError:
        print()
        break
    if not user_input:
        break
    chat.add_user_message(user_input)
    print("Bot: ", end="", flush=True)
    model.act(
        chat,
        tools=[safe_exec_python],
        on_message=chat.append,
        on_prediction_fragment=print_fragment,
    )
    print()