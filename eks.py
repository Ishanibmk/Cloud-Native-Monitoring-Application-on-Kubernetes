from eks import client, config

#load Kubernetes configuration
config.load_kube_config()

#create a kubernetes client api
api_client = client.ApiClient()

#Define the deployment
deployment = client.V1Deployment(
    api_version="apps/v1",
    kind="Deployment",
    metadata=client.V1ObjectMeta(name="my-deployment"),
    spec=client.V1DeploymentSpec(
        replicas=2,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "my-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-container",
                        image="663881823323.dkr.ecr.us-east-1.amazonaws.com/my-cloud-native-repo:latest",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
) 

#Create the deployment in the default namespace
apps_v1 = client.AppsV1Api(api_client)
api_v1.create_namespaced_deployment(
    namespace="default",
    body=deployment
)

#define the service
service = client.V1Service(
    api_version="v1",
    kind="Service",
    metadata=client.V1ObjectMeta(name="my-service"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-app"},
        ports=[client.V1ServicePort(port=5000, target_port=5000)],
        type="LoadBalancer"
    )
)

#Create the service
api_v1=client.CoreV1Api(api_client)
api_v1.create_namespaced_service(
    namespace="default",
    body=service
)