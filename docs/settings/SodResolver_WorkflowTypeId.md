# SoD Resolver Workflow Type

**Technical Name:** SodResolver_WorkflowTypeId

**Category:** SOD

**Default Value:** 

**Impact Level:** High

**Description:**

The SoD Resolver Workflow Type parameter is designed to specify the type of workflow process to be engaged in resolving Separation of Duties (SoD) conflicts within the Pathlock Cloud GRC platform. It guides the resolution process, ensuring that SoD conflicts are addressed according to the configured workflow type.

**Business Impact:**

By configuring the SoD Resolver Workflow Type, organizations can streamline and standardize the process of resolving SoD conflicts, leading to a more efficient risk management process. It helps in mitigating risks associated with unauthorized access and conflicting activities within critical systems, thus maintaining compliance with regulatory requirements and internal policies.

**Technical Impact when configured:**

When configured, this parameter directly influences the workflow for resolving SoD violations, enabling automated processes or guiding manual interventions based on the specified workflow type. This may affect how quickly and effectively SoD conflicts are resolved and how mitigation efforts are documented within the system.

**Examples Scenario:**

A company implements the SoD Resolver Workflow Type to automate the resolution of SoD conflicts in their financial system. When an SoD conflict is detected, the system automatically assigns a pre-defined mitigation task to the relevant manager, streamlines the review process by predefined criteria, and records the resolution steps for audit purposes.

**Related Settings:**

- SodFullReportRunOfflineUsers
- SodMitigatedUsersGroupId

**Best Practices:** Configure the SoD Resolver Workflow Type at the initial setup of the Pathlock platform to ensure that any detected SoD conflicts are managed according to organizational policies. Avoid manual intervention without recorded reasons to maintain an auditable trail of SoD conflict resolutions.