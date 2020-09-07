#!/bin/bash

echo "Start clean-up process:"

echo "[Step 1] Delete ingress"
kubectl delete ingress metadefender-menlo-ingress

echo "[Step 2] Delete service"
kubectl delete service metadefender-menlo-service

echo "[Step 3] Delete secret"
kubectl delete secret metadefender-menlo-secret-tls

echo "[Step 4] Delete deployment"
kubectl delete deployment metadefender-menlo-deployment

echo "[Step 5] Delete self-signed keys"
rm csr_details.txt rootCA.crt rootCA.key rootCA.srl tls.crt server.csr tls.key

echo "[Step 6] Delete static IP"
gcloud compute addresses delete metadefender-menlo-static-ip --global

# echo "[STEP 7] Delete cluster"
# gcloud container clusters delete metadefender-menlo-cluster

echo "Done."