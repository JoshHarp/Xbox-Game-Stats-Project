# **Xbox Game Stats Analysis**

As an avid gamer with countless hours logged, I have always been intrigued by the statistics behind each game I've played. To explore this curiosity, I created this project which analyzes the achievement data from each Xbox game I’ve ever played. The dataset contains information on the games, including the percentage of achievements completed, the total number of achievements unlocked, and the genre of the game. Ultimately, the goal is to explore the distribution of genres and identify trends based on the completion rates of the games played.

### **Project Overview:**

This Python project reads and processes a CSV file containing data on Xbox game achievements. Key tasks performed in this project include:

#### **Data Cleaning:** 
Converting the 'Percent Complete' column from string format to a numerical value.

#### **Filtering:** 
Filtering the data to focus on games with more than 50% of achievements completed.

#### **Genre Mapping:** 
Simplifying and grouping similar genres for better visualization and analysis.

#### **Visualization:** 
Creating bar charts to display:

Distribution of game genres with over 50% completion.

Distribution of all game genres, with simplified genre categories.

#### **Descriptive Statistics:**

Identifying the most common game genre.
Listing games with 100% and 1% achievement completion.
Dataset

**The dataset (Final Raw Data Xbox Stats.csv) contains the following columns:**

Game: Name of the game.

Genre: Genre(s) of the game.

Percent Complete: The percentage of achievements completed in the game.
Requirements

## **To run this project, you will need to have the following Python libraries installed:**

matplotlib (for plotting)
numpy (for numerical operations)
pandas (for data manipulation)
You can install these libraries using pip:

Instructions:

1.Clone or download this repository.

2.Ensure the Final Raw Data Xbox Stats.csv file is in the same directory as the script.

3.Run the script in your Python environment.

4.View the visualizations and printed results in the terminal.

### **Results:**

After running the script, the following information will be displayed:

The most common game genre.
The genre with the highest count of games with over 50% achievement completion.
A list of games with 100% completion and those with minimal completion (at least 1%).