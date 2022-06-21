import numpy as np


def brain_predict(number:int=1) -> int:
    """Guess the number. Algorithm - each time divides the range by 2 

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Number of attempts
    """

    count = 0
    max_range = 100
    min_range = 1
    pre_predict = 0
    
    while True:
        count+=1
        
        predict_number = int((max_range - min_range)/2 + min_range)
        #Devide the range by 2
        
        if predict_number==pre_predict:
            predict_number+=1
        #Because rounding goes by discarding the fractional part 
        # if the intended number is 100 it will be 99 all the time
            
        if number==predict_number:
            break
        
        if number>predict_number:
            min_range = predict_number
            pre_predict = predict_number
            
        if number<predict_number:
            max_range = predict_number 
            pre_predict = predict_number          
    return(count)


def score_game() -> int:
    """For how many attempts on average out of 1000 approaches
    our algorithm guesses

    Args:
        brain_predict ([type]): Guess function

    Returns:
        int: Average number of tries
    """
     
    count_ls = [] # List to save the number of attempts
    np.random.seed(1) # Fix seed for reproducibility
    # made a list of numbers
    random_array = np.random.randint(1, 101, size=(1000)) 

    for number in random_array:
        count_ls.append(brain_predict(number))

    score = int(np.mean(count_ls)) # Find the average number of attempts
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game()