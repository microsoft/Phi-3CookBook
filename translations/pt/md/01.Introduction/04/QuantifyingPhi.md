# **Quantificando a Família Phi**

A quantização de modelos refere-se ao processo de mapeamento dos parâmetros (como pesos e valores de ativação) em um modelo de rede neural de um intervalo de valores amplo (geralmente um intervalo contínuo) para um intervalo de valores finito menor. Essa tecnologia pode reduzir o tamanho e a complexidade computacional do modelo, além de melhorar a eficiência operacional em ambientes com recursos limitados, como dispositivos móveis ou sistemas embarcados. A quantização do modelo alcança a compressão ao reduzir a precisão dos parâmetros, mas também introduz uma certa perda de precisão. Portanto, no processo de quantização, é necessário equilibrar o tamanho do modelo, a complexidade computacional e a precisão. Métodos comuns de quantização incluem quantização de ponto fixo, quantização de ponto flutuante, entre outros. É possível escolher a estratégia de quantização mais adequada de acordo com o cenário e as necessidades específicas.

Nosso objetivo é implantar o modelo GenAI em dispositivos de borda e permitir que mais dispositivos entrem em cenários de GenAI, como dispositivos móveis, PCs com IA/PC Copilot+ e dispositivos IoT tradicionais. Por meio da quantização do modelo, podemos implantá-lo em diferentes dispositivos de borda com base nas características de cada um. Combinando o framework de aceleração de modelo e os modelos quantizados fornecidos pelos fabricantes de hardware, podemos criar melhores cenários de aplicação para SLM.

No cenário de quantização, temos diferentes níveis de precisão (INT4, INT8, FP16, FP32). A seguir, uma explicação sobre as precisões de quantização mais utilizadas:

### **INT4**

A quantização INT4 é um método radical que quantiza os pesos e os valores de ativação do modelo em números inteiros de 4 bits. Geralmente, a quantização INT4 resulta em uma perda maior de precisão devido ao intervalo de representação mais restrito e à menor precisão. No entanto, em comparação com a quantização INT8, a INT4 pode reduzir ainda mais os requisitos de armazenamento e a complexidade computacional do modelo. É importante observar que a quantização INT4 é relativamente rara em aplicações práticas, pois a precisão muito baixa pode causar uma degradação significativa no desempenho do modelo. Além disso, nem todo hardware suporta operações INT4, portanto, a compatibilidade com o hardware deve ser considerada ao escolher um método de quantização.

### **INT8**

A quantização INT8 é o processo de converter os pesos e ativações de um modelo de números de ponto flutuante para números inteiros de 8 bits. Embora o intervalo numérico representado por inteiros INT8 seja menor e menos preciso, essa abordagem pode reduzir significativamente os requisitos de armazenamento e cálculo. Na quantização INT8, os pesos e valores de ativação do modelo passam por um processo de quantização, incluindo escalonamento e deslocamento, para preservar ao máximo as informações originais de ponto flutuante. Durante a inferência, esses valores quantizados são desquantizados de volta para números de ponto flutuante para o cálculo e, em seguida, quantizados novamente para INT8 na etapa seguinte. Esse método pode oferecer precisão suficiente na maioria das aplicações, mantendo alta eficiência computacional.

### **FP16**

O formato FP16, ou seja, números de ponto flutuante de 16 bits (float16), reduz pela metade o uso de memória em comparação com números de ponto flutuante de 32 bits (float32), o que apresenta vantagens significativas em aplicações de aprendizado profundo em larga escala. O formato FP16 permite carregar modelos maiores ou processar mais dados dentro das limitações de memória da GPU. À medida que o hardware moderno de GPU continua a oferecer suporte para operações FP16, o uso do formato FP16 também pode trazer melhorias na velocidade de computação. No entanto, o formato FP16 tem suas desvantagens inerentes, como menor precisão, o que pode levar a instabilidade numérica ou perda de precisão em alguns casos.

### **FP32**

O formato FP32 oferece maior precisão e pode representar com exatidão uma ampla gama de valores. Em cenários que envolvem operações matemáticas complexas ou que exigem resultados de alta precisão, o formato FP32 é preferido. No entanto, maior precisão também significa maior uso de memória e maior tempo de cálculo. Para modelos de aprendizado profundo em larga escala, especialmente quando há muitos parâmetros e uma enorme quantidade de dados, o formato FP32 pode causar insuficiência de memória na GPU ou redução na velocidade de inferência.

Em dispositivos móveis ou IoT, podemos converter modelos Phi-3.x para INT4, enquanto PCs com IA/PC Copilot podem usar precisões mais altas, como INT8, FP16 ou FP32.

Atualmente, diferentes fabricantes de hardware possuem frameworks distintos para dar suporte a modelos generativos, como o OpenVINO da Intel, o QNN da Qualcomm, o MLX da Apple e o CUDA da Nvidia. Combinando esses frameworks com a quantização do modelo, é possível realizar implantações locais.

Em termos de tecnologia, temos suporte para diferentes formatos após a quantização, como os formatos PyTorch/TensorFlow, GGUF e ONNX. Fiz uma comparação entre os formatos GGUF e ONNX e seus cenários de aplicação. Aqui, recomendo o formato ONNX para quantização, pois ele possui bom suporte do framework do modelo ao hardware. Neste capítulo, vamos nos concentrar no ONNX Runtime para GenAI, OpenVINO e Apple MLX para realizar a quantização de modelos (se você tiver uma abordagem melhor, pode nos enviar por meio de um PR).

**Este capítulo inclui**

1. [Quantizando Phi-3.5 / 4 usando llama.cpp](./UsingLlamacppQuantifyingPhi.md)

2. [Quantizando Phi-3.5 / 4 usando extensões de IA generativa para onnxruntime](./UsingORTGenAIQuantifyingPhi.md)

3. [Quantizando Phi-3.5 / 4 usando Intel OpenVINO](./UsingIntelOpenVINOQuantifyingPhi.md)

4. [Quantizando Phi-3.5 / 4 usando o Framework Apple MLX](./UsingAppleMLXQuantifyingPhi.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.