from flask import Flask
from flask import render_template
from random import choices


app = Flask(__name__)


def random_fruit():
    fruits = ["apple", "pear", "orange"]
    return choices(fruits)


def random_task():
    tasks = ["eat", "clean", "learn"]
    return choices(tasks)


@app.route("/fruit")
def fruit():
    my_fruit = random_fruit()
    return render_template(
        "index.html", title="Random Fruit", category="Fruit", item=my_fruit
    )

@app.route("/task")
def task():
    my_task = random_task()
    return render_template(
        "index.html", title="Random Task", category="Task", item=my_task
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
