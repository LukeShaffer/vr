
### Create - exec - delete
```
yans@ramoth ~/code/kuboid $ kubectl create -f nfs_test.yml 
pod/nfs-test created
yans@ramoth ~/code/kuboid $ kubectl wait --for=condition=ready pod/nfs-test
pod/nfs-test condition met
yans@ramoth ~/code/kuboid $ kubectl exec nfs-test -- ls -l /shared/591
total 3
drwxr-xr-x. 2 nobody nogroup 2 Feb 11 09:36 airspace
drwxr-xr-x. 2 nobody nogroup 2 Feb 11 09:36 conclusion
drwxr-xr-x. 2 nobody nogroup 2 Feb 11 09:36 syntax
drwxr-xr-x. 2 nobody nogroup 2 Feb 11 09:36 transmitter
drwxr-xr-x. 2 nobody nogroup 2 Feb 11 09:36 unconquerable
yans@ramoth ~/code/kuboid $ kubectl delete -f nfs_test.yml 
pod "nfs-test" deleted
```
