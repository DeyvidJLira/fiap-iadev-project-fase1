# fiap-iadev-project-fase1
Projeto destinado ao desafio da fase 1 do curso de pós graduação "AI para devs" na FIAP.

## Contexto
Dado um conjunto fictício de dados, tentar prever o valor à ser pago de plano de saúde.

## Quer ver no Google Colab?
Acesse: https://colab.research.google.com/drive/1gdghr-bwtZNTSLGELOeBupvb-38L8kjk?usp=sharing

## Rodando a aplicação
> Basta executar o código contido em ./src/start_app.ipynb

## Como estar organizado
O projeto é formado pelas seguintes pastas e arquivos, com os respectivos propósitos:
> - main.ipynb - arquivo com todo código fonte do projeto para ser executado no Google Colab;
> - data -> destinado à conter arquivos de dados, no caso em csv;
>> - raw.csv -> arquivo de dados base;
>> - processed.csv -> arquivo de dados pré-processados, gerado a partir do script *step_1_data_process.ipynb*;
>> - final.csv -> arquivo de dados final, gerado a partir do script *step_3_creating_model.ipynb*.
> - model -> destinado à conter modelos já gerados para facilitar uso posterior;
>> - model_name.pkl -> modelo gerado pelo script *step_3_creating_model.ipynb*.
> - src -> destinado à conter código fonte do projeto.
>> - start_app.ipynb -> aplicação para poder visualizar o form de preenchimento para previsão no Colab;
>> - constants.py -> arquivo de constantes;
>> - save_model_manager.py -> manager para salvar e carregar modelos;
>> - step_1_data_process.ipynb -> processar os dados contido em *raw.csv*;
>> - step_2_data_analyzing.ipynb -> analisar os dados contido em *processed.csv*;
>> - step_3_creating_model.ipynb -> realizar ajustes finais e cria o modelo baseado nos dados contido em *processed.csv;
>> - train_model.py -> contém as classes para treinamento de modelo;
>> - util.py -> contém classe utilitária para cálculos.

## Screenshots
![Form](./img/screenshot_1.PNG)
![Form submetido](./img/screenshot_2.PNG)
![Testando outro modelo](./img/screenshot_3.PNG)

## Créditos
Copyright (C) by Deyvid Jaguaribe
