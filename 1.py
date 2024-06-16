from roboflow import Roboflow
rf = Roboflow(api_key="FNg3jxiAOjvDOtBnJksZ")
project = rf.workspace().project("fire-i81vb")
model=project.version(1).model
model.predict("a.jpg", confidence=20).save("b.jpg")
