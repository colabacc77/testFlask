from flask import Flask, request, render_template # Импортируем модуль Flask и объект request
app = Flask(__name__) # Создаем объект app

history = [] # Создай пустой список для истории

@app.route("/", methods=["GET", "POST"]) # Декорируем функцию index с URL-адресом "/"
def index():
#     return render_template('index.html') # Возвращаем результат render_template с файлом index.html
  
# def main():
    if request.method == "POST": # Если метод запроса - POST
        question = request.form.get("question") # Получи вопрос из request.form
    else: # Если метод запроса - GET
        question = request.args.get("question") # Получи вопрос из request.args # question = request.args.get("question") # Получаем вопрос от пользователя из параметра запроса
    if question: # Если вопрос не пустой
        answer = "Это твой ответ: " + question[::-1] # Генерируем ответ, например, переворачивая вопрос задом наперед
        history.append({"question": question, "answer": answer}) # Добавь новую пару вопрос-ответ в список history
    else: # Если вопрос пустой
        answer = "Пожалуйста, задай мне вопрос" # Говорим пользователю, что нужен вопрос
    return render_template('index.html', question=question, answer=answer, history=history) # Возвращай шаблон с данными и ответом # answer # Возвращаем ответ

@app.route('/chat')
def chat():
  return render_template('chat.html', history=history)

if __name__ == "__main__":
    #index()
    app.run(host="0.0.0.0") # Запускаем сервер Flask
