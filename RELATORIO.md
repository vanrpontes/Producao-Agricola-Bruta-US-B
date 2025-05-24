# Relatório do Projeto: Produção Agrícola Bruta (US$ B) – Web App em Python + Streamlit
## 📅 Data: 24 de maio de 2025
## Autor: Van Pontes
## GitHub: https://github.com/vanrpontes/Producao-Agricola-Bruta-US-B/tree/main
## App Online: https://appucao-agricola-bruta-us-b.streamlit.app/ (hospedado no Streamlit Cloud)

## Objetivo
Desenvolver um web app interativo utilizando Python, Pandas, Altair e Streamlit para apresentar, de forma visual, acessível e dinâmica, os dados de produção agrícola bruta de diferentes países ao longo dos anos.

## Tecnologias e Bibliotecas
- Python
- Pandas
- Streamlit
- Altair
Dataset público hospedado no repositório GitHub (data/agri.csv).

## Desafios Encontrados e Soluções
1. Carregamento de dados e configuração do índice
 - Problema: O dataset original possui a coluna Region, mas havia sido alterado para País no CSV local, quebrando a leitura.
 - Solução: Padronizei o arquivo CSV e ajustei o código para trabalhar corretamente com Region como índice.

2. Tamanho fixo da tabela no Streamlit
 - Problema: A tabela exibia todas as linhas, o que tornava a visualização pouco prática.
 - Solução: Ajustei a propriedade height do st.dataframe para limitar a visualização a cerca de 6-7 linhas, ativando o scroll automático.

3. Gráfico Altair com sobreposição de áreas inadequada
 - Problema: O gráfico de área apresentava desalinhamento e áreas não sobrepostas corretamente quando mais de um país era selecionado.
 - Solução: Corrigi a estrutura do DataFrame com pd.melt, garantindo o uso correto da variável Region para agrupamento, e configurei a codificação de cores por país via alt.Color("Region:N"). Também ajustei o mark_area com interpolate='monotone' e opacidade em 0.3 para melhor visualização.

4. Gráfico sem dados visíveis
 - Problema: Mesmo após ajustes, o gráfico não exibia dados.
 - Solução: Corrigi nomes de colunas e tipos de dados utilizados no Altair, revisei o fluxo e normalização dos dados para garantir o formato longo (“tidy data”) esperado.

## Resultado Final
- Tabela interativa com scroll vertical e horizontal
- Multiselect para seleção dinâmica de países
- Gráfico de área com sobreposição colorida, interpolação suave e tooltip customizado
- App responsivo e leve, hospedado no Streamlit Cloud, acessível publicamente via web
# Veja o app funcionando aqui: [Produção Agrícola Bruta App](https://appucao-agricola-bruta-us-b.streamlit.app/)

## Lições Aprendidas
- Importância da padronização de nomes de colunas em bases de dados
- Manipulação de dados para gráficos no formato longo (“tidy data”)
- Controle de layout e propriedades de visualização no Streamlit
- Customização avançada de gráficos Altair, incluindo tooltips e interpolação
- Valor de mensagens de erro claras para debug e experiência do usuário

## Próximos Passos
- Adicionar funcionalidades para exportar gráficos e tabelas em PNG e CSV
- Implementar filtros por período (ano inicial e final)
- Publicar o projeto no portfólio pessoal e promover o app em redes sociais e comunidades técnicas


