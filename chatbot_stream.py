import lmstudio as lms


model = lms.llm()
chat = lms.Chat("You are a task focused AI assistant")


while True:
    try:
        user_input = input("You (leave blank to exit): ")
    except EOFError:
        print()
        break
    if not user_input:
        break
    chat.add_user_message(user_input)
    prediction_stream = model.respond_stream(
        chat,
        on_message=chat.append,
    )
    print("Bot: ", flush=True)
    for fragment in prediction_stream:
        print(fragment.content, end="", flush=True)
    print()

    result = prediction_stream.result()
    print("Model used:", result.model_info.display_name)
    print("Predicted tokens:", result.stats.predicted_tokens_count)
    print("Time to first token (seconds):", result.stats.time_to_first_token_sec)
    print("Stop reason:", result.stats.stop_reason)

