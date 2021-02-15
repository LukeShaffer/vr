
### To create the pod for fuzzing pillow on the cluster
`kubectl create -f pillow.yml`

### To get the logs
`pod_logs pod/pillow`

### Delete pod
`kubectl delete pods/pillow`

### To get a lot of info on pillow pod
`kubectl describe pods/pillow`

### To get the status of all the pods
`kubectl get pods -o wide`
