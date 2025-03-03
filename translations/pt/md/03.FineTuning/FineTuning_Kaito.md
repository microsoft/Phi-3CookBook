## Ajuste Fino com Kaito

[Kaito](https://github.com/Azure/kaito) é um operador que automatiza a implantação de modelos de inferência de IA/ML em um cluster Kubernetes.

Kaito apresenta as seguintes diferenças principais em relação à maioria das metodologias de implantação de modelos baseadas em infraestruturas de máquinas virtuais:

- Gerenciar arquivos de modelo usando imagens de contêiner. Um servidor HTTP é fornecido para realizar chamadas de inferência utilizando a biblioteca do modelo.
- Evitar ajustes de parâmetros de implantação para se adequar ao hardware GPU, fornecendo configurações pré-definidas.
- Provisionamento automático de nós GPU com base nos requisitos do modelo.
- Hospedar grandes imagens de modelos no Microsoft Container Registry (MCR) público, se a licença permitir.

Com o Kaito, o fluxo de trabalho para integrar grandes modelos de inferência de IA no Kubernetes é amplamente simplificado.

## Arquitetura

Kaito segue o padrão clássico de design de Definição de Recurso Personalizado (CRD)/controlador do Kubernetes. O usuário gerencia um recurso personalizado `workspace` que descreve os requisitos de GPU e a especificação de inferência. Os controladores do Kaito automatizam a implantação conciliando o recurso personalizado `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Arquitetura do Kaito" alt="Arquitetura do Kaito">
</div>

A figura acima apresenta uma visão geral da arquitetura do Kaito. Seus principais componentes consistem em:

- **Controlador de workspace**: Ele concilia o recurso personalizado `workspace`, cria recursos personalizados `machine` (explicados abaixo) para acionar o provisionamento automático de nós e cria a carga de trabalho de inferência (`deployment` ou `statefulset`) com base nas configurações pré-definidas do modelo.
- **Controlador de provisionamento de nós**: O nome do controlador é *gpu-provisioner* no [helm chart gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ele utiliza o CRD `machine` originado do [Karpenter](https://sigs.k8s.io/karpenter) para interagir com o controlador de workspace. Ele se integra às APIs do Azure Kubernetes Service (AKS) para adicionar novos nós GPU ao cluster AKS. 
> Nota: O [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) é um componente de código aberto. Ele pode ser substituído por outros controladores, desde que suportem as APIs do [Karpenter-core](https://sigs.k8s.io/karpenter).

## Vídeo de visão geral
[Assista à demonstração do Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalação

Por favor, confira o guia de instalação [aqui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Início rápido

Após instalar o Kaito, é possível executar os seguintes comandos para iniciar um serviço de ajuste fino.

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
```

```sh
$ cat examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

O status do workspace pode ser acompanhado executando o comando a seguir. Quando a coluna WORKSPACEREADY se tornar `True`, o modelo foi implantado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Em seguida, é possível encontrar o IP do cluster do serviço de inferência e usar um pod temporário `curl` para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.