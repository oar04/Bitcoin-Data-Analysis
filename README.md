# ETL Pipeline for Bitcoin Data

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline for Bitcoin data. The pipeline extracts Bitcoin price data, related news articles, and Google Trends data, transforms them into a single dataframe, and loads the transformed data into a CSV file. Additionally, the project includes steps for data visualization and training a model.

## Dependencies

Make sure to install the following dependencies:

- pytrends
- pandas
- numpy
- nltk
- seaborn
- scikit-learn

You can install these dependencies using the following commands:
- !pip install pytrends
- !pip install pandas
- !pip install numpy
- !pip install nltk
- !pip install seaborn
- !pip install scikit-learn


Please note that additional dependencies might be required depending on your specific project setup and requirements. Make sure to install any other necessary libraries based on the error messages or specific instructions provided in your project's documentation.

## Getting Started

To run the project, follow these steps:

1. Clone the repository to your local machine.
2. Open the project in Jupyter Notebook.
3. Before running the notebook, make sure to delete the `bitcoin_monthly_trends.csv` and `Bitcoin_news_trends.csv` files if they exist in the project directory. This step helps avoid any potential writing permission errors.
4. Run the notebook cells to execute the ETL pipeline, visualize the data, and train the model.

## Data Sources

The following data sources were used in this project:

- The `historical_bitcoin_data.csv` file was downloaded from [Investing.com](https://uk.investing.com/crypto/bitcoin/historical-data).
- The `cryptonews.csv` file was downloaded from [Kaggle](https://www.kaggle.com/datasets/oliviervha/crypto-news).

## Acknowledgements

I would like to express my gratitude to Xander Talent for their training throughout this past two months. Their guidance has been invaluable in helping me accomplish my career goals.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code for your own purposes.

## Conclusion

This ETL pipeline provides a comprehensive solution for extracting, transforming, and loading Bitcoin data. It combines price data, news articles, and Google Trends data into a single dataframe, enabling further analysis and modeling. The project demonstrates how to handle multiple data sources, perform data cleaning and transformation, and leverage visualization and machine learning techniques for deeper insights.

Please feel free to customize and enhance the pipeline based on your specific requirements and use cases. Happy analyzing!
