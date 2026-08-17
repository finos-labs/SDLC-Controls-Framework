---
sequence: 21
title: Infrastructure Dependencies
layout: mitigation
doc-status: Draft
type: PREV
phase: RELEASE
mitigates:
  - ri-7  # Configuration Drift
  - ri-4  # Vulnerable Software in Production
  - ri-5  # Audit and Compliance Evidence Failure
chain:
  - Inventory
related_mitigations:
  - mi-9   # Component Inventory
  - mi-17  # Service Dependency Control
---

## Summary

Infrastructure Dependencies provides visibility into the infrastructure resources required to host and operate a software system. By maintaining an accurate inventory of the compute, network, and storage resources a given software system requires, we can better manage the system throughout its lifecycle. This improves operational visibility, supports security and compliance activities, and reduces the risk associated with unmanaged or unknown infrastructure requirements. The primary goal is to ensure that each software system is supported by the appropriate infrastructure and that those infrastructure requirements are understood and governed throughout the software lifecycle.

## Description

Infrastructure Dependencies is the practice of identifying, documenting, and maintaining an up-to-date record of the infrastructure resources required to support the software under management. This includes the compute, network, storage resources and identity and access management on which an application depends, regardless of whether it is deployed on-premises, in cloud environments, or across hybrid infrastructures.

Examples of infrastructure resources include:

* **Compute resources** such as physical servers, virtual machines, containers, Kubernetes clusters, and serverless execution environments.
* **Network resources** such as load balancers, network segments, gateways, DNS services, and connectivity components.
* **Storage resources** such as file systems, object storage, block storage, network-attached storage, relational databases, NoSQL databases, data warehouses, and managed database services.
* **Identity and Access Management** such as customer, employee, and privileged.

Maintaining an accurate list of infrastructure dependencies enables organizations to understand system requirements for deployment, identify ownership and accountability, assess the impact of infrastructure changes, and support operational, security, and compliance activities.

Infrastructure Dependencies enables organizations to appropriately plan and react to changes in underlying infrastructure caused by planned and unplanned outages. It supports software management during platform upgrades, vulnerability remediation efforts, capacity planning, and infrastructure migrations. This control complements Component Inventory and Service Dependency Control by providing visibility into the infrastructure resources that software components and services depend upon at runtime.

## Requirements

* Infrastructure dependencies MUST include the compute, network, storage, and identity resources that support production workloads.
* Compute resources MUST include deployment and hosting information where applicable, such as:
  * Physical servers
  * Virtual machines
  * Containers
  * Kubernetes clusters
  * Serverless execution environments
* Network resources MUST include infrastructure components that provide connectivity, routing, traffic management, or external access where applicable, such as:
  * Load balancers
  * DNS services
  * Network gateways
  * Network segments
* Storage resources MUST include infrastructure used for persistent data storage where applicable, including:
  * File systems
  * Object storage
  * Block storage
  * Relational databases
  * NoSQL databases
  * Data warehouses
* Identity resources MUST include infrastructure used for persistent identity storage, including:
  * Identity stores
  * Certificate vaults
  * Privileged access management stores
* Each infrastructure resource MUST include ownership information to ensure accountability for maintenance, security, and operational support.
* The dependencies MUST identify the infrastructure resources associated with that system, application, or service.
* Infrastructure dependencies records MUST include deployment location information where applicable, such as:
  * On-premises environments
  * Cloud environments
  * Hybrid environments
  * Geographic regions or data centers
* Infrastructure dependencies data MUST be reviewed and updated whenever infrastructure resources associated with the software are added, modified, migrated, or decommissioned.
* Decommissioned infrastructure dependencies MUST be removed from active dependency lists or clearly identified as retired.
* Changes to infrastructure resources MUST be reflected in the dependency list as part of the organization’s change management process.
* Organizations SHOULD endeavor to put practices in place to maintain Infrastructure Dependencies lists aligned with Infrastructure Asset Management Inventories.

## Examples & Commentary

* **Software Deployment**

  A software system is being prepared for production deployment. Infrastructure Dependencies identifies the compute, network, storage, and identity resources required to operate the system, enabling teams to confirm that the appropriate infrastructure has been provisioned and that required dependencies are understood before deployment.

* **Vulnerability Remediation**

  A critical vulnerability is identified in an infrastructure platform or resource used by a software system. Infrastructure Dependencies enables teams to determine whether the software depends on the affected infrastructure, assess the potential impact, and coordinate remediation or migration activities with the appropriate infrastructure owners.

* **Platform Upgrade**

  A software system depends on a Kubernetes cluster that is scheduled for an upgrade. Infrastructure Dependencies provides visibility into the system's reliance on the affected platform, enabling teams to assess compatibility, coordinate testing and deployment activities, and manage the risk of disruption to the software.

* **Infrastructure Migration**

  A software system is being migrated from an on-premises environment to a cloud environment. Infrastructure Dependencies identifies the compute, network, storage, identity, and location requirements supporting the system, enabling teams to plan the target environment and verify that required infrastructure dependencies are preserved during the migration.

* **Operational Incident**

  A software system experiences a production outage caused by the failure of an underlying load balancer or other infrastructure resource. Infrastructure Dependencies enables responders to identify the infrastructure supporting the affected software, determine ownership, understand relevant dependencies, and coordinate recovery activities with the responsible teams.

* **Software Decommissioning**

  A software system is being retired. Infrastructure Dependencies identifies the infrastructure resources associated with the system, enabling teams to determine which compute, network, storage, and identity resources may also be decommissioned or reassigned while reducing the risk of removing infrastructure still required by other systems.
