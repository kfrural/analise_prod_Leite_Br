# Carregando as bibliotecas necessárias
library(ggplot2)
library(dplyr)
library(reshape2)
library(gmodels)
library(reshape)

# Carregando os dados
leite <- read.csv('producao_leite.csv')

# Explorando os dados
head(leite)
str(leite)

# Visualizando a produção de leite por região
ggplot(leite, aes(x = regiao, y = producao)) +
  geom_bar(stat = 'identity') +
  labs(title = 'Produção de Leite por Região', x = 'Região', y = 'Produção (litros)')

# Analisando a relação entre produção e tecnologia
ggplot(leite, aes(x = tecnologia, y = producao)) +
  geom_point() +
  labs(title = 'Relação entre Produção e Tecnologia', x = 'Tecnologia', y = 'Produção (litros)')

# Modelando a produção de leite
model <- lm(producao ~ tecnologia + genetica + manejo, data = leite)

# Avaliando o modelo
summary(model)

# Fazendo previsões
new_data <- data.frame(tecnologia = 80, genetica = 90, manejo = 85)
predicted_production <- predict(model, new_data)
print('Produção Prevista:', predicted_production)
