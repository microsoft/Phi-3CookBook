## Ajuste fino con Kaito 

[Kaito](https://github.com/Azure/kaito) es un operador que automatiza el despliegue de modelos de inferencia de IA/ML en un clúster de Kubernetes.

Kaito tiene las siguientes diferencias clave en comparación con la mayoría de las metodologías de despliegue de modelos convencionales basadas en infraestructuras de máquinas virtuales:

- Gestiona los archivos de modelos utilizando imágenes de contenedor. Se proporciona un servidor HTTP para realizar llamadas de inferencia utilizando la biblioteca del modelo.
- Evita ajustar parámetros de despliegue para adaptarse al hardware GPU al proporcionar configuraciones predefinidas.
- Aprovisiona automáticamente nodos GPU según los requisitos del modelo.
- Aloja imágenes de modelos grandes en el Registro de Contenedores Público de Microsoft (MCR) si la licencia lo permite.

Con Kaito, el flujo de trabajo para incorporar modelos de inferencia de IA grandes en Kubernetes se simplifica considerablemente.

## Arquitectura

Kaito sigue el clásico patrón de diseño de Definición de Recurso Personalizado (CRD)/controlador de Kubernetes. El usuario gestiona un recurso personalizado `workspace` que describe los requisitos de GPU y la especificación de inferencia. Los controladores de Kaito automatizarán el despliegue reconciliando el recurso personalizado `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Arquitectura de Kaito" alt="Arquitectura de Kaito">
</div>

La figura anterior presenta una visión general de la arquitectura de Kaito. Sus componentes principales incluyen:

- **Controlador de espacio de trabajo**: Reconciliará el recurso personalizado `workspace`, creará recursos personalizados `machine` (explicados más abajo) para activar el aprovisionamiento automático de nodos, y generará la carga de trabajo de inferencia (`deployment` o `statefulset`) basándose en las configuraciones predefinidas del modelo.
- **Controlador de aprovisionamiento de nodos**: El nombre de este controlador es *gpu-provisioner* en el [helm chart de gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utiliza el CRD `machine` originado de [Karpenter](https://sigs.k8s.io/karpenter) para interactuar con el controlador del espacio de trabajo. Se integra con las APIs del Servicio de Kubernetes de Azure (AKS) para añadir nuevos nodos GPU al clúster de AKS.  
> Nota: El [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) es un componente de código abierto. Puede ser reemplazado por otros controladores si soportan las APIs de [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video de introducción 
[Mira la demo de Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalación

Por favor, consulta la guía de instalación [aquí](https://github.com/Azure/kaito/blob/main/docs/installation.md).

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

El estado del espacio de trabajo puede ser rastreado ejecutando el siguiente comando. Cuando la columna WORKSPACEREADY cambie a `True`, el modelo habrá sido desplegado con éxito.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

A continuación, se puede encontrar la IP del clúster del servicio de inferencia y usar un pod temporal de `curl` para probar el endpoint del servicio en el clúster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.