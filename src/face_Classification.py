# develop a classifier for the 5 Celebrity Faces Dataset
from random import choice
from numpy import load
from numpy import expand_dims
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from matplotlib import pyplot

# load faces
data = load('exc/test_compare_img_np.npz')
testX_faces = data['arr_0']
# load face embeddings
data = load('exc/test_compare_embeddings.npz')
trainX, label = data['arr_0'], data['arr_1']

# normalize input vectors
in_encoder = Normalizer(norm='l2')
print(trainX)
trainX = in_encoder.transform(trainX)
testX = in_encoder.transform(trainX)

# label encode targets
trainy = label
out_encoder = LabelEncoder()
out_encoder.fit(trainy)
print(trainy)
trainy = out_encoder.transform(trainy)
testy = out_encoder.transform(label)

# fit model
model = SVC(kernel='linear', probability=True)
model.fit(trainX, trainy)

# test model on a random example from the test data
# selection = choice([i for i in range(testX.shape[0])])
# random_face_pixels = testX_faces[selection]
# random_face_emb = testX[selection]
# random_face_class = testy[selection]
# random_face_name = out_encoder.inverse_transform([random_face_class])
#
# # prediction for the face
# samples = expand_dims(random_face_emb, axis=0)
# yhat_class = model.predict(samples)
# yhat_prob = model.predict_proba(samples)


# SVM
x = 0
for i in range(testX.shape[0]):
    # print(testX.shape[0])
    random_face_pixels = testX_faces[i]
    random_face_emb = testX[i]
    random_face_class = testy[i]
    random_face_name = out_encoder.inverse_transform([random_face_class])
    # prediction for the face
    samples = expand_dims(random_face_emb, axis=0)
    yhat_class = model.predict(samples)
    yhat_prob = model.predict_proba(samples)
    class_index = yhat_class[0]
    class_probability = yhat_prob[0, class_index] * 100
    print(class_probability)
    x += class_probability

print(x / (testX.shape[0]))



# get name
# class_index = yhat_class[0]
# class_probability = yhat_prob[0,class_index] * 100
# predict_names = out_encoder.inverse_transform(yhat_class)
# print('Predicted: %s (%.3f)' % (predict_names[0], class_probability))
# print('Expected: %s' % random_face_name[0])
# plot for fun
# pyplot.imshow(random_face_pixels)
# title = '%s (%.3f)' % (predict_names[0], class_probability)
# pyplot.title(title)
# pyplot.show()
# print("done")