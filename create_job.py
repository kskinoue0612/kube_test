import kubernetes
from kubernetes import client

def create_job_object():
    # Configureate Pod template container
    container = client.V1Container(
        name="pi",
        image="perl",
        command=["perl", "-Mbignum=bpi", "-wle", "print bpi(2000)"])

    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "pi"}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container]))

    # Create the specification of deployment
    spec = client.V1JobSpec(
        template=template,
        backoff_limit=4)
 
    # Instantiate the job object
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name="pi-4", labels={"vtype": "pi"}),
        spec=spec)

    return job

namespace = 'default'

kubernetes.config.load_kube_config()
v1 = kubernetes.client.BatchV1Api()

job = create_job_object()

resource = v1.create_namespaced_job(namespace, job)
print(resource)
