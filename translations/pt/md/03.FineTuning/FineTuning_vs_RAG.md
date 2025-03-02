## Ajuste Fino vs RAG

## Geração com Recuperação de Dados

RAG combina recuperação de dados com geração de texto. Os dados estruturados e não estruturados da empresa são armazenados no banco de dados vetorial. Ao buscar por conteúdo relevante, um resumo e o conteúdo correspondente são encontrados para formar um contexto, e a capacidade de completar texto do LLM/SLM é utilizada para gerar conteúdo.

## Processo RAG
![FinetuningvsRAG](../../../../translated_images/rag.36e7cb856f120334d577fde60c6a5d7c5eecae255dac387669303d30b4b3efa4.pt.png)

## Ajuste Fino
O ajuste fino é baseado na melhoria de um modelo existente. Não é necessário começar do zero com o algoritmo do modelo, mas é preciso acumular dados continuamente. Se você busca uma terminologia mais precisa e uma expressão linguística mais adequada para aplicações industriais, o ajuste fino é a melhor escolha. No entanto, se seus dados mudam frequentemente, o ajuste fino pode se tornar complicado.

## Como escolher
Se a nossa resposta requer a introdução de dados externos, o RAG é a melhor escolha.

Se você precisa produzir conhecimento especializado estável e preciso, o ajuste fino será uma boa opção. O RAG prioriza a recuperação de conteúdo relevante, mas pode não captar sempre as nuances especializadas.

O ajuste fino exige um conjunto de dados de alta qualidade, e se for apenas um pequeno volume de dados, não fará muita diferença. O RAG é mais flexível.  
O ajuste fino é uma "caixa preta", uma abordagem difícil de entender em relação ao seu mecanismo interno. Por outro lado, o RAG facilita a identificação da origem dos dados, permitindo ajustar de forma mais eficaz alucinações ou erros de conteúdo e oferecendo maior transparência.

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução humana profissional. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.