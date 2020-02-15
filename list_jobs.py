import kubernetes

namespace = 'default'

kubernetes.config.load_kube_config()
v1 = kubernetes.client.BatchV1Api()
jobs = v1.list_namespaced_job(namespace)
for j in jobs.items:
    print (j.metadata.name)
