
# Orchestration Layers Design: Entry Point Modeling

# Orchestration Layers Design: Entry Point Modeling

from src.data_ingestion import data_ingestion
from src.data_preprocessing import data_preprocessing

def main():
    # Step 1: Data Ingestion (Data load karna)
    df = data_ingestion()
    
    # Step 2: Data Preprocessing & Feature Engineering
    X_train, X_test, y_train, y_test = data_preprocessing(df)
    
    # Step 3: Success Check
    print("Pipeline executed successfully!")
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")

if __name__ == '__main__':
    main()