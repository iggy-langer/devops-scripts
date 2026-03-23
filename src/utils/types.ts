// types.ts
import { execSync } from 'child_process';

interface Creds {
  username: string;
  password: string;
  token: string;
}

interface Config {
  github: {
    username: string;
    password: string;
    token: string;
    owner: string;
    repo: string;
    branch: string;
  };
  docker: {
    host: string;
    port: number;
    username: string;
    password: string;
  };
  kubernetes: {
    clusterName: string;
    namespace: string;
  };
}

interface Manifest {
  apiVersion: string;
  kind: string;
  metadata: {
    name: string;
    namespace: string;
  };
  spec: {
    containers: {
      name: string;
      image: string;
      ports: {
        containerPort: number;
      }[];
    }[];
  };
}

interface KubernetesConfig {
  clusterName: string;
  namespace: string;
  manifest: Manifest;
}

interface Deployment {
  name: string;
  image: string;
  ports: { containerPort: number }[];
  env: { name: string; value: string }[];
}

interface Image {
  name: string;
  tag: string;
  secret: string;
  port: number;
}