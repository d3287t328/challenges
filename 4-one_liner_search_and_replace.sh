grep -q "^replicaCount: 1" values.yaml && grep -q '^serviceName: "nginx"' values.yaml && grep -q '^image: "nginx:1.14.2"' values.yaml && sed -i -e 's/^replicaCount: 1/replicaCount: 3/' -e 's/^serviceName: "nginx"/serviceName: "mynginx"/' -e 's/^image: "nginx:1.14.2"/image: "nginx:1.18.0"/' values.yaml && echo "Values have been replaced, the sts must be restarted"

# a much better way to do this is with yq
# yq eval '.replicaCount = 3 | .serviceName = "mynginx" | .image = "nginx:1.18.0"' -i values.yaml
