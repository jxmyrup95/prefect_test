from prefect import flow, get_run_logger, task
import numpy as np

from prefect.events import emit_event

# def some_function(name: str="kiki") -> None:
#     print(f"hi {name}!")
#     emit_event(event=f"{name}.sent.event!", resource={"prefect.resource.id": f"coder.{name}"})

# some_function()

@flow(name="Prefect Cloud Quickstart Jesper3", retries=4, retry_delay_seconds=2)
def quickstart_flow(name: str="_HEJ_HEJ"):
    logger = get_run_logger()
    logger.warning("Local quickstart flow is running!")
    random_int = np.random.randint(2)
    # if random_int:
    #     logger.error("0/0")
    #     0/0
    # some_function()
    string = more_logging1()
    string = string + name
    more_logging2(string)


@task
def more_logging1():
    return "Hello"


@task
def more_logging2(string: str):
    logger = get_run_logger()
    logger.info(string)


if __name__ == "__main__":
    # string = quickstart_flow()
    string = quickstart_flow.serve(name="Testing7", cron="3 * * * *")
