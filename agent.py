import math
import lmstudio as lms
from rich.markdown import Markdown
from rich.console import Console
import re

def remove_think_tags(text):
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)


def add(a: int, b: int) -> int:
    """Given two numbers a and b, returns the sum of them."""
    print("*"*80)
    print(f"call add({a}, {b})")
    print("*"*80)
    return a + b

def is_prime(n: int) -> bool:
    """Given a number n, returns True if n is a prime number."""
    print("*"*80)
    print(f"call is_prime({n})")
    print("*"*80)
    if n < 2:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt):
        if n % i == 0:
            return False
    return True

def print_message(message) :
    global console
    if message.role == "assistant" :
        for e in message.content :
            if e.type == "text" :
                console.print(Markdown(remove_think_tags(e.text)))                

console = Console()

# model = lms.llm("qwen3-4b")
model = lms.llm("qwen3-30b-a3b-mlx")
model.act(
  "Is the result of 12345 + 45668 a prime? Think step by step.",
  [add, is_prime],
  on_message=print_message,
)