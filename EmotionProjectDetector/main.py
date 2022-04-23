from flask import Flask
from app import views

app = Flask(__name__, static_url_path="/Users/maria/PycharmProjects/EmotionProjectDetector/static",
            static_folder='/Users/maria/PycharmProjects/EmotionProjectDetector/static')

app.add_url_rule('/base','base',views.base)
app.add_url_rule('/','index',views.index)
app.add_url_rule('/project','project',views.project)
app.add_url_rule('/pasos','pasos',views.pasos)
app.add_url_rule('/detector','detector',views.detector)
app.add_url_rule('/detector/emotion','emotion',views.emotion, methods=['GET','POST'])


if __name__ == "__main__":
    app.run(debug=True)
