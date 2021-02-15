
### Create Dockerfile with contents
```
FROM ubuntu:20.04
COPY hello /
CMD ["/hello"]
```

### Build the docker container with name `r00tus3r/sleep_hello`
`docker build -t r00tus3r/sleep_hello .`

### Push to dockerhub
`docker push r00tus3r/sleep_hello`

### Create the pod on your cluster
`pod_create -i r00tus3r/sleep_hello /hello`

### Helpful for debugging/ getting status
`kubectl get pods -o wide`
`kubectl describe pods/hello`

### Get logs
`pod_logs pod/hello`

### Delete pods
`pod_delete pod/hello`
