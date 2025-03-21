**Shadow System**

**Technical Name:** ShadowSystemId

**Category:** Workflow

**Default Value:** None

**Impact Level:** High

**Description:**

The ShadowSystemId parameter is utilized within the context of Pathlock Cloud GRC platform workflows to identify and operate on shadow systems. A shadow system in this context refers to secondary or auxiliary systems that run in parallel to primary systems, often to support specific workflows or processes without altering the state of primary systems directly.

**Business Impact:**

The correct configuration of the ShadowSystemId is crucial for maintaining accurate and effective governance, risk, and compliance (GRC) processes within an organization. By ensuring proper identification and handling of shadow systems, organizations can mitigate risks associated with unregulated data access and processing, enhance compliance with internal and external regulations, and maintain the integrity of their security posture.

**Technical Impact when configured:**

When the ShadowSystemId is correctly configured, it allows for a precise targeting and execution of workflow actions on the appropriate shadow systems. This ensures that workflow actions, such as starting workflows for specific user roles or processing compliance checks, are accurately directed, thereby maintaining system integrity and compliance.

**Examples Scenario:**

For instance, in an organization with a primary HR system and a shadow system for processing employee role changes, the ShadowSystemId could be used to start workflows specific to role change approvals and audits in the shadow system without impacting the primary HR system's operation. This would allow the HR department to manage changes in a controlled environment, enhancing the organization's compliance and auditability.

**Related Settings:** N/A

**Applicable Workflows Actions:** StartWorkflows

**Best Practices:** 

- **configure when**: Implementing shadow systems for parallel processing of specific workflows to ensure these workflows do not directly impact the primary system's data integrity.
  
- **avoid when**: There is no clear separation of concerns between primary and shadow systems, or when workflows do not require a separate system to process their actions, to prevent unnecessary system complexity and potential data inconsistency.