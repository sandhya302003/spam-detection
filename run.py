from src.model import train_and_evaluate
from src.predict import predict_spam

if __name__ == '__main__':
    data_path = 'data/spam.csv'
    train_and_evaluate(data_path)

    # Test prediction on new message
    test_message = 'Congratulations! You have won a free ticket to Bahamas. Call now!'
    print(f'Prediction for test message: {predict_spam(test_message)}')
