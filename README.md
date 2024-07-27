# fiap-iadev-project-fase1
Projeto destinado ao desafio da fase 1 do curso de pós graduação "AI para devs" na FIAP.

## Contexto
Dado um conjunto fictício de dados, tentar prever o valor à ser pago de plano de saúde.

## Quer ver no Google Colab?
[![Ver no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1gdghr-bwtZNTSLGELOeBupvb-38L8kjk?usp=sharing)

## Rodando a aplicação
> - Basta executar todos os scripts contidos em *Passo 0: Setup*;
> - Executar a função *build_and_start_app()*.

## Como estar organizado
O projeto é formado pelas seguintes pastas e arquivos, com os respectivos propósitos:
> - main.ipynb - arquivo com todo código fonte do projeto para ser executado no Google Colab, explicação sobre as seções estão contidas nele;
> - data -> destinado à conter arquivos de dados, no caso em csv;
>> - raw.csv -> arquivo de dados base;
>> - processed.csv -> arquivo de dados pré-processados, gerado a partir dos scripts contidos no *Passo 1: Processamento dos dados*;
>> - final.csv -> arquivo de dados final, gerado a partir dos scripts contidos no *Passo 3: Construindo o modelo*.
> - model -> destinado à conter modelos já gerados para facilitar uso posterior;
>> - model_name.pkl -> modelo gerado pelos scripts contidos no *Passo 3: Construindo o modelo*.

## Screenshots
![Form](./img/screenshot_1.PNG)
![Form submetido](./img/screenshot_2.PNG)
![Testando outro modelo](./img/screenshot_3.PNG)

## Avaliando os modelos

### Gradient Boosting Regressor
![Gradient Boosting Regressor Evaluate](./img/gradient_boosting_regressor_evaluate.PNG)
### Linear Regression
![Linear Regression Evaluate](./img/linear_regression_evaluate.PNG)
### Lasso Regression
![Lasso Regression Evaluate](./img/lasso_regression_evaluate.PNG)
### Ridge Regression
![Ridge Regression Evaluate](./img/ridge_regression_evaluate.PNG)
### Elastic Net Regression
![Elastic Net Regression Evaluate](./img/elastic_net_regression_evaluate.PNG)
### Support Vector Regression
![SVR Evaluate](./img/svr_evaluate.PNG)
### Random Forest Regressor
![Random Forest Regressor Evaluate](./img/random_forest_regressor_evaluate.PNG)

## Créditos
Copyright (C) by Deyvid Jaguaribe
