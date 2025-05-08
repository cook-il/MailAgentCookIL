import os
from langchain.llms import LlamaCpp, OpenAI


def get_llm():
    """
    Returns an LLM instance, preferring local LlamaCpp if the model is available.
    Falls back to OpenAI if local loading fails or is disabled.
    """

    llama_model_path = os.getenv(
        "LLAMA_MODEL_PATH",
        "models/mistral-7b-instruct-v0.1.Q4_K_M.gguf"
    )
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Attempt to load local LlamaCpp model
    try:
        if os.path.exists(llama_model_path):
            print(f"[LLM_ENGINE] Loading local model: {llama_model_path}")
            return LlamaCpp(
                model_path=llama_model_path,
                temperature=0.5,
                max_tokens=512,
                n_ctx=2048,
                n_threads=6,
                verbose=False,
            )
        else:
            print(f"[LLM_ENGINE] Model file not found: {llama_model_path}")
            raise FileNotFoundError
    except Exception as e:
        print(f"[LLM_ENGINE WARNING] Failed to load local model: {e}")

    # Fallback to OpenAI if local model fails
    if openai_api_key:
        print("[LLM_ENGINE] Falling back to OpenAI API.")
        return OpenAI(
            temperature=0.5,
            openai_api_key=openai_api_key
        )
    else:
        raise RuntimeError("No local model found and OPENAI_API_KEY not set.")
