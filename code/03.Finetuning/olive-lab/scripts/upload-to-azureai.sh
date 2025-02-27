az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group RESOURCE_GROUP \
    --workspace-name PROJECT_NAME
