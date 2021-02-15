
### To create the pod for fuzzing pillow on the cluster
`kubectl create -f pillow.yml`

### Copy the required files onto the cluster
##### Note: Use the pod `nfs-test` to get the info related to storage
##### Note: Directory for team syntax: /shared/591/syntax/
##### Pro tip: Put everything into a repo and clone it there
`exec pillow -- git clone https://github.com/r00tus3r/vr.git /shared/591/syntax/vr`

### To get the logs
`pod_logs pod/pillow`

### Delete pod
`kubectl delete pods/pillow`

### To get a lot of info on pillow pod
`kubectl describe pods/pillow`

### To get the status of all the pods
`kubectl get pods -o wide`
