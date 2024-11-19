#!/usr/bin/env python
import sys
import warnings
from cache.crew import Cache

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Main file to run the crew locally
def run():
    """
    Run the crew.
    """
    try:
        result = Cache().crew().kickoff(inputs={"search_term": "Principais destinos turísticos da Bahia"})
        print(f"Resultado final da Crew: {result}")
    except Exception as e:
        print(f"Erro ao executar a Crew: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Cache().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Cache().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Cache().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
