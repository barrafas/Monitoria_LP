# Retorna a média dos scores representados pelos valores em um dicionário
def average_scores(scores_dict):
    if type(scores_dict) != dict: #Levanta um erro caso o parâmetro não seja um dicionário
        raise TypeError 
    scores = scores_dict.values()
    if len(scores) == 0:#Levanta um erro caso o parâmetro seja um dicionário vazio
        raise ValueError
    scores_mean = 0
    for score in scores:
        scores_mean += score
    scores_mean = scores_mean/len(scores)
    return scores_mean
        
