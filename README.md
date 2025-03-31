# **Movie Recommender System**  

### **Project Overview**  
The **Movie Recommender System** is a machine learning-based web application that suggests movies based on user input. The system allows users to search for a movie, and it recommends **5 similar movies** along with their posters. This enhances the user experience by providing relevant movie suggestions based on content similarity.  

### **Features**  
✅ **Movie Search** – Users can enter the name of a movie to get recommendations.  
✅ **Movie Recommendations** – The system suggests 5 similar movies based on content similarity.  
✅ **Movie Posters** – Fetches and displays posters of recommended movies for a visually appealing interface.  
✅ **User-Friendly Interface** – Implemented using **Streamlit** for easy interaction.  

### **Technologies Used**  
🔹 **Python** – Core programming language for implementing machine learning models.  
🔹 **Pandas & NumPy** – Used for data handling and preprocessing.  
🔹 **Scikit-Learn** – Used for building the recommendation model.  
🔹 **Streamlit** – To create an interactive web-based UI.  
🔹 **Requests API** – Fetches movie posters using an API key.  

### **Working Principle**  
1. **Data Processing** – The dataset is cleaned and processed to extract meaningful features.  
2. **Vectorization** – Text data (movie descriptions) is converted into numerical format using **TF-IDF** or **CountVectorizer**.  
3. **Similarity Calculation** – Cosine similarity is used to find similar movies.  
4. **User Input & Recommendation** – When a user searches for a movie, the system finds and displays the **5 most similar movies**.  

### **Conclusion**  
This project provides a simple yet effective approach to movie recommendation using **machine learning**. It can be further improved by incorporating **collaborative filtering**, **deep learning models**, or **real-time user preferences** for better recommendations.  

