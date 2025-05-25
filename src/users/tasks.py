from config.settings_celery import app


@app.task(queue="default")
def example_task() -> str:
    """
    An example Celery task that can be scheduled or called asynchronously.
    """
    print("This is an example task running asynchronously.")
    return "Task completed successfully."
