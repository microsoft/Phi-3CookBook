## Inferencia con Kaito

[Kaito](https://github.com/Azure/kaito) es un operador que automatiza el despliegue de modelos de inferencia de IA/ML en un clúster de Kubernetes.

Kaito tiene las siguientes diferencias clave en comparación con la mayoría de las metodologías de despliegue de modelos convencionales basadas en infraestructuras de máquinas virtuales:

- Gestiona archivos de modelos utilizando imágenes de contenedor. Se proporciona un servidor HTTP para realizar llamadas de inferencia usando la biblioteca del modelo.
- Evita ajustar parámetros de despliegue para adaptarse al hardware de GPU al proporcionar configuraciones preestablecidas.
- Aprovisiona automáticamente nodos GPU según los requisitos del modelo.
- Aloja imágenes de modelos grandes en el Registro de Contenedores Público de Microsoft (MCR) si la licencia lo permite.

Con Kaito, el flujo de trabajo para integrar modelos de inferencia de IA grandes en Kubernetes se simplifica considerablemente.

## Arquitectura

Kaito sigue el clásico patrón de diseño de Definición de Recurso Personalizado (CRD)/controlador de Kubernetes. El usuario gestiona un recurso personalizado `workspace` que describe los requisitos de GPU y la especificación de inferencia. Los controladores de Kaito automatizan el despliegue reconciliando el recurso personalizado `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Arquitectura de Kaito" alt="Arquitectura de Kaito">
</div>

La figura anterior presenta una visión general de la arquitectura de Kaito. Sus componentes principales son:

- **Controlador de espacio de trabajo**: Reconciliará el recurso personalizado `workspace`, creará recursos personalizados `machine` (explicados a continuación) para activar el aprovisionamiento automático de nodos y creará la carga de trabajo de inferencia (`deployment` o `statefulset`) según las configuraciones preestablecidas del modelo.
- **Controlador de aprovisionamiento de nodos**: El nombre de este controlador es *gpu-provisioner* en el [gráfico helm de gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utiliza el CRD `machine` originado de [Karpenter](https://sigs.k8s.io/karpenter) para interactuar con el controlador de espacio de trabajo. Se integra con las APIs de Azure Kubernetes Service (AKS) para añadir nuevos nodos GPU al clúster de AKS.
> Nota: El [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) es un componente de código abierto. Puede ser reemplazado por otros controladores si soportan las APIs de [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalación

Por favor, consulta la guía de instalación [aquí](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Inicio rápido de inferencia Phi-3
[Código de ejemplo para inferencia Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

El estado del espacio de trabajo puede ser monitoreado ejecutando el siguiente comando. Cuando la columna WORKSPACEREADY sea `True`, el modelo se habrá desplegado con éxito.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

A continuación, se puede encontrar la IP del clúster del servicio de inferencia y usar un pod temporal `curl` para probar el punto final del servicio en el clúster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Inicio rápido de inferencia Phi-3 con adaptadores

Después de instalar Kaito, se pueden ejecutar los siguientes comandos para iniciar un servicio de inferencia.

[Código de ejemplo para inferencia Phi-3 con adaptadores](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

El estado del espacio de trabajo puede ser monitoreado ejecutando el siguiente comando. Cuando la columna WORKSPACEREADY sea `True`, el modelo se habrá desplegado con éxito.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

A continuación, se puede encontrar la IP del clúster del servicio de inferencia y usar un pod temporal `curl` para probar el punto final del servicio en el clúster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.