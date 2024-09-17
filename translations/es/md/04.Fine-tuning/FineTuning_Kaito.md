## Ajuste fino con Kaito 

[Kaito](https://github.com/Azure/kaito) es un operador que automatiza el despliegue de modelos de inferencia de IA/ML en un clúster de Kubernetes.

Kaito tiene las siguientes diferencias clave en comparación con la mayoría de las metodologías de despliegue de modelos basadas en infraestructuras de máquinas virtuales:

- Gestiona archivos de modelos utilizando imágenes de contenedores. Se proporciona un servidor http para realizar llamadas de inferencia utilizando la biblioteca del modelo.
- Evita ajustar parámetros de despliegue para adaptarse al hardware GPU proporcionando configuraciones preestablecidas.
- Aprovisiona automáticamente nodos GPU basándose en los requisitos del modelo.
- Aloja imágenes de modelos grandes en el Registro de Contenedores de Microsoft (MCR) público si la licencia lo permite.

Usando Kaito, el flujo de trabajo de incorporación de grandes modelos de inferencia de IA en Kubernetes se simplifica considerablemente.

## Arquitectura

Kaito sigue el patrón de diseño clásico de Definición de Recursos Personalizados (CRD) y controlador de Kubernetes. El usuario gestiona un recurso personalizado `workspace` que describe los requisitos de GPU y la especificación de inferencia. Los controladores de Kaito automatizarán el despliegue reconciliando el recurso personalizado `workspace`.
<div align="left">
  <img src="https://github.com/Azure/kaito/blob/main/docs/img/arch.png" width=80% title="Arquitectura de Kaito" alt="Arquitectura de Kaito">
</div>

La figura anterior presenta una visión general de la arquitectura de Kaito. Sus componentes principales consisten en:

- **Controlador de workspace**: Reconciliará el recurso personalizado `workspace`, creará recursos personalizados `machine` (explicado abajo) para activar el aprovisionamiento automático de nodos y creará la carga de trabajo de inferencia (`deployment` o `statefulset`) basándose en las configuraciones preestablecidas del modelo.
- **Controlador de aprovisionamiento de nodos**: El nombre del controlador es *gpu-provisioner* en el [helm chart de gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utiliza el CRD `machine` originado de [Karpenter](https://sigs.k8s.io/karpenter) para interactuar con el controlador de workspace. Se integra con las APIs del Servicio de Kubernetes de Azure (AKS) para agregar nuevos nodos GPU al clúster de AKS.
> Nota: El [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) es un componente de código abierto. Puede ser reemplazado por otros controladores si soportan las APIs de [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalación

Por favor, revisa la guía de instalación [aquí](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Inicio rápido

Después de instalar Kaito, se pueden probar los siguientes comandos para iniciar un servicio de ajuste fino.

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ruta de salida de ajuste fino en ACR
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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Ruta de salida de ajuste fino en ACR
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

El estado del workspace se puede rastrear ejecutando el siguiente comando. Cuando la columna WORKSPACEREADY se vuelva `True`, el modelo se habrá desplegado con éxito.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

A continuación, se puede encontrar la IP del clúster del servicio de inferencia y usar un pod temporal de `curl` para probar el punto final del servicio en el clúster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"TU PREGUNTA AQUÍ\"}"
```

Aviso legal: La traducción fue realizada a partir de su original por un modelo de IA y puede no ser perfecta. 
Por favor, revise el resultado y haga las correcciones necesarias.