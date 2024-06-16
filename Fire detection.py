from roboflow import Roboflow
rf=Roboflow(api_key="FNg3jxiAOjvDOtBnJksZ")

project=rf.workspace().project("fire-i81vb")
model=project.version(1).model


print(model.predict("a.jpg",confidence=40, overlap=30).json())

model.predict("a.jpg", confidence=40, overlap=30).save("b.jpg")


