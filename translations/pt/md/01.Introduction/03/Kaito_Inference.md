## Inferência com Kaito

[Kaito](https://github.com/Azure/kaito) é um operador que automatiza o processo de implantação de modelos de inferência de IA/ML em um cluster Kubernetes.

Kaito possui as seguintes diferenças principais em comparação com a maioria das metodologias convencionais de implantação de modelos baseadas em infraestruturas de máquinas virtuais:

- Gerenciar arquivos de modelo usando imagens de contêiner. Um servidor HTTP é fornecido para realizar chamadas de inferência utilizando a biblioteca do modelo.
- Evitar ajustes nos parâmetros de implantação para se adequar ao hardware GPU, oferecendo configurações predefinidas.
- Provisionamento automático de nós GPU com base nos requisitos do modelo.
- Hospedar imagens de modelos grandes no Registro de Contêiner Público da Microsoft (MCR), se a licença permitir.

Com o Kaito, o fluxo de trabalho para incorporar grandes modelos de inferência de IA no Kubernetes é amplamente simplificado.

## Arquitetura

Kaito segue o padrão clássico de design de Definição de Recurso Personalizado (CRD) / controlador do Kubernetes. O usuário gerencia um recurso personalizado `workspace` que descreve os requisitos de GPU e a especificação de inferência. Os controladores do Kaito automatizam a implantação reconciliando o recurso personalizado `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Arquitetura do Kaito" alt="Arquitetura do Kaito">
</div>

A figura acima apresenta uma visão geral da arquitetura do Kaito. Seus principais componentes consistem em:

- **Controlador de workspace**: Ele reconcilia o recurso personalizado `workspace`, cria recursos personalizados `machine` (explicados abaixo) para acionar o provisionamento automático de nós e cria a carga de trabalho de inferência (`deployment` ou `statefulset`) com base nas configurações predefinidas do modelo.
- **Controlador de provisionamento de nós**: O nome deste controlador é *gpu-provisioner* no [helm chart gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ele utiliza o CRD `machine` originado do [Karpenter](https://sigs.k8s.io/karpenter) para interagir com o controlador de workspace. Ele se integra às APIs do Azure Kubernetes Service (AKS) para adicionar novos nós GPU ao cluster AKS.  
> Nota: O [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) é um componente de código aberto. Ele pode ser substituído por outros controladores, caso suportem as APIs do [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalação

Por favor, consulte o guia de instalação [aqui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Início rápido: Inferência Phi-3
[Código de Exemplo para Inferência Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3
inference:
  preset:
    name: phi-3-mini-4k-instruct
    # Note: This configuration also works with the phi-3-mini-128k-instruct preset
```

```sh
$ cat examples/inference/kaito_workspace_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-4k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

O status do workspace pode ser monitorado executando o seguinte comando. Quando a coluna WORKSPACEREADY se tornar `True`, o modelo foi implantado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Em seguida, é possível localizar o IP do serviço de inferência no cluster e usar um pod temporário `curl` para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Início rápido: Inferência Phi-3 com adaptadores

Após instalar o Kaito, é possível executar os seguintes comandos para iniciar um serviço de inferência.

[Código de Exemplo para Inferência Phi-3 com Adaptadores](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3-adapter
inference:
  preset:
    name: phi-3-mini-128k-instruct
  adapters:
    - source:
        name: "phi-3-adapter"
        image: "ACR_REPO_HERE.azurecr.io/ADAPTER_HERE:0.0.1"
      strength: "1.0"
```

```sh
$ cat examples/inference/kaito_workspace_phi_3_with_adapters.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
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
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

O status do workspace pode ser monitorado executando o seguinte comando. Quando a coluna WORKSPACEREADY se tornar `True`, o modelo foi implantado com sucesso.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Em seguida, é possível localizar o IP do serviço de inferência no cluster e usar um pod temporário `curl` para testar o endpoint do serviço no cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se uma tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.