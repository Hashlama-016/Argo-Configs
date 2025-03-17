# 🌟 App of Apps Project

This repository implements the **"App of Apps"** pattern for GitOps-based Kubernetes deployments, likely using **ArgoCD** or a similar GitOps tool.

## 📝 Overview

The **"App of Apps"** pattern is a deployment strategy that uses a **parent application** to manage and orchestrate multiple **child applications**. This approach provides a centralized way to manage deployments across multiple environments and applications.

## 📁 Repository Structure

- `apps/` - Directory containing application-specific configurations 🛠️
- `services/` - Directory containing service definitions and configurations 🌐
- `applications.yaml` - Main manifest that defines the applications to be deployed 📜

## 🚀 Usage

This repository serves as a central control point for deploying and managing multiple applications in your Kubernetes cluster. The `applications.yaml` file acts as the entry point that ArgoCD uses to synchronize all child applications.
