docker build -t r00tus3r/sleep_hello .
docker push r00tus3r/sleep_hello
pod_create -i r00tus3r/sleep_hello /hello
kubectl get pods -o wide
kubectl describe pods/hello
pod_logs pod/hello
pod_delete pod/hello
