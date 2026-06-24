---
sequence: 21
title: Infrastructure Inventory
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

Infrastructure Inventory provides visibility into the infrastructure resources used to host and operate software systems. By maintaining an accurate inventory of compute, network, and storage resources, organizations can understand what infrastructure exists, who owns it, where it is deployed, and how it is managed throughout its lifecycle. This improves operational visibility, supports security and compliance activities, and reduces the risk associated with unmanaged or unknown infrastructure.
## Description

Infrastructure Inventory is the practice of identifying, documenting, and maintaining an up-to-date record of the infrastructure resources that support software systems and services.
This includes the compute, network, and storage resources on which applications depend, regardless of whether they are deployed on-premises, in cloud environments, or across hybrid infrastructures.

Examples of infrastructure resources include:

* **Compute resources** such as physical servers, virtual machines, containers, Kubernetes clusters, and serverless execution environments.
* **Network resources** such as load balancers, network segments, gateways, DNS services, and connectivity components.
* **Storage resources** such as file systems, object storage, block storage, network-attached storage, relational databases, NoSQL databases, data warehouses, and managed database services.

Maintaining an accurate infrastructure inventory enables organizations to understand where systems are deployed, identify ownership and accountability, assess the impact of infrastructure changes, and support operational, security, and compliance activities.

Infrastructure inventory helps organizations quickly identify affected infrastructure during outages, platform upgrades, vulnerability remediation efforts, capacity planning activities, and infrastructure migrations. It also reduces the risk of unmanaged, undocumented, or obsolete infrastructure remaining in production environments.
This control complements Component Inventory and Service Dependency Control by providing infrastructure-level visibility into the resources that software components and services depend upon at runtime.

## Requirements
* Infrastructure resources MUST be documented and maintained in an inventory for all production systems.
* Infrastructure inventory MUST include the compute, network, and storage resources that support production workloads.
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
* Each infrastructure resource MUST include ownership information to ensure accountability for maintenance, security, and operational support.
* The inventory MUST identify the system, application, or service associated with each infrastructure resource.
* Infrastructure inventory records MUST include deployment location information where applicable, such as:
  * On-premises environments
  * Cloud environments
  * Hybrid environments
  * Geographic regions or data centers
* Infrastructure inventory records MUST include lifecycle status information (e.g., active, planned for decommissioning, retired).
* Infrastructure inventory data MUST be reviewed and updated whenever infrastructure resources are added, modified, migrated, or decommissioned.
* Decommissioned infrastructure MUST be removed from active inventories or clearly identified as retired.
* Changes to infrastructure resources MUST be reflected in the inventory as part of the organization’s change management process.

## Examples & Commentary

* **Vulnerability Remediation**

  A critical operating system vulnerability is identified affecting a specific server image version. Infrastructure Inventory enables teams to quickly identify all affected servers, virtual machines, containers, and Kubernetes nodes using the vulnerable image, allowing remediation efforts to be prioritized and coordinated.

* **Infrastructure Migration**

  An organization plans to migrate workloads from an on-premises data center to a cloud provider. Infrastructure Inventory provides visibility into the compute, network, and storage resources supporting each application, enabling migration planning and reducing the risk of overlooked infrastructure dependencies.

* **Capacity Planning**

  A production database approaches storage capacity limits. Infrastructure Inventory allows teams to identify the affected database platform, associated storage resources, ownership information, and dependent applications, enabling timely capacity expansion and reducing the risk of service disruption.

* **Platform Upgrade**

  A Kubernetes platform upgrade is scheduled. Infrastructure Inventory helps identify affected clusters, workloads, and supporting infrastructure resources, enabling teams to assess impact, coordinate activities, and reduce upgrade-related risk.

* **Incident Response**

  A production outage occurs due to a failed load balancer. Infrastructure Inventory enables responders to quickly identify the affected infrastructure component, determine ownership, understand which systems depend on it, and coordinate recovery activities.

* **Infrastructure Decommissioning**

  An organization plans to retire a legacy server environment. Infrastructure Inventory helps identify associated storage resources, databases, network dependencies, and consuming applications, reducing the risk of disrupting active systems during decommissioning.

