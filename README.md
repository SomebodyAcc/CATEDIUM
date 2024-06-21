<h1>Catedium App</h1>

<h3>Catedium is a mobile app that helps users distinguish between 10 types of big cats, like lions, tigers, and jaguars, which are often hard to tell apart. The app educates and aids in recognizing and understanding these cats' differences.</h3>
<p>This app will classify 10 types of big cats with the following labels:</p>
<ul>
  <li>African Leopard</li>
  <li>Caracal</li>
  <li>Cheetah</li>
  <li>Clouded Leopard</li>
  <li>Jaguar</li>
  <li>Lion</li>
  <li>Ocelot</li>
  <li>Puma</li>
  <li>Snow Leopard</li>
  <li>Tiger</li>
</ul>

<h2>Machine Learning Path</h2>

<p>We at Machine Learning Path have built a model for catedium with the following steps:</p>

![Alt Text](https://i.imgur.com/BCB6JOu.jpeg)

<p><strong>Part 1: Data Preprocessing</strong></p>
<ul>
 <li>Imported necessary libraries such as TensorFlow and os.</li>
 <li>Accessed Google Drive to retrieve the dataset and extracted the dataset into the working directory.</li>
 <li>Performed data augmentation and image normalization using <code>ImageDataGenerator</code>.</li>
 <li>Created generators for the training, validation, and test sets.</li>
</ul>
<p><strong>Part 2: Model Building</strong></p>
<ul>
 <li>Created a Convolutional Neural Network (CNN) model using TensorFlow's Sequential API.</li>
 <li>Added several Conv2D, MaxPooling2D, Flatten, Dense, and Dropout layers.</li>
 <li>Compiled the model with the 'adam' optimizer, 'categorical_crossentropy' loss function, and 'accuracy' metric.</li>
</ul>
<p><strong>Part 3: Model Training</strong></p>
<ul>
 <li>Trained the model using data generators for the training and validation sets.</li>
 <li>Set the number of epochs for training and monitored the model's performance on the validation set.</li>
</ul>
<p><strong>Part 4: Model Evaluation and Prediction</strong></p>
<ul>
 <li>Evaluated the model's performance on the test set and displayed accuracy.</li>
 <li>Saved the trained model in <code>.h5</code> and <code>SavedModel</code> formats.</li>
 <li>Loaded the saved model for reuse.</li>
 <li>Created a function to display sample images along with predictions and true labels.</li>
</ul>
<p><strong>Part 5: Testing to Unknown Data</strong></p>
<ul>
 <li>Prepared test data from a zip file and created a generator for the test data.</li>
 <li>Uploaded new images, processed them, and made predictions using the trained model.</li>
<li>Displayed the images along with the predicted class provided by the model.</li>
</ul>
<p><strong>Part 6: API</strong></p>
<ul>
 <li>Implemented a REST API using Flask.</li>
 <li>Loaded the trained CNN model and created a function to preprocess images.</li>
 <li>Created an endpoint <code>/predict</code> that accepts image files, processes them, and provides predictions in JSON format.</li>
 <li>Used Postman to test this endpoint.</li>
 <li>Handed over the model and REST API to the Path Cloud team for deployment.</li>
</ul>


<h2>Cloud Computing Path</h2>
<p>As a cloud computing path, we design backend services to bridge machine learning models and mobile applications. Starting from designing the response structure on the API, then deploying the backend application to Google Cloud Run and we also create a website version of the application.</p>

![Alt Text](https://i.imgur.com/jcitHK4.png)


<h2>Mobile Developer Path</h2>
<p>As a mobile developer path, we created a mobile application using Kotlin language with Android Studio. In this manufacture, it uses images as a benchmark to check which class the cat is in. When the image has been obtained from the camera or uploaded, the image will be sent to the fire that has been created. When the image is processed by the fire and returns the name of the cat class, the application will display information that matches the cat class.</p>

![Alt Text](https://i.imgur.com/1HAtpza.png)

