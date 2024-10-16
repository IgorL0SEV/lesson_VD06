from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Хранилище для данных анкеты
user_data = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем данные из формы
        name = request.form.get("name")
        city = request.form.get("city")
        hobby = request.form.get("hobby")
        age = request.form.get("age")

        # Добавляем новые данные в список
        user_data.insert(0, {
            "name": name,
            "city": city,
            "hobby": hobby,
            "age": age
        })

    # Передаём данные для отображения
    return render_template("index.html", user_data=user_data)


if __name__ == "__main__":
    app.run(debug=True)

