import kubernetes

namespace = 'default'

kubernetes.config.load_kube_config()
v1 = kubernetes.client.CoreV1Api()
pods = v1.list_namespaced_pod(namespace, label_selector='dist=ubuntu')
for p in pods.items:
    print (p.metadata.name)
